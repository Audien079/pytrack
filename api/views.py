import json, httpagentparser
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from website.models import PageStat, Website


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

                PageStat.objects.create(
                    website=website[0],
                    page_url=page_url,
                    referrer=data.get("referrer", ""),
                    user_agent=data["userAgent"],
                    browser=browser,
                    ip_address=ip
                )
                return JsonResponse({"status": "success"}, status=201)

            else:
                return JsonResponse({"error": "Invalid data"}, status=400)
        except (KeyError, ValueError):
            return JsonResponse({"error": "Invalid data"}, status=400)

    def get(self, request, *args, **kwargs):
        """get method"""
        return JsonResponse({"error": "Method not allowed"}, status=405)
