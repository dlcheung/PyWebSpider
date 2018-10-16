# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午11:42'

from io import BytesIO
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
from PIL import Image
import pytesseract

browser = webdriver.Chrome()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
url = 'https://passport.bilibili.com/register/phone.html#/phone'
wait = WebDriverWait(browser, 5)
url = 'https://www.zuhaowan.com/login/register.html'
browser.get(url)


# 处理验证码
def fix_code():
    img = Image.open('code.png')
    img = img.convert('L')
    img.show()
    res = pytesseract.image_to_string(img)
    time.sleep(2)
    print(res)
    return res


# https://www.zuhaowan.com/login/register.html
def zuhaowan_com(phone_num):
    # 填充注册手机号
    phone_area = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="registername"]')))
    phone_area.send_keys(phone_num)

    # 填充验证码
    code = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="verify_code"]')))
    code.send_keys(fix_code())
    # 点击注册按钮
    reg_but = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="verify-code"]')))
    reg_but.click()


def get_postion():
    img = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="verify_img"]')))
    location = img.location
    print(location)
    size = img.size
    print(size)
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    return (left, top, right, bottom)


def get_code_img(name='code.png'):
    """
        保存验证码
    :param name: 图片对象
    :return:
    """
    left, top, right, bottom = get_postion()
    print(get_postion())
    browser.get_screenshot_as_file('code.png')
    screenhot = Image.open('code.png')
    # 由于高分屏将位置放大2倍
    captcha = screenhot.crop((left * 2, top * 2, right * 2, bottom * 2))
    captcha.save(name)


get_code_img()
zuhaowan_com(18618340685)
