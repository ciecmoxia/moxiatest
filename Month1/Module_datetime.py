#datetime_date
'''
# https://blog.csdn.net/cmzsteven/article/details/64906245
from datetime import date
# #import datetime as dt
# d=dt.date(2021,9,16)
# print(d,type(d))
# # 构建一个日期对象，包含有 year, month, day 三个属性。
# # 构建一个日期对象
# # year 区间[1, 9999], month 区间[1, 12], day 区间[1, (28,29,30,31)]
# d = dt.date(year=2018, month=6, day=15)
# print(d, type(d))
#
# # 获取当前系统的日期
# today =d.today();
# print("当前系统日期为：", today)

# 构建一个日期对象
# year 区间[1, 9999], month 区间[1, 12], day 区间[1, (28,29,30,31)]
d = date(2018, 6, 12)
print(d, type(d))
d = date(year=2018, month=6, day=15)
print(d, type(d))
# 获取当前系统的日期
today = date.today();
print("当前系统日期为：", today)
# 时间戳转化成日期
timestamp = 5555555555
d = date.fromtimestamp(timestamp)
print(d)
# 获取日期的星期几
today = date.today()
print("今天是星期", today.weekday() + 1)
print(today.weekday(), today.isoweekday())
print("今天是星期", today.isoweekday())

# 格式化日期
today = date.today()
ds = today.isoformat()
print(ds, type(ds))#<class 'str'>
ds = today.strftime("%Y-%m-%d")
print(ds, type(ds))#<class 'str'>
ds = today.strftime("%Y/%m/%d")
print(ds, type(ds))#<class 'str'>

# 返回日期构成的元素元组
time_tuple = date.today().timetuple()
print(time_tuple)
# time.struct_time(tm_year=2018, tm_mon=6, tm_mday=13, tm_hour=0, tm_min=0,
# tm_sec=0, tm_wday=2, tm_yday=164, tm_isdst=-1)

# 替换
print("当前时间为：", date.today())
print("替换后的时间为：", date.today().replace(2012, 8, 8))
'''


'''
isoformat()使用标准化的格式：%Y-%m-%d，返回是一个字符串
strftime(format)函数，使用 format 的格式，返回是一个字符串
Format 格式：
 %y 两位数的年份表示（00-99）  %Y 四位数的年份表示（000-9999）  %m 月份（01-12）  %d 月内中的一天（0-31）  %H 24 小时制小时数（0-23）  %I 12 小时制小时数（01-12）  %M 分钟数（00=59）  %S 秒（00-59）  %a 本地简化星期名称
 %A 本地完整星期名称
 %b 本地简化的月份名称
 %B 本地完整的月份名称
 %c 本地相应的日期表示和时间表示
 %j 年内的一天（001-366）  %p 本地 A.M.或 P.M.的等价符
 %U 一年中的星期数（00-53）星期天为星期的开始
 %w 星期（0-6），星期天为星期的开始
 %W 一年中的星期数（00-53）星期一为星期的开始
 %x 本地相应的日期表示
 %X 本地相应的时间表示
 %Z 当前时区的名称
 %% %号本身
'''
'''
#datetime_time
from datetime import time
# 构建一个时间对象，包含有 hour, minute, second, microsecond 和 tzinfo 五个属性
t = time(10, 30, 59, 1000)
print(t,type(t))
# 替换
t = time(10, 30, 59)
t = t.replace(12, 23, 36)
print(t)
# 时间对象转化成时间字符串
t = time(hour=12, minute=34, second=56,
microsecond=123456).strftime("%H:%M:%S")
print(t)
t = time(hour=12, minute=34, second=56,
microsecond=123456).strftime("%H-%M")
print(t)
# 标准格式化
t = time(hour=12, minute=34, second=56,
microsecond=123456).isoformat(timespec='hours')
print(t)
t = time(12, 34, 56, 123456).isoformat(timespec='minutes')
print(t)
t = time(12, 34, 56, 123456).isoformat(timespec='seconds')
print(t)
t = time(12, 34, 56, 123456).isoformat(timespec='milliseconds')
print(t)
t = time(12, 34, 56, 123456).isoformat(timespec='microseconds')
print(t)
t = time(12, 34, 56, 123456).isoformat(timespec='auto')
print(t)
'''
'''
返回值类型是字符串
 'auto': 如果微秒为 0 就不会显示
 'hours': 显示小时.  'minutes': 显示小时分钟 HH:MM.
 'seconds': 显示时分秒 HH:MM:SS.
 'milliseconds':显示时分秒毫秒. HH:MM:SS.sss.
 'microseconds': 显示时分秒微秒 HH:MM:SS.mmmmmm.
'''
'''
#datetime_datetime
from datetime import datetime
# 构 建 一 个 日 期 时 间 对 象 ， 包 含 有 year, month, day, hour, minute, second,microsecond 和 tzinfo 八个属性
d = datetime(2018, 8, 8, 18, 50, 23)
print(d)
# 获取当前日期
now = datetime.today()
print(now)
now = datetime.now()
print(now)
# 获取当前标准时区时间
print(datetime.utcnow())
# 日期时间转时间戳
d = datetime(2018, 8, 8, 18, 50, 23)
print(d.timestamp())
# 时间戳转日期时间
timestamp = 1533725423.0
print(datetime.fromtimestamp(timestamp))
# 日期时间结合
from datetime import date, time
d = datetime.combine(date.today(), time(23, 59, 34))
print(d)
# 日期时间格式化
ds = datetime.today().strftime("%Y-%m-%d")
print(ds)
ds = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
print(ds)
ds = datetime.today().strftime("%Y-%m-%d %I:%M:%S")
print(ds)
# 日期时间字符串转日期时间格式
d = datetime.strptime("2018-04-07 08:43:07 AM", "%Y-%m-%d %I:%M:%S %p")
print(d, type(d))
d = datetime.strptime("2018-04-07 08:43:07 PM", "%Y-%m-%d %I:%M:%S %p")
print(d, type(d))
# 日期时间获取日期和时间
print(datetime.today().date())
print(datetime.today().time())
# 替换
print(datetime.today())
print(datetime.today().replace(2017, 3, 6, 18, 50, 23))
'''

import datetime
# 两个日期相差多少天
dt1 = datetime.datetime.strptime("2017-01-05 00:46:05", "%Y-%m-%d %H:%M:%S")
dt2 = datetime.datetime.strptime("2018-02-05 14:46:05", "%Y-%m-%d %H:%M:%S")
delta = dt2 - dt1
print(type(delta), delta)
print("两日期相差%d 天，%d 小时"%(delta.days, delta.seconds/(60 * 60))) #delta.seconds 相差秒数
print("两日期总共相差%d 秒" % (delta.total_seconds()))
# <class 'datetime.timedelta'> 396 days, 14:00:00
# 两日期相差 396 天，14 小时
# 两日期总共相差 34264800 秒

# 今天的 n 天后的日期
now = datetime.datetime.now()
print(now)
delta = datetime.timedelta(days=10)
n_datetime = now + delta
print(n_datetime)
# 日期时间（日期）比较大小
dt1 = datetime.datetime(2017, 8, 5, 17, 49)
dt2 = datetime.datetime(2018, 3, 2, 8, 1)
print(dt1 < dt2)

#时区
# 是 tzinfo 的具体实现，timezone(offset, name=None)其中 offset 偏移参数必须指定
# 为表示本地时间和 UTC 之间差异的时间增量对象。(-24, 24)开区间，否则就会产生
# ValueError。
from datetime import datetime, timezone, timedelta
# 计算标准时区（UTC）和东八区时间（UTC +8）
dt = datetime.utcnow()
print(dt)
# 设置 utc 标准时间时区
dt = dt.replace(tzinfo=timezone.utc)
print(dt)
tzutc_8 = timezone(timedelta(hours=8))
local_dt = dt.astimezone(tzutc_8) # 设置了时区的时间
print(local_dt)
print(local_dt.tzinfo) # 查看时区相差几个小时


#time 模块
# -*- coding:utf-8 -*-
import time
# 当前时间的时间戳
print(time.time())
# 获取时间元组
t = time.localtime(1528900481.1909196)
print(t)
# 接收时间元组返回时间戳
t = time.localtime(1528900481.1909196)
print(time.mktime(t))
# 获取标准时区（UTC）世界时
print(time.gmtime(1528900481.1909196))
# 接收时间元组，并返回以可读字符串表示的当地时间，格式由 fmt 决定
ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1528900481.1909196))
print(ts)
# 根据 fmt 的格式把一个时间字符串解析为时间元组
tp = time.strptime("2018-06-13 22:34:41", "%Y-%m-%d %H:%M:%S")
print(tp, type(tp))
print("*"*30) # 当前线程沉睡多少秒
tp = time.strptime("2018-06-13 22:34:41", "%Y-%m-%d %H:%M:%S")
time.sleep(1)
print(tp)
# 用以浮点数计算的秒数返回当前的 CPU 时间。用来衡量不同程序的耗时，比 time.time()更精确
# def test():
# 	time.sleep(5)
# if __name__ == '__main__':
# 	t1 = time.clock()
# 	test()
# 	t2 = time.clock()
# 	print("程序执行时间：", (t2 - t1))

#Calendar 模块
import calendar
# 获取日历的开始星期(默认星期一开始)，以及设置开始星期
print("开始星期：", calendar.firstweekday(), "星期一")
calendar.setfirstweekday(1)
print("修改后开始星期：", calendar.firstweekday(), "星期二")
# 打印某月份的日历
print(calendar.month(2018, 6))
print(calendar.monthcalendar(2018, 6))
# 判断是否是闰年
print(calendar.isleap(2016))
print(calendar.isleap(2018))