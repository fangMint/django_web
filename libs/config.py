# ==================================
# Author   : fang
# Time     : 2020/4/15 上午11:52
# Email    : zhen.fang@qdreamer.com
# File     : config.py
# Software : PyCharm
# ==================================
import configparser
import logging

logger = logging.getLogger(__name__)

_CF_FILE = "config.ini"
_SECTION = "QBox"


class MyConfig:
    def __init__(self, cf_file=_CF_FILE, section=_SECTION):
        self.cf_file = cf_file
        self.cf = configparser.ConfigParser()
        try:
            self.cf.read(cf_file)
        except FileNotFoundError:
            logger.error("config file path error")
        self.section = section

    def set_config(self, option, value, section=None):
        section = section if section else self.section
        self.cf.set(section, option, value)
        self.cf.write(open(self.cf_file, 'w'))

    def get_config(self, option, section=None):
        section = section if section else self.section
        return self.cf.get(section, option)
