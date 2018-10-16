# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午3:57'
import urllib.request
import urllib.parse  # 格式化字典数据用于post  data属性用于存放post数据

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')

response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
