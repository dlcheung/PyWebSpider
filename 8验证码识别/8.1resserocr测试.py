# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午9:33'

import pytesseract

from PIL import Image

image = Image.open('code.jpeg')

image = image.convert('L')  # 转化为灰度对象
image.show()

result = pytesseract.image_to_string(image)

print(result)
