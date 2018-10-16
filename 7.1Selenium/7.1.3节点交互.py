# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午9:57'

# 节点交互

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://taobao.com')
input_addr = browser.find_element_by_id('q')
input_addr.send_keys('iPhone')
time.sleep(2)
input_addr.clear()  # 清空输入
time.sleep(2)
input_addr.send_keys('iPad')
button = browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
button.click()
browser.close()