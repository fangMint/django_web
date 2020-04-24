# ==================================
# Author   : fang
# Time     : 2020/4/24 下午12:07
# Email    : zhen.fang@qdreamer.com
# File     : setting_test.py
# Software : PyCharm
# ==================================
from .setting_base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}