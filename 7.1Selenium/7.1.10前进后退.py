# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午11:07'

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.get('https://taobao.com')
browser.get('http://jd.com')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

# #这里我们连续访问3 个页面，然后调用back （）方法回到第二个页面，接下来再调用forward （）方
# 法又可以前进到第三个页面。
