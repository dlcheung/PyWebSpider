# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午11:17'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()

url = 'https://passport.bilibili.com/register/phone.html#/phone'
wait = WebDriverWait(browser, 5)


# 呼出验证界面
def get_code(phone_num):
    browser.get(url)
    # 填充注册手机号
    phone_area = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="registerForm"]/div[5]/div/input')))
    phone_area.send_keys(phone_num)

    # 点击注册按钮
    reg_but = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="registerForm"]/div[7]/button/span')))
    reg_but.click()


def get_position():
    """
    获取验证码位置
    :return: 验证码位置元组
    """
    img = wait.until(EC.presence_of_element_located((By.XPATH, )))