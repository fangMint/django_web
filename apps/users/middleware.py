# ==================================
# Author   : fang
# Time     : 2020/5/28 13:47
# Email    : zhen.fang@qdreamer.com
# File     : middleware.py
# Software : PyCharm
# ==================================
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from .models import Tokens

white_list = [
    '/user/login',  # 登录
    '/user/register',  # 注册
]


class TokenMiddle(MiddlewareMixin):

    def white_validator(self, next_url):
        return next_url in white_list or next_url.find("admin") > 0

    def process_request(self, request):
        from django.shortcuts import redirect, HttpResponse
        next_url = request.path_info  # next_url请求url
        # print("请求url ————> ", next_url)
        if not self.white_validator(next_url):
            headers = request.headers
            if "Token" in headers:
                recv_token = headers["Token"]
                if recv_token:  # 如果token存在
                    check = Tokens.objects.token_decode(recv_token)
                    if check:  # token合格
                        pass
                    else:
                        return JsonResponse({"code": 4001, "im": "token不存在或token过期"})
            else:
                return JsonResponse({"code": 4001, "im": "没有携带token"})
        else:
            pass



