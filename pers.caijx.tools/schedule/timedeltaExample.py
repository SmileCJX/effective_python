#! python3
# timedeltaExample.py - timedelta数据类型
import datetime,time
delta = datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
print(str(delta.days) + '天' + str(delta.seconds) + '秒' + str(delta.microseconds) + '微秒')
print(str(delta.total_seconds()) + '秒')
print(str(delta))

# 计算当前时间后的1000天的日期
dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

# 计算30年前的某一天以及60年前的某一天
oct21st = datetime.datetime(2015,10,21,16,29,0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(aboutThirtyYears)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))

# 暂停直至特定日期
aug2018 = datetime.datetime(2018,8,17,13,50,0)
while datetime.datetime.now() < aug2018:
    time.sleep(1)