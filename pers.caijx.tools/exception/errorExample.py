#! python3
# errorExample.py - 取得反向跟踪的字符串
def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()