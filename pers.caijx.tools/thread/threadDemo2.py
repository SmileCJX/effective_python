#! python3
# threadDemo2.py - 向线程的目标函数传递参数
import threading
threadObj = threading.Thread(target=print,args=['Cats','Dogs','Frogs'],kwargs={'sep':' & '})
# 不正确的做法
# threadObj = threading.Thread(target=print('Cats','Dogs','Frogs',sep=' & '))
threadObj.start()