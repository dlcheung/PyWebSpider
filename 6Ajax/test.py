# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午8:59'

import requests


res = requests.get("p3.pstatp.com/list/tuchong.fullscreen/19370096_tt")
print(res.text)