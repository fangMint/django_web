import hashlib
import socket
import time
import uuid


def get_host_ip():
    """
    获取-网络-IP
    利用 UDP 协议来实现的，生成一个UDP包，把自己的 IP 放到 UDP 协议头中，然后从UDP包中获取本机的IP
    这个方法并不会真实的向外部发包，所以用抓包工具是看不到的。但是会申请一个 UDP 的端口，
    所以如果经常调用也会比较耗时的
    :return:
    """
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.baidu.com', 8000))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def md5(s):
    m = hashlib.md5(s.encode('utf8'))
    return m.hexdigest()


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])


if __name__ == '__main__':
    print(get_host_ip())
    print(md5("qmz0102_qmz01pk0040201_qmz0101"))
