#! python3
# 从ZIP文件中解压缩
import zipfile,os
exampleZip = zipfile.ZipFile('.\\desktop.zip')
# 解压全部文件
exampleZip.extractall()
# 只解压CDA.txt文件
exampleZip.extract('CDA.txt')
# 解压文件放置到move文件夹中
exampleZip.extract('CDA.txt','.\\move')
exampleZip.close()