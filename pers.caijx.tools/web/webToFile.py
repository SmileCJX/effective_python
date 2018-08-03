#! python3
# webToFile.py - 将下载的文件保存到硬盘
import requests
res = requests.get('http://www.baidu.com')
res.raise_for_status()
playFile = open('.\\webContent.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()