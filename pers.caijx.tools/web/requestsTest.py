#! python3
# requestsTest.py - 下载一个网页
import requests
res = requests.get('http://www.baidu.com')
print('类型：' + str(type(res)))
print('长度：' + str(len(res.text)))
print('内容：\n' + res.text)

