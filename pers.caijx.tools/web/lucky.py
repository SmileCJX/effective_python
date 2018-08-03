#! python3
# lucky.py - 打开百度搜索结果
import requests,sys,webbrowser,bs4
print('Baidu ing ...') # display text while downloading the baidu page
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrive top search result links.

# Open a browser tab for each result.