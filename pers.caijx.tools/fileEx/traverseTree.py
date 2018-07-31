#! python3
# 遍历目录树
import os
for folderName,subfolders,filenames in os.walk('.\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLER OF ' + folderName + ':' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ':' + filename)
    print('')