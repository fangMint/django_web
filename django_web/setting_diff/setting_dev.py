# ==================================
# Author   : fang
# Time     : 2020/4/24 上午11:47
# Email    : zhen.fang@qdreamer.com
# File     : setting_dev.py
# Software : PyCharm
# ==================================
from .setting_base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}