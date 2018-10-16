# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午5:59'

from urllib.parse import urlencode, quote

params = {
    'name': 'ruis',
    'age': 22
}

keywords = '大白菜'
# quote用于将中文转换为URL编码

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params) + quote(keywords)
print(url)

# unquote可以还原