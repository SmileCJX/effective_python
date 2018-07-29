# 用pprint.pformat()函数保存变量
import os,pprint

cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
pprint.pformat(cats)

fileObj = open('.\\myCats.py','w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
