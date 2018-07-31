#! python3
# 读取ZIP文件
import zipfile,os
exampleZip = zipfile.ZipFile('.\\desktop.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('CDA.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size,2)))
exampleZip.close()