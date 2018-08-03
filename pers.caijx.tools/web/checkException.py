#! python3
# checkException.py - 检查错误
import requests
res = requests.get('http://www.baidu.com')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))