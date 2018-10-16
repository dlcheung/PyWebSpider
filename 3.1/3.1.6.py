# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午5:06'

# 多参数request请求
from urllib import request, parse

url = 'http://httpbin.org/post'
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT',
    'HSOt': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=header, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
