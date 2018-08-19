#! python3
# mouseMouse.py - 实时得到鼠标的位置
# todo 未能清除原先的坐标
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
