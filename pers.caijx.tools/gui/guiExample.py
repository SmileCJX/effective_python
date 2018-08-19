#! python3
# guiExample.py - 读取屏幕属性
import pyautogui
print(pyautogui.size())
width,height = pyautogui.size()
print('宽度为：' + str(width))
print('长度为：' + str(height))