# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午9:47'

from selenium import webdriver
from selenium.webdriver.common.by import By

# 单个节点 browser.find_element
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_four = browser.find_element(By.ID, 'q')
print(input_first)
print(input_second)
print(input_third)
print(input_four)

# 多节点

lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()