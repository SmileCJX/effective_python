# 用shelve模块保存变量
import shelve
shelfFile = shelve.open('.\\mydata')
cats = ['Zophies','Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('.\\mydata')
print(type(shelfFile))
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))