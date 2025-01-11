import os

import environ
from django.core.wsgi import get_wsgi_application

env = environ.Env()
env.read_env(str(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")

if env("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = env("DJANGO_SETTINGS_MODULE")

application = get_wsgi_application()
