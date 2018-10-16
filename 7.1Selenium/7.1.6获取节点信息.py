# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午10:27'


from selenium import webdriver
from selenium.webdriver import ActionChains
opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=opt)

url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
# 获取属性
print(logo.get_attribute('class'))


# 获取文本值
text = browser.find_element_by_id('zu-top-add-question')
print(text.text)

# 获取id、位置、标签名和大小
# 这里首先获得“提问”按钮这个节点，然后调用其挝、location 、tag_name 、size 属性来获取对应的属性值。
print(text.id)
print(text.location)
print(text.tag_name)
print(text.size)

browser.close()