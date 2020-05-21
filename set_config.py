# ==================================
# Author   : fang
# Time     : 2020/5/20 20:28
# Email    : zhen.fang@qdreamer.com
# File     : set_config.py
# Software : PyCharm
# ==================================
from libs import config
from libs.tool_fun import get_host_ip

my_config = config.MyConfig()

host = get_host_ip()
my_config.set_config("host", host)

print(f"host设置完成, {host}")