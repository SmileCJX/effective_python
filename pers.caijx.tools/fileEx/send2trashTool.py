#! python3
# 用send2trash模块进行安全的删除
import send2trash
baconFile = open('.\\bacon.txt','a') # creates the file
baconFile.write('Bacon is not a begetable.')
baconFile.close()
send2trash.send2trash('.\\bacon.txt')