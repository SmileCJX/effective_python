# 1、用open()函数打开文件 2、读取文件内容  3、写入文件
import os

helloFile = open('.\\hello.txt')
hellContent = helloFile.read()
print(hellContent)

sonnetFile = open('.\\sonnet29.txt')
print(sonnetFile.readline())

baconFile = open('.\\bacon.txt','w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('.\\bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('.\\bacon.txt')
content = baconFile.read()
print(content)