from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import MyUserManager


class BaseModel(models.Model):
    """
    Base model
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    """
    User model
    """

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    last_contacted = models.DateTimeField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.username}"

    objects = MyUserManager()
