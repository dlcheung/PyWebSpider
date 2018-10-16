# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 上午11:28'
from lxml.html import etree  # 最新版本的etree换地方了

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
