# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午4:04'

import urllib.request
import urllib.error
import socket

# 可以通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过它的抓取

try:
    response = urllib.request.urlopen('http://www.ruisfree.com', timeout=1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

