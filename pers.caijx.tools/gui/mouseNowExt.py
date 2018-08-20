#! python3
# mouseMouseExt.py - 实时得到鼠标的位置，并得到像素
# todo 未能清除原先的坐标
# todo 得到像素点颜色
import pyautogui
print('Press CTRL-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x,y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        print(positionStr,end='')
        print('\b' * len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\nDone.')
