#! python3
# scrollExample.py - 复制数字，并滚动滚轮
import pyperclip,pyautogui,time
numbers = ''
for i in range(200):
    numbers = numbers + str(i) + '\n'

pyperclip.copy(numbers)
time.sleep(5)
pyautogui.scroll(100)