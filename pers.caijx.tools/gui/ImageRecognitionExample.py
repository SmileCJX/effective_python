#! python3
# ImageRecognitionExample.py - 图像识别
import pyautogui
print(pyautogui.locateOnScreen('.\\test.png'))
# print(list(pyautogui.locateOnScreen('.\\multiTest.png')))  # 如果该图像可以在屏幕中找到多处，则可以得到一个列表
print('中心点：' + str(pyautogui.center((265, 375, 166, 82))))
pyautogui.click((348, 416))