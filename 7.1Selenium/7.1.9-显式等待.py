# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午10:54'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
browser = webdriver.Chrome()

browser.get('https://taobao.com')
wait = WebDriverWait(browser, 10)

q_wait = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))

button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(q_wait, button)
# 关于等待条件，其实还有很多， 比如判断标题内容，判断某个节点内是杏出现了某文字等。
