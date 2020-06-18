# ==================================
# Author   : fang
# Time     : 2020/5/28 13:50
# Email    : zhen.fang@qdreamer.com
# File     : decorator.py
# Software : PyCharm
# ==================================
from django.http import JsonResponse

from apps.users.models import Tokens
from libs.response_extra import response_failure


def cvb_token_check(func):
    def wrapper(*args):
        try:
            headers = args[1].headers
            recv_token = headers["Token"]
            if recv_token:
                user_id = Tokens.objects.token_check(recv_token)
                if user_id:
                    return func(*args, user_id)
            return JsonResponse({"code": 4001, "im": "token不存在或token过期"})
        except KeyError:
            return response_failure(msg="缺少token", code=2)
    return wrapper
