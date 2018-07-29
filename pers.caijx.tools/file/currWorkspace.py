# 当前工作目录
import os

print(os.getcwd())
os.chdir('C:\\dev\\IdeaProjects\\effective_python')
print(os.getcwd())

# 处理绝对路径和相对路径
print('------------------------')
print(os.path.abspath('.'))
print(os.path.abspath('.\\scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('c:\\windows','c:\\'))
print(os.path.relpath('c:\\windows','c:\\spam\\eggs'))
