# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午4:52'

import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context #全局取消ssl证书认证

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

