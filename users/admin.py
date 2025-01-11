from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User data view in admin panel
    """

    list_display = ["id", "username", "email"]
    search_fields = ["username", "email"]
