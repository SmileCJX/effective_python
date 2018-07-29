# 文件路径的字符串
import os

print(os.path.join('usr','bin','spam'))

myFiles = ['account.txt','details.csv','invite.docx']
for filename in myFiles:
    print(os.path.join('c:\\users\\asweigart'),filename)

