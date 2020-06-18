# ==================================
# Author   : fang
# Time     : 2020/5/30 16:18
# Email    : zhen.fang@qdreamer.com
# File     : datetime_fun.py
# Software : PyCharm
# ==================================
import datetime
import time


def timestamp_length(timestamp, length=13):
    time_stamp = int(timestamp) * (10 ** (length-len(str(int(timestamp)))))
    return time_stamp


def string_2_datetime(string: str, format_str="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strptime(string, format_str)


def string_2_time_tuple(string: str, format_str="%Y-%m-%d %H:%M:%S"):
    return time.strptime(string, format_str)


def string_2_timestamp(string: str, format_str="%Y-%m-%d %H:%M:%S"):
    time_tuple = string_2_time_tuple(string, format_str)
    timestamp = time.mktime(time_tuple)
    # 方法2
    # dt = string_2_datetime(string, format_str)
    # timestamp = dt.timestamp()
    return timestamp_length(timestamp, 13)


def datetime_2_string(dt: datetime):
    return dt.strftime()


def datetime_2_timestamp(dt: datetime):
    timestamp = dt.timestamp()
    return timestamp_length(timestamp, 13)


def datetime_2_time_tuple(dt: datetime):
    return dt.timetuple()


def __timestamp_2_time_tuple(timestamp):
    return time.localtime(timestamp)  # 只接受十位，不然解析出错


def timestamp_2_string(timestamp, format_str="%Y-%m-%d %H:%M:%S"):
    timestamp = timestamp_length(timestamp, 10)
    time_tuple = __timestamp_2_time_tuple(timestamp)
    return time.strftime(format_str, time_tuple)


def timestamp_2_datetime(timestamp):
    if isinstance(timestamp, (str, int)):
        timestamp = float(timestamp)
    timestamp = timestamp_length(timestamp, 10)
    return datetime.datetime.fromtimestamp(timestamp)


def string_2_date(string: str, format_str="%Y-%m-%d"):  # 或者datetime -> date
    dt = string_2_datetime(string, format_str)
    return datetime.datetime.date(dt)


def now_2_timestamp(length=13):
    timestamp = datetime.datetime.now().timestamp()
    return timestamp_length(timestamp, length)


if __name__ == '__main__':
    t = "2020-06-04 23:04"
    s1 = string_2_datetime(t, format_str="%Y-%m-%d %H:%M")
    print(s1)
    print(datetime.datetime.date(s1))
    s2 = string_2_timestamp(t, format_str="%Y-%m-%d %H:%M")
    print(s2)
    s4 = timestamp_2_string(s2)
    print(s4)
    s5 = timestamp_2_datetime(s2)
    print(s5)
    print(now_2_timestamp())
