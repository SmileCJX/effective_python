#! python3
# countdown.py - 倒计时
import time,subprocess
timeLeft = 20
while timeLeft > 0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of countdown,play a sound file.
subprocess.Popen(['start','末日不孤单.mp3'],shell=True)