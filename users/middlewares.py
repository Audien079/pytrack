from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin
import re


EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
# Other login exempt urls can be added in settings with 'LOGIN_EXEMPT_URLS'


class LoginRequiredMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        assert hasattr(request, 'user')

        path = request.path_info.lstrip('/')

        for endpoint in ["api/", "settings", "mfa", "reset"]:
            if path.startswith(endpoint):
                return self.get_response(request)

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == settings.LOGOUT_URL.lstrip('/'):
            logout(request)

        if request.user.is_authenticated and url_is_exempt:
            # If the user is authenticated and the URL is in the exempt list
            # redirect to the login page
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated or url_is_exempt:
            # Do nothing if the user is authenticated and the URL is not in the
            # exempt list
            return None

        else:
            # Trying to access any page as a non authenticated user
            return redirect(f"{settings.LOGIN_URL}?next=/{path}")

