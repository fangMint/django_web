# ==================================
# Author   : fang
# Time     : 2020/4/22 下午7:58
# Email    : zhen.fang@qdreamer.com
# File     : task_handler.py
# Software : PyCharm
# ==================================
import datetime

from apscheduler.schedulers.background import BackgroundScheduler


class MyScheduler:
    def __init__(self, start=True):
        self.__scheduler = BackgroundScheduler()
        if start:
            self.sys_start()

    def sys_start(self):
        self.__scheduler.start()

    def __add_job(self, func, trigger=None, args=None, kwargs=None, id=None, name=None,
                  jobstore='default', executor='default',
                  replace_existing=False, **trigger_args
                  ):
        self.__scheduler.add_job(func, trigger, args, kwargs, id, name, jobstore=jobstore, executor=executor,
                                 replace_existing=replace_existing, **trigger_args)

    def cron_add_job(self, func, day_of_week='0-6', hour=0, minute=0, second=0, _datetime=""):
        """

        :param func:
        :param day_of_week:
        :param hour:
        :param minute:
        :param second:
        :param _datetime: 存在时会忽略其它参数
        :return:
        """
        if _datetime:
            pass
        self.__add_job(func, "cron", day_of_week=day_of_week, hour=hour, minute=minute, second=second)

    def interval_add_job(self, func, seconds=0):
        self.__add_job(func, "interval", seconds=seconds)
