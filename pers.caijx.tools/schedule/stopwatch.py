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
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - startTime,2)
        print('lap #%s: %s (%s)' % (lapNum,totalTime,lapTime),end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the CTRL-C exception to keep its error message from displaying.
    print('\nDone.')