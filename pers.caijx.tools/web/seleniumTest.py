#! python3
# seleniumTest.py - 用selenium模块控制浏览器

from selenium import webdriver
browser = webdriver.Chrome()
print(str(type(browser)))
browser.get('http://www.baidu.com')