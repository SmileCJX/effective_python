#! python3
# timedeltaExample.py - timedelta数据类型
import datetime
delta = datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
print(str(delta.days) + '天' + str(delta.seconds) + '秒' + str(delta.microseconds) + '微秒')
print(str(delta.total_seconds()) + '秒')
print(str(delta))

# 计算当前时间后的1000天的日期
dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)