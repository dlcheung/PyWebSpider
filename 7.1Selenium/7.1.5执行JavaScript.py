# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午10:23'

# 对于某些操作， Selenium API 并没有提供。比如，下拉进度条，它可以直接模拟运行JavaScript
# 此时使用execute_script()方法即可实现，代码如下：

from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.zhihu.com/explore')
browser.execute_script('alert("test")')
