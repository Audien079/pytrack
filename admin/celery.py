from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

import environ
from celery import Celery

env = environ.Env()
env.read_env(str(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")

if env("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = env("DJANGO_SETTINGS_MODULE")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.result_expires = timedelta(days=365)
app.conf.timezone = "UTC"

app.autodiscover_tasks()
