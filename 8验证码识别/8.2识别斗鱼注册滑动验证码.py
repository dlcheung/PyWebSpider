# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午10:24'
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()

url = 'https://passport.douyu.com/member/login'
wait = WebDriverWait(browser, 5)


# 模拟点击

def test_geetest_button():
    """
    获取初始验证按钮, 先点击注册然后等待加载新的页面,再返回but按钮
    :return: 按钮对象
    """
    #  先访问斗鱼首页点击注册
    browser.get(url)
    reg_but = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbox"]/div[1]/div[2]/div[3]/div/a')))
    reg_but.click()
    time.sleep(3)
    phone_num = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginbox"]/div/div[2]/form/div[1]/div/input')))
    phone_num.send_keys('13180200665')
    but = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.geetest_radar_tip')))
    but.click()


try:
    test_geetest_button()
except TimeoutException:
    print("Time Out")
