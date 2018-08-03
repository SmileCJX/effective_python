#! python3
# beautifulSoup4Demo.py - 从HTML创建一个BeautifulSoup对象
import requests,bs4
res = requests.get('http://www.baidu.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,features='html.parser')
print('类型：' + str(type(noStarchSoup)))

print('--------------------------------')
exampleFile = open('.\\example.html')
exampleFile = bs4.BeautifulSoup(exampleFile,features='html.parser')
print('类型：' + str(type(exampleFile)))