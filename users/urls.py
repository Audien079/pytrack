from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView
from users.views import CustomLoginView, SignUpView


urlpatterns = [
    path("", RedirectView.as_view(url="/login/", permanent=False), name="dashboard-redirect"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
