from django.db import models
from jwt import ExpiredSignatureError, DecodeError, InvalidIssuerError

from .token import Token
from libs.tool_fun import md5

from .config import ORIGINAL_PW


def encryption(pw):
    return md5(pw)


class UsersManage(models.Manager):

    def user_create(self, **kwargs):
        user = self.model()
        user.name = kwargs["name"]
        user.account = kwargs["account"]
        user.user_type = kwargs["user_type"]
        user.password = encryption(kwargs["password"])
        user.gender = kwargs["gender"] if "gender" in kwargs else 1
        user.email = kwargs["email"]
        user.portrait = kwargs["portrait"] if "portrait" in kwargs else "https://avatar.csdnimg.cn/2/3/C/2_mantoo123.jpg"
        user.permission = 1
        user.save()
        return user

    def delete_by_pk(self, pk: int):
        user = self.filter(id=pk).first()
        if user:
            user.delete()
            return True
        return False


class Users(models.Model):
    USER_TYPES = ((1, "角色1"), (2, "角色2"), (3, "角色3"), (4, "角色4"))
    GENDER_TYPES = ((0, "女"), (1, "男"))
    PERMISSION_TYPE = ((0, "否"), (1, "可"))

    name = models.CharField(max_length=20, verbose_name="用户名")
    account = models.CharField(max_length=20, unique=True, verbose_name="账号(暂定手机号)")
    user_type = models.IntegerField(choices=USER_TYPES, verbose_name="用户类别")
    password = models.CharField(max_length=50, verbose_name="用户密码")
    gender = models.IntegerField(choices=GENDER_TYPES, default=1, verbose_name="性别")
    email = models.EmailField(max_length=100, verbose_name="邮箱")
    portrait = models.URLField(max_length=300, verbose_name="头像链接")
    permission = models.IntegerField(choices=PERMISSION_TYPE, verbose_name="是否可登陆")
    register_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    last_login_time = models.DateTimeField(auto_now_add=True, verbose_name="上次登录时间")

    objects = UsersManage()

    class Meta:
        verbose_name_plural = verbose_name = "用户"

    def authentication(self, pw):
        return self.password == encryption(pw)

    def reset_password(self):
        self.password = encryption(ORIGINAL_PW)
        self.save()

    def __str__(self):
        return self.name


class TokensManage(models.Manager):

    token = Token()

    def token_create(self, user_id, token_type):
        token_dc = self.token.encode({"user_id": user_id})
        token_old_m = self.filter(user_id=user_id, token_type=token_type).first()
        if token_old_m:
            token_old_m.token = token_dc
            token_old_m.save()
        else:
            token_m = self.model(user_id=user_id, token_type=token_type, token=token_dc)
            token_m.save()
        return token_dc

    def token_decode(self, recv_token):
        try:
            payload = self.token.decode(recv_token)
            user_id = payload["data"]["user_id"]
            return user_id
        except ExpiredSignatureError:
            # TODO token过期要删除
            return False
        except DecodeError:
            return False
        except InvalidIssuerError:
            return False
        except BaseException:
            raise

    def token_check(self, recv_token):
        user_id = self.token_decode(recv_token)
        if user_id and self.filter(user_id=user_id, token=recv_token).exists():
            return user_id
        return False


class Tokens(models.Model):
    TOKEN_TYPE = ((1, "web"),
                  (2, "android"))
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="所属用户")
    token = models.TextField(verbose_name="用户token")
    token_type = models.IntegerField(choices=TOKEN_TYPE, verbose_name="token类型")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="token创建时间")
    # expire_at = models.DateTimeField(verbose_name="token结束时间")

    objects = TokensManage()

    class Meta:
        verbose_name_plural = verbose_name = "token"

    def __str__(self):
        return f"token对象{self.pk}"  # print的时候会显示
