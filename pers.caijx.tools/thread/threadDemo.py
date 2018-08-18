#! python3
# threadDemo.py - 多线程
import threading,time
print('Start of progrqm.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program!')