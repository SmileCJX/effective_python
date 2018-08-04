#! python3
# seleniumTest.py - 用selenium模块控制浏览器

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
print(str(type(browser)))
browser.get('http://www.zhibo8.com')

# 找到带有container类名的标签名
try:
    elem = browser.find_element_by_class_name('container')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# 点击页面
linkElem = browser.find_element_by_link_text('NBA视频')
print(str(type(linkElem)))
linkElem.click()

# 填写并提交表单
# browser.get('https://sso.toutiao.com')
# phone = browser.find_element_by_id('mobile')
# phone.send_keys('17210851234')
# captcha1 = browser.find_element_by_id('captcha1')
# captcha1.send_keys('1234')
# code = browser.find_element_by_id('code')
# code.send_keys('4567')
# code.submit()

# 发送特殊键
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scrolls to bottom
htmlElem.send_keys(Keys.HOME) # scrolls to top