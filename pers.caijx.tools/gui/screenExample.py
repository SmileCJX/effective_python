#! python3
# screenExample.py - 获取屏幕快照
import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((0,0)))
print(im.getpixel((50,200)))
# 分析屏幕快照
print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))
print(pyautogui.pixelMatchesColor(50, 200, (60, 63, 65)))