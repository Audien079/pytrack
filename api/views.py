import json, httpagentparser
from datetime import datetime
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from website.models import PageStat, Website, Visitor


@method_decorator(csrf_exempt, name='dispatch')
class TrackView(View):
    """
    Track api view
    """

    def post(self, request, *args, **kwargs):
        """post method"""
        try:
            data = json.loads(request.body)
            web_page_url = data["pageUrl"]
            domain = web_page_url.split('/')[2]
            page_url = web_page_url.split('//')[1].replace(domain, '')
            website = Website.objects.filter(web_url=domain)

            if website:
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')

                user_agent = request.META.get('HTTP_USER_AGENT', '')
                parsed_agent = httpagentparser.detect(user_agent)
                browser = parsed_agent.get('browser', {}).get('name', 'Unknown')

                visitor, created = Visitor.objects.get_or_create(
                    ip_address=data["ipAddress"],
                    user_agent=data["userAgent"],
                    session_id=data["sessionId"]
                )
                # Calculate visit duration
                previous_stat = PageStat.objects.filter(visitor=visitor).order_by('-created_at').first()
                visit_duration = 0.0

                if previous_stat:
                    visit_duration = (datetime.utcnow() - previous_stat.created_at.replace(tzinfo=None)).total_seconds()

                PageStat.objects.create(
                    website=website[0],
                    page_url=page_url,
                    referrer=data.get("referrer", ""),
                    user_agent=data["userAgent"],
                    browser=browser,
                    ip_address=ip,
                    visit_duration=visit_duration,
                    visitor=visitor
                )
                return JsonResponse({"status": "success"}, status=201)

            else:
                return JsonResponse({"error": "Invalid data"}, status=400)
        except (KeyError, ValueError):
            return JsonResponse({"error": "Invalid data"}, status=400)

    def get(self, request, *args, **kwargs):
        """get method"""
        return JsonResponse({"error": "Method not allowed"}, status=405)
