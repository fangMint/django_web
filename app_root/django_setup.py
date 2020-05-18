import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_root.settings")


def setup():
    django.setup()
