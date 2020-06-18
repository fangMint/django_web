import logging
from django.views import View

from .models import Users, Tokens
from libs.response_extra import response_failure, response_success, user_does_not_exists, view_exception
from libs.tool_decorator import cvb_params
from .decorator import cvb_token_check


log = logging.getLogger(__name__)


class LoginView(View):
    @cvb_params(POST_BODY=["account", "password"])
    def post(self, request, body_params):
        try:
            request_body = request.headers
            recv_token = request_body["Token"]
            login_type = request_body["platform"] if "platform" in request_body else 1  # 1是网页端
            account = body_params['account']
            password = body_params['password']

            if recv_token == "none":  # 不存在token才登录,“none”是前端兼容IE浏览器
                user_m = Users.objects.filter(account=account).first()
                if user_m:
                    if user_m.permission:  # 验证是否允许登录
                        if user_m.authentication(password):  # 验证密码
                            token = Tokens.objects.token_create(user_m.id, login_type)
                            data = {
                                "account": account,
                                "userType": user_m.user_type,
                                "name": user_m.name,
                                "portrait": user_m.portrait,
                                "token": token
                            }
                            return response_success(msg="登录成功", code=0, data=data)
                        return response_failure(msg='密码错误，请重新输入', code=6)
                    return response_failure(msg='用户被禁止登录', code=7)
                return response_failure(msg="账号不存在", code=5)
            return response_failure(msg="携带token登录", code=4)
        except BaseException as err:
            log.error(f"登录接口异常 {err}")


class LogoutView(View):
    @cvb_token_check
    def get(self, request, user_id):
        request_body = request.headers
        recv_token = request_body["Token"]
        token_m = Tokens.objects.filter(user_id=user_id, token=recv_token).first()
        if token_m:
            token_m.delete()
        return response_success(msg="退出成功")


class RegisterView(View):
    @cvb_params(POST_BODY=['userType', 'name', 'account', 'password', 'email', 'gender', 'portrait'])
    def post(self, request, body_params):
        Users.objects.user_create(
            name=body_params["name"],
            account=body_params["account"],
            password=body_params["password"],
            gender=body_params["gender"],
            email=body_params["email"],
            portrait=body_params["portrait"],
            user_type=body_params["userType"],
        )
        return response_success(msg="添加用户成功")


class ModifyPasswordView(View):
    @cvb_token_check
    @cvb_params(POST_BODY=["oldPassword", "newPassword"])
    def post(self, request, user_id, params):
        """
        {
        "oldPassword":"123456",
        "newPassword":"1q2w3e4r"
        }
        """
        try:
            user = Users.objects.filter(id=user_id).first()
            if user:
                if user.authentication(params["oldPassword"]):
                    user.password = user.encryption(params["newPassword"])
                    user.save()
                    return response_success(msg="密码修改成功", code=0)
                return response_failure(msg='旧密码错误，请重新输入', code=6)
            return user_does_not_exists()
        except BaseException as err:
            log.error(err)
            return view_exception()

"""
注册:
{
"userType": 2,
"name": "rocky_admin",
"account": "13002111111",
"password": "1q2w3e4r",
"email":"rocky_admin@163com",
"gender": 1,
"portrait": "www.baidu.com"

}

登录:
{
"account": "13002111111",
"password": "1q2w3e4r"
}
"""