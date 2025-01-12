from django.contrib import admin
from website.models import Website, PageStat


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    """
    Website data view in admin panel
    """

    list_display = ["web_url", "id", "user"]
    search_fields = ["web_url"]


@admin.register(PageStat)
class PageStatAdmin(admin.ModelAdmin):
    """
    PageStat data view in admin panel
    """

    list_display = ["page_url", "website", "ip_address"]
    search_fields = ["page_url"]
