# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午10:38'

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=opt)

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')

try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO Logo')

browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
