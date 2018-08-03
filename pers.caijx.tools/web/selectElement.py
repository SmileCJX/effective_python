#! python3
# selectElement.py - 用select()方法寻找元素
import bs4
exampleFile = open('.\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),features='html.parser')
elems = exampleSoup.select('#author')
print('类型：' + str(type(elems)))
print('长度：' + str(len(elems)))
print('类型：' + str(type(elems[0])))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print('长度：' + str(len(pElems)))
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[0].getText())
print(str(pElems[2]))
print(pElems[2].getText())

spamElem = exampleSoup.select('span')[0]
print(str(spamElem))
print(spamElem.get('id'))
print(spamElem.get('some_exists') == None)
print(spamElem.attrs)