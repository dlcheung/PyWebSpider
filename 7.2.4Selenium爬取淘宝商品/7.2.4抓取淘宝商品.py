# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午2:31'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

from pyquery import PyQuery as pq
import pymongo

# 无界面模式

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input_area = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="J_BottomSearchForm"]/button'))
            )
            input_area.clear()
            input_area.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )
        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )
        get_products()
    except TimeoutException:
        index_page(page)


# 定义解析商品函数
def get_products():
    """
    抓取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#m-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/strong').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('//*[@id="J_Itemlist_TLink_566940629944"]').text(),
            'shop': item.find(
                '//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]/div[2]/div[3]/div[1]/a/span[2]').text(),
            'location': item.find('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]/div[2]/div[3]/div[2]').text()
        }
        print(product)
        save_to_mongo(product)


MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(result):
    """
    保存到 MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB 成功')
    except Exception:
        print('存储到MongoDB失败')


MAX_PAGE = 100


def main():
    """
    遍历每一项
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)

    browser.close()