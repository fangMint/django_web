# ==================================
# Author   : fang
# Time     : 2020/5/26 14:11
# Email    : zhen.fang@qdreamer.com
# File     : singleton.py
# Software : PyCharm
# ==================================
import threading


class Singleton(object):
    instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton.instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self):
        pass


