# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午6:31'

import requests
data = {
    'nane': 'ruis',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.status_code)
print(r.text)
print(r.cookies)
print(r.json())
