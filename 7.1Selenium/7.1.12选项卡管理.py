# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午11:15'

# 在访问网页的时候，会开启一个个选项卡。在Selenium 中，我们也可以对选项卡进行操作

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])  # 使用新方法替换旧方法  use driver.switch_to.window 替换switch_to_window
browser.get('https://taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://ruisfree.com')

# 首先访问了百度，然后调用了execute_script方法，这里传入window.open()这个JavaScript 语
# 句新开启一个选项卡。接下来，我们想切换到该选项卡。这里调用window handles 属性获取当前开启
# 的所有选项卡，返回的是选项卡的代号列表。要想切换选项卡，只需要调用switch_to.window() 方法
# 即可，其中参数是选项卡的代号。这里我们将第二个选项卡代号传人，即跳转到第二个选项卡，接下
# 来在第二个选项卡下打开一个新页面，然后切换回第一个选项卡重新调用switch_window()方法，
