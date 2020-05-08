# ==================================
# Author   : fang
# Time     : 2020/4/22 下午7:58
# Email    : zhen.fang@qdreamer.com
# File     : task_handler.py
# Software : PyCharm
# ==================================
import datetime
import logging

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


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
        self.__scheduler.add_listener(self.job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

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

    def date_add_job(self, func, args=None, run_date="", job_id=""):
        # 定时执行一次，执行完之后任务就会自动移除,若错过指定运行时间，任务不会被创建
        self.__add_job(func, "date", args=args, run_date=run_date, id=job_id)

    def date_second(self, func, args=None, seconds=0, minutes=0, hours=0, days=0, job_id=""):
        now_date = datetime.datetime.now()
        add_second = datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        fin_date = now_date + add_second
        fin_date_str = fin_date.strftime("%Y-%m-%d %H:%M:%S")
        self.date_add_job(func, args=args, run_date=fin_date_str, job_id=job_id)

    def remove_job(self, job_id):
        self.__scheduler.remove_job(job_id)

    def print_jobs(self):
        log.info(self.__scheduler.running)
        self.__scheduler.print_jobs()

    def job_listener(self, event):
        if event.exception:
            log.error(f'任务出错了！！！！！！')
        else:
            pass


my_scheduler = MyScheduler()
