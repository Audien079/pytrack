from website.models import Website, PageStat, Visitor
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils.timezone import now, timedelta
from django.db.models import Count, Avg
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

        # Determine date range and grouping
        if filter_option == "last_7_days":
            start_date = today - timedelta(days=7)
            date_range = [start_date + timedelta(days=i) for i in range(8)]
            grouping = TruncDate("created_at")
        elif filter_option == "last_30_days":
            start_date = today - timedelta(days=30)
            date_range = [start_date + timedelta(days=i) for i in range(31)]
            grouping = TruncDate("created_at")
        elif filter_option == "all_time":
            start_date = None
            date_range = None  # No specific range for all-time data
            grouping = TruncDate("created_at")
        elif filter_option == "today":
            start_date = today
            date_range = None  # Group by hours for today
            grouping = TruncHour("created_at")
        else:
            return []

        # Fetch and process visitor data
        visitor_data = PageStat.objects.filter(created_at__gte=start_date) if start_date else PageStat.objects.all()
        visitor_data = (
            visitor_data.annotate(period=grouping)
            .values("period")
            .annotate(count=Count("id"))
            .order_by("period")
        )

        # Calculate metrics
        total_visits = visitor_data.count()
        total_page_views = visitor_data.values("page_url").distinct().count()
        avg_visit_duration = visitor_data.aggregate(avg_duration=Avg("visit_duration"))["avg_duration"] or 0
        single_page_visits = visitor_data.filter(referrer__isnull=True).count()
        bounce_rate = f"{int((single_page_visits / total_visits) * 100)}%" if total_visits else "0%"
        unique_visitors = Visitor.objects.filter(
            id__in=visitor_data.values_list("visitor", flat=True).distinct()
        ).count()
        minutes, seconds = divmod(int(avg_visit_duration), 60)
        avg_visit_duration_str = f"{minutes}m {seconds}s"

        # Prepare the filter dictionary
        filter_dict = {
            "total_visits": total_visits,
            "total_page_views": total_page_views,
            "average_visit_duration": avg_visit_duration_str,
            "bounce_rate": bounce_rate,
            "unique_visitors": unique_visitors,
        }

        # Add filter-specific data
        if filter_option in {"last_7_days", "last_30_days"}:
            visitor_dict = {entry["period"]: entry["count"] for entry in visitor_data}
            filter_dict["filter_data"] = [
                {"day": day, "count": visitor_dict.get(day, 0)} for day in date_range
            ]
        elif filter_option == "all_time":
            filter_dict["filter_data"] = [
                {"day": entry["period"], "count": entry["count"]} for entry in visitor_data
            ]
        elif filter_option == "today":
            filter_dict["filter_data"] = [
                {"hour": entry["period"], "count": entry["count"]} for entry in visitor_data
            ]

        return [filter_dict]

    def post(self, request, *args, **kwargs):
        """
        Handle AJAX requests for chart data.
        """
        filter_option = request.POST.get("filter_option", "last_30_days")
        data = self.get_chart_data(filter_option)
        return JsonResponse(data, safe=False)
