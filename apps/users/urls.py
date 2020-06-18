# ==================================
# Author   : fang
# Time     : 2020/5/28 15:09
# Email    : zhen.fang@qdreamer.com
# File     : urls.py
# Software : PyCharm
# ==================================
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ModifyPasswordView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('setPassword', ModifyPasswordView.as_view()),
    # path('retPassword', )
]