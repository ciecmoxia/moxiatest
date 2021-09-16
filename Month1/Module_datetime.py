
#datetime_date
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