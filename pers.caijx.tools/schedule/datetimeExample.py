#! python3
# datetimeExample.py
import datetime,time
print(datetime.datetime.now())
dt = datetime.datetime(2018,8,17,16,29,0)
print(str(dt.year) + '年' + str(dt.month) + '月' + str(dt.day) + '日')
print(str(dt.hour) + '时' + str(dt.minute) + '分' + str(dt.second) + '秒')

print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

# 比较时间
halloween2015 = datetime.datetime(2015,10,31,0,0,0)
newYear2018 = datetime.datetime(2018,8,17,13,18,0)
oct31_2015 = datetime.datetime(2015,10,31,0,0,0)
print(halloween2015 == oct31_2015)
print(halloween2015 > newYear2018)
print(newYear2018 > halloween2015)
print(newYear2018 != oct31_2015)