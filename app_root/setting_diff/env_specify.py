# ==================================
# Author   : fang
# Time     : 2020/4/24 上午11:24
# Email    : zhen.fang@qdreamer.com
# File     : env_specify.py
# Software : PyCharm
# ==================================
import socket
import os

# 指定环境，dev, test, prod可选。生产环境一定要去除！！！
SPECIAL_ENV = "test"

# 开发环境机器
DEVELOPER = [
    'DESKTOP-6LSP19F',   # 自己笔记本
    'fang-DJ-C-H310M-E-D3',   # 公司电脑
    'feng',  # 同事
]

# 测试环境机器
TESTER = [
    'iZbp16e9fiu6p7q4rjobgjZ',  # 公司阿里云机器121.40.97.71
]

# 本地调制时用，可以区分是热加载服务还是真实服务，其它环境无效！！！
is_key_process = os.environ.get('RUN_MAIN') == 'true'

# 获取主机名
hostname = socket.gethostname()
# 分辨环境
if set(DEVELOPER).intersection(set(TESTER)):
    raise ValueError("developer与tester配置机器冲突")

is_development = True if hostname in DEVELOPER else False
is_test = True if hostname in TESTER else False
is_production = False if is_test or is_development else True

get_env = SPECIAL_ENV if SPECIAL_ENV else "dev" if is_development else "test" if is_test else "prod"


print(f"Django environment is ({get_env})")
