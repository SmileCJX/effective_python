#! python3
# stopwatch.py - 设置程序来记录时间
import time

# Display the program's instructions
print('Press ENTER to begin. Afterwards,press ENTER to "click" the stopwatch.Press CTRL-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
