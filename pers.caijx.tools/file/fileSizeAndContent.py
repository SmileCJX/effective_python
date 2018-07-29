# 查看文件大小和文件内容

import os

print(os.path.getsize('c:\\windows\\system32\\calc.exe'))
print(os.listdir('c:\\windows\\system32'))

totalSize = 0
for filename in os.listdir('c:\\windows\\system32'):
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\windows\\system32',filename))

print(totalSize)