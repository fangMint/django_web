import time

import requests

from libs.tool_fun import md5


class ConnectBoss:
    """
    与后端服务器交互
    2020-01-04 增加与资源服务器的交互

    初始化参数从配置文件中获取
    与服务器交互需要key生成的签名进行身份验证
    """

    def __init__(self):
        self.box = QBOX_MARK
        self.key = QBOX_SECRET_KEY
        self.time_stamp = int(round(time.time() * 1000))
        self.timeout = (5, 10)
        self.debug = True
        self.request_url = None
        self.request_param = None
        self.response = None

    def inspect(self):
        if self.debug:
            print(f"请求连接 {self.request_url}")
            print(f"请求参数 {self.request_param}")
            print(f"返回参数 {self.response}")

    def return_result(self, response):
        if response.status_code != 500:
            response_json = response.json()
            self.response = response_json
            self.inspect()
            return response_json
        self.inspect()
        return 0

    def get_send_dict(self):
        """
        获取的加密签名等信息
        """
        sign = f"authTime={self.time_stamp}" \
               f"{md5(self.key)}"
        send_data = {
            "QBoxMark": self.box,
            "authTime": self.time_stamp,
            "authSign": md5(sign)
        }
        self.request_param = send_data
        return send_data

    def get_request(self, url,  **params):
        """
        请求boss服务器
        :param url:

        :param params: 参数

        :return:
        """
        self.request_url = url
        send_data = self.get_send_dict()

        for k, v in params.items():
            send_data[k] = v

        try:

            response = requests.get(url, params=send_data, timeout=self.timeout)

            return self.return_result(response)

        except BaseException as err:
            print(f"连接远程服务器 ———> {err}")
            pass

    def post_request(self, url, body=True, files=None, **params):
        """
        :param url:
        :param body: 参数是否放body中
        :param files: 文件
        :param params: 参数
        :return:
        """

        self.request_url = url

        try:
            send_data = self.get_send_dict()

            for k, v in params.items():
                send_data[k] = v

            if body:
                response = requests.post(url, json=send_data, files=files, timeout=self.timeout)
            else:
                response = requests.post(url, data=send_data, files=files, timeout=self.timeout)

            return self.return_result(response)

        except BaseException as err:
            print(f"连接远程服务器 ———> {err}")
            pass

    # def sign_change_state(self, data_dict, state_type):
    #     url = get_config(REMOTE=["STEP_SIGN_STATE_URL"])
    #     return self.request(url, stateType=state_type, dataDict=data_dict)
    #
    # def send_resource(self, file):
    #     # host, port, url = get_config(RESOURCE=["HOST", "PORT", "SAVE_VOICE"])
    #     host = '139.196.8.173'
    #     port = 8029
    #     url = '/doubleTeacher/save/voice'
    #     full_url = f"http://{host}:{port}{url}"
    #     self.request(full_url, url_full=True, files=file)


if __name__ == '__main__':
    REMOTE_HOST = '127.0.0.1'
    REMOTE_PORT = 8000
    REMOTE_ADDRESS = f'http://{REMOTE_HOST}:{REMOTE_PORT}'
    UPDATE_AL_URL = f'{REMOTE_ADDRESS}/qBox/check/arrangeLesson'
    connection = ConnectBoss()
    res = connection.get_request(UPDATE_AL_URL)
    print(res)

