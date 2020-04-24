import datetime
import time


def datetime_now_to_timestamp(digits=13):
    """
    将当前时间规范成13位时间戳
    :param digits:
    :return:
    """
    time_stamp = datetime.datetime.now().timestamp()
    digits = 10 ** (digits - 10)
    time_stamp = int(round(time_stamp*digits))
    return str(time_stamp)


def date_to_timestamp(date="today", digits=13):
    """
    将今天date规范成13位时间戳
    :param date:
    :param digits
    :return:
    """
    now_datetime = datetime.datetime.now()
    if date == "today":
        pass
    elif date == "tomorrow":
        diff_time = datetime.timedelta(days=1)
        now_datetime = now_datetime + diff_time
    date_time = now_datetime.strftime("%Y-%m-%d 00:00:00")
    date_timestamp = datetime.datetime.strptime(date_time, "%Y-%m-%d 00:00:00").timestamp()
    time_stamp = int(date_timestamp * (10 ** (digits - len(str(int(date_timestamp))))))
    return time_stamp


def date_now_to_str(format_string="%Y%m%d"):
    """
    将当天日期格式化成字符串
    :param format_string:
    :return:
    """
    now_datetime = datetime.datetime.now()
    date_time = now_datetime.strftime(format_string)
    return date_time


def remove_symbol(dt_str):
    """
    删除时间字符串中的符号
    :param dt_str:
    :return:
    """
    return dt_str.replace("-", "").replace(":", "").replace(" ", "")


def datetime_to_timestamp(date, format_string="%Y-%m-%d %H:%M:%S", digits=13):
    """
    将时间字符串转换为10位时间戳，时间字符串默认为2017-10-01 13:37:04格式
    :param date:
    :param format_string:
    :return:
    """
    count = date.count(":")
    if count == 1:
        format_string = "%Y-%m-%d %H:%M"
    time_array = datetime.datetime.strptime(date, format_string)
    time_stamp = int(time_array.timestamp())
    time_stamp = int(time_stamp * (10 ** (13 - len(str(time_stamp)))))
    return time_stamp


# 将时间戳规范为10位时间戳
def timestamp_to_timestamp10(time_stamp):
    time_stamp = int(time_stamp* (10 ** (10-len(str(time_stamp)))))
    return time_stamp


# 将13位时间戳转换为时间字符串，默认为2017-10-01 13:37:04格式
def timestamp_13_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_stamp_10 = timestamp_to_timestamp10(time_stamp)
    time_array = time.localtime(time_stamp_10)
    str_date = time.strftime(format_string, time_array)
    return str_date


if __name__ == '__main__':
    s = date_to_timestamp(date="tomorrow")
    print(timestamp_13_to_date(s))