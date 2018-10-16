# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 上午11:59'

from lxml import html

etree = html.etree

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result)
print(result.decode('utf-8'))
