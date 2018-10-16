# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午1:29'

import requests

url = 'http://10.10.10.5:8050/render.html?url=https://www.baidu.com&wait=1'

response = requests.get(url)

print(response.text)