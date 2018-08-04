#! python3
# seleniumTest.py - 用selenium模块控制浏览器

from selenium import webdriver
browser = webdriver.Chrome()
print(str(type(browser)))
browser.get('http://www.zhibo8.com')

# 找到带有container类名的标签名
try:
    elem = browser.find_element_by_class_name('container')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')