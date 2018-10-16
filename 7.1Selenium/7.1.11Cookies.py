# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午11:11'

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'ruis', 'domain': 'wwww.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

# 首先，我们访问了知乎。加载完成后，浏览器实际上已经生成Cookies 了。接着，调用get_cookies()
# 方法获取所有的Cookies 。然后，我们添加一个Cookie ，这里传入一个字典，有name 、domain 和value
# 等内容。接下来，再次获取所有的Cookies 。可以发现，结果就多了这一项新加的Cookie 。最后，调
# 用delete_all_cookies （）方法删除所有的Cookies 。再重新获取，发现结果就为空了。