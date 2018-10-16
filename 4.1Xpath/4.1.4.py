# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午12:25'


from lxml.html import etree

text = '''
<li class="li li-first"><a href="link.html">firse itrm</a></li>
'''


html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
