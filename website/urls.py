from django.urls import path
from website.views import HomeView, WebsiteView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('site/<str:site>/', WebsiteView.as_view(), name='website'),
]
