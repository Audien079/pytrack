from django.db import models
from users.models import BaseModel, User


class Website(BaseModel):
    """
    Website model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_websites')
    web_url = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.web_url


class PageStat(BaseModel):
    """
    Page Stat model
    """
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='web_stats')
    page_url = models.CharField(max_length=100)
    referrer = models.URLField(blank=True, null=True)
    user_agent = models.TextField()
    browser = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.website + self.page_url + self.timestamp
