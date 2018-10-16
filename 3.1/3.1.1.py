# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午3:27'

import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context #全局取消ssl证书认证
response = urllib.request.urlopen('https://mooc.ruisfree.com')
print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
