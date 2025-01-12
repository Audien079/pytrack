from website.models import Website, PageStat
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils.timezone import now, timedelta
from django.db.models import Count
from django.db.models.functions import TruncHour, TruncDate


class HomeView(TemplateView):
    """
    Website lists page
    """
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["websites"] = Website.objects.all()
        return context


class WebsiteView(TemplateView):
    """
    Website detail view
    """
    template_name = "website/website.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Default filter (last 30 days)
        context['default_filter'] = 'last_30_days'
        return context

    def get_chart_data(self, filter_option):
        """
        Process data based on filter option.
        """
        today = now().date()

        if filter_option == "last_7_days":
            start_date = today - timedelta(days=7)
            date_range = [start_date + timedelta(days=i) for i in range((today - start_date).days + 1)]
            visitor_data = (
                PageStat.objects.filter(created_at__gte=start_date)
                .annotate(day=TruncDate("created_at"))
                .values("day")
                .annotate(count=Count("id"))
                .order_by("day")
            )
            visitor_dict = {entry["day"]: entry["count"] for entry in visitor_data}
            data = [{"day": day, "count": visitor_dict.get(day, 0)} for day in date_range]
        elif filter_option == "last_30_days":
            start_date = today - timedelta(days=30)
            date_range = [start_date + timedelta(days=i) for i in range((today - start_date).days + 1)]
            visitor_data = (
                PageStat.objects.filter(created_at__gte=start_date)
                .annotate(day=TruncDate("created_at"))
                .values("day")
                .annotate(count=Count("id"))
                .order_by("day")
            )
            visitor_dict = {entry["day"]: entry["count"] for entry in visitor_data}
            data = [{"day": day, "count": visitor_dict.get(day, 0)} for day in date_range]

        elif filter_option == "all_time":
            data = list(
                PageStat.objects.annotate(day=TruncDate("created_at"))
                .values("day")
                .annotate(count=Count("id"))
                .order_by("day")
            )
            # visitor_dict = {entry["day"]: entry["count"] for entry in visitor_data}
            # data = [{"day": day, "count": visitor_dict.get(day, 0)} for day in date_range]
        elif filter_option == "today":
            data = list(
                PageStat.objects.filter(created_at__date=today)
                .annotate(hour=TruncHour("created_at"))
                .values("hour")
                .annotate(count=Count("id"))
                .order_by("hour")
            )
        else:
            data = []

        return data

    def post(self, request, *args, **kwargs):
        """
        Handle AJAX requests for chart data.
        """
        filter_option = request.POST.get("filter_option", "last_30_days")
        data = self.get_chart_data(filter_option)
        return JsonResponse(data, safe=False)
