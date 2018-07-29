# 检查路径有效性
import os

print(os.path.exists('c:\\windows'))
print(os.path.exists('c:\\some_made_up_folder'))
print(os.path.isdir('c:\\windows\\system32'))
print(os.path.isfile('c:\\windows\\system32'))
print(os.path.isdir('c:\\windows\system32\\calc.exe'))