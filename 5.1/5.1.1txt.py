# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午4:54'

import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}

html = requests.get(url, headers=headers).text

doc = pq(html)

items = doc('.explore-tab .feed-items').items()  # 调用items()方法后,会得到一个生成器,遍历一下,就可以逐个得到节点对象

for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()

with open('explore.txt', 'a', encoding='utf-8') as f:
    f.write('\n'.join([question, author, answer]))
    f.write('\n' + '=' * 50 + '\n')
