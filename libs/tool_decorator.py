import json
import functools
import logging

from libs.response_extra import response_failure


def method(request_method):
    """
    验证请求方式装饰器
    :param request_method:
    :return:
    """
    def check_method(func):
        def in_fun(*request):
            if request[0].method == request_method:
                return func(*request)
            else:
                return response_failure(msg=f"请求方式不是{request_method}", code=1)
        return in_fun
    return check_method


def params(**kwargs):
    """
    验证请求参数装饰器
    :param kwargs:
    :return:
    """
    """
    里面居然会在项目启动的时候执行？？
    """
    def function(func):
        """
        里面居然也会在项目启动的时候执行？？
        """
        def in_fun(*request):
            request_method = None
            params = None
            for k, v in kwargs.items():
                request_method = k
                params = v
            if request_method == "POST":
                request_post = request[0].POST
                p = {}
                for val in params:  # 遍历客户端请求是否包含字段
                    param = request_post.get(val, None)
                    if not param:
                        return response_failure(msg=f'需要参数{val}', code=3)
                    if isinstance(param, str):
                        param = param.strip()
                    p[val] = param  # 若包含则返回给被装饰的函数
                return func(*request, p)
            if request_method == "POST_BODY":
                request_body = request[0].body
                if request_body:
                    p = {}
                    post_body = json.loads(request_body)
                    for val in params:  # 遍历客户端请求是否包含字段
                        try:
                            param = post_body[val]
                            if isinstance(param, str):
                                param = param.strip()
                            p[val] = param  # 若包含则返回给被装饰的函数
                        except:
                            return response_failure(msg=f'需要参数{val}', code=3)
                    return func(*request, p)
                return response_failure(msg=f'请携带参数请求', code=3)
            elif request_method in ["GET", "DELETE"]:
                request_get = request[0].GET
                p = {}
                for val in params:  # 遍历客户端请求是否包含字段
                    param = request_get.get(val, None)
                    if not param:
                        return response_failure(msg=f'需要参数{val}', code=3)
                    if isinstance(param, str):
                        param = param.strip()
                    p[val] = param  # 若包含则返回给被装饰的函数
                return func(*request, p)
        return in_fun
    return function


# def pure_check(length):
#     """
#     检查数据数是否足够
#     :param length:需要的参数个数
#     :return:
#     """
#     def check_params(func):
#         @functools.wraps(func)
#         def in_fun(*args):
#             try:
#                 if len(*args) == length:
#                     return func(*args)
#                 return raise_mark_msg(0, 1, "请求参数不全")
#             except ValueError as e1:
#                 e = f"函数{func.__name__}调用提取参数装饰器发生错误：{e1}"
#                 logging.error(e)
#                 return raise_mark_msg(0, 1, e)
#         return in_fun
#     return check_params


def cvb_params(**kwargs):
    """
    验证请求参数装饰器
    :param kwargs:
    :return:
    """
    """
    里面居然会在项目启动的时候执行？？
    """
    def function(func):
        """
        里面居然也会在项目启动的时候执行？？
        """
        def in_fun(self, *request):
            request_method = None
            params = None
            for k, v in kwargs.items():
                request_method = k
                params = v
            if request_method == "POST":
                request_post = request[0].POST
                p = {}
                for val in params:  # 遍历客户端请求是否包含字段
                    param = request_post.get(val, None)
                    if not param:
                        return response_failure(msg=f'需要参数{val}', code=3)
                    p[val] = param  # 若包含则返回给被装饰的函数
                return func(self, *request, p)
            if request_method == "POST_BODY":
                request_body = request[0].body
                if request_body:
                    p = {}
                    post_body = json.loads(request_body)
                    for val in params:  # 遍历客户端请求是否包含字段
                        try:
                            find_flag = val.find(":?")
                            if find_flag > 0:  # 可选参数
                                val = val[:find_flag]
                                if val in post_body.keys():
                                    param = post_body[val]
                                else:
                                    param = None
                            else:
                                param = post_body[val]
                            p[val] = param  # 若包含则返回给被装饰的函数
                        except:
                            return response_failure(msg=f'需要参数{val}', code=3)
                    return func(self, *request, p)
                return response_failure(msg=f'请携带参数请求', code=3)
            elif request_method in ["GET", "DELETE"]:
                request_get = request[0].GET
                p = {}
                for val in params:  # 遍历客户端请求是否包含字段
                    if val not in request_get:
                        return response_failure(msg=f'需要参数{val}', code=3)
                    param = request_get.get(val, None)
                    p[val] = param  # 若包含则返回给被装饰的函数
                return func(self, *request, p)

            else:
                return response_failure(msg=f'未知类型{request_method}', code=3)
        return in_fun
    return function


def get_token(func):
    """
    验证用户token是否存在
    :param func:
    :return:
    """
    def wrapper(*args):
        request_header = args[1].headers
        return func(*args, request_header["token"])
    return wrapper


def fvb_get_token(func):
    """
    验证用户token是否存在
    :param func:
    :return:
    """
    def wrapper(*args):
        request_header = args[0].headers
        return func(*args, request_header["token"])
    return wrapper