#! python3
# countdown.py - 倒计时
import time,subprocess
timeLeft = 60
while timeLeft > 0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of countdown,play a sound file.