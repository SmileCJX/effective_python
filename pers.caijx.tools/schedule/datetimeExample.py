#! python3
# datetimeExample.py
import datetime
print(datetime.datetime.now())
dt = datetime.datetime(2018,8,17,16,29,0)
print(str(dt.year) + '年' + str(dt.month) + '月' + str(dt.day) + '日')
print(str(dt.hour) + '时' + str(dt.minute) + '分' + str(dt.second) + '秒')
