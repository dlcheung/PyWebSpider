# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午10:44'

from selenium import webdriver
opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=opt)

# 隐式等待
browser.implicitly_wait(10)
url = 'https://www.zhihu.com/explore'
browser.get(url)

test = browser.find_element_by_class_name('zu-top-add-question')
print(test)

