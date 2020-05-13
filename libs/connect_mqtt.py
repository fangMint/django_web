import json
import logging
import paho.mqtt.client as m_client
import time

log = logging.getLogger(__name__)


class MQTTConnect:
    """
    qos:0:最多一次，1:至少一次，2:只有一次
    pub时指定的qos是服务器肯定按此规则接收，但是最终订阅者不一定。
    sub时指定的qos表示订阅者可以接收的最高消息等级，也就是可能收到更低等级的消息。
    """
    def __init__(self, host, port, keepalive=60, qos=0, username=None, password=None, uid_pre="", at=False):
        self.host = host
        self.port = port
        self.uid_pre = uid_pre
        self.username = username
        self.password = password
        self.keepalive = keepalive
        self.qos = qos
        self.subscribe_dict = {}
        self.client = None
        self.__connect(at=at)

    def __connect(self, at=False):
        try:
            client_id = time.strftime(f'{self.uid_pre}%Y%m%d%H%M%S', time.localtime(time.time()))
            # transport会自动在ip上加一个ws://
            client = m_client.Client(
                client_id=client_id,
                transport="websockets",
                clean_session=False
            )
            if self.username and self.password:
                client.username_pw_set(self.username, self.password)
            client.connect_async(self.host, self.port, keepalive=self.keepalive)
            client.on_connect = self.__on_connect
            client.on_subscribe = self.__on_subscribe
            client.on_publish = self.__on_publish
            client.on_disconnect = self.__on_disconnect
            client.loop_start()
            client.will_set("will_topic", payload="i will go back", qos=2, retain=False)
            if at:
                time.sleep(1)
                # 睡一秒解决连接之后不能立刻发送消息
            self.client = client
        except BaseException as err:
            log.error(err)
            raise

    def __on_connect(self, client, user_data, flags, rc):
        log.debug(f"mqtt is connect  {client._client_id} ")
        for topic, callback in self.subscribe_dict.items():
            self.__subscribe(topic, callback)

    def __on_disconnect(self, client, user_data, rc):
        # 项目重启,连接中断都会触发
        log.debug("断开连接", client._client_id)

    def __on_subscribe(self, client, user_data, mid, granted_qos):
        # mid在订阅时也会累加
        log.debug("订阅", client, user_data, mid, granted_qos)

    def __on_publish(self, client, user_data, mid):
        log.debug("mqtt发送", mid)

    def __subscribe(self, t, cb):
        log.debug(f"subscribe {t}")
        self.client.message_callback_add(t, cb)
        self.client.subscribe(t, self.qos)

    def add_subscribe(self, topic, callback):
        self.subscribe_dict[topic] = callback
        self.__subscribe(topic, callback)

    def publish_only(self, topic, payload, qos=None):
        qos = self.qos if not qos else qos
        if isinstance(payload, dict):
            payload = json.dumps(payload)
        elif isinstance(payload, (str, bytearray, int, float)):
            payload = str(payload)
        self.client.publish(topic, payload, qos)

    def show_subscribe(self):
        return self.subscribe_dict.keys()
