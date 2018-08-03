#! python3
# lucky.py - 打开百度搜索结果的前5条
import requests,sys,webbrowser,bs4
print('Baidu ing ...') # display text while downloading the baidu page
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrive top search result links.
soup = bs4.BeautifulSoup(res.text,features='html.parser')

# Open a browser tab for each result.r
linkElems = soup.select('.result.c-container > h3 > a')
print(str(len(linkElems)))
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))