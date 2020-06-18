# ==================================
# Author   : fang
# Time     : 2020/5/28 15:44
# Email    : zhen.fang@qdreamer.com
# File     : token.py
# Software : PyCharm
# ==================================
import datetime
import jwt
from . import config


class Token:
    def __init__(self):
        self.sign = config.TOKEN_SIGN
        self.algorithm = config.TOKEN_ALGORITHM
        self.exp = config.TOKEN_EXP

    def encode(self, data):
        iat = datetime.datetime.utcnow()
        exp = iat + datetime.timedelta(seconds=self.exp)
        payload = {
            "iat": iat,
            "exp": exp,
            "iss": self.sign,
            "data": data

        }
        token = jwt.encode(payload, "secret", self.algorithm)
        return token.decode()

    def decode(self, recv_token):
        return jwt.decode(recv_token, "secret", self.sign, self.algorithm)