# ==================================
# Author   : fang
# Time     : 2020/4/8 pm 8:55
# Email    : zhen.fang@qdreamer.com
# File     : play_db.py
# Software : PyCharm
# ==================================
import datetime

DB = {}


class PlayDB:
    def __init__(self, inherited=False):
        if inherited:
            self.__store = DB  # 数据暂存空间
        else:
            self.__store = {}

    @staticmethod
    def __timestamp():
        time_stamp = datetime.datetime.now().timestamp()
        time_stamp = int(round(time_stamp * 3000))
        return time_stamp

    def save(self, **kwargs):
        print("进入")
        tc = 0
        for k, v in kwargs.items():
            tc += 1
            if k not in self.__store.keys():
                db_data = {"value": v, "data_stamp": self.__timestamp()}
            else:
                db_data = {"value": v, "data_stamp": self.__store[k]["data_stamp"]}
            self.__store[k] = db_data
        return tc

    def delete(self, key):
        if key in self.__store.keys():
            tv = self.__store.get(key)
            del self.__store[key]
            return {key: tv}
        return False

    def __get_or_consume(self, key, _all=False, _d=False):
        if key in self.__store.keys():
            if not _all:
                this_value = self.__store.get(key)["value"]
            else:
                this_value = self.__store.get(key)
            if _d:
                self.delete(key)
            return this_value
        raise ValueError(f"{key} does not exists in store")

    def get(self, key):
        self.__get_or_consume(key, _all=False, _d=False)

    def consume(self, key):
        self.__get_or_consume(key, _all=False, _d=True)

    def show(self, key, _all=False):
        if key in self.__store.keys():
            if not _all:
                return self.__store.get(key)["value"]
            else:
                return self.__store.get(key)
        raise -1

    def update(self, **kwargs):
        return self.save(**kwargs)


play_global = PlayDB(inherited=True)
