#! python3
# screenExample.py - 获取屏幕快照
import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((0,0)))
print(im.getpixel((50,200)))
