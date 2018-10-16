# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午5:16'

import json

str = """
[{
    "name": "大白菜",
    "gender": "male",
    "birthday": "1992-19-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
"""

print(type(str))
data = json.loads(str)
print(data)
print(type(data))

print(data[0]['name'])
print(data[0].get('name'))

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))    # indent缩进 更清晰 ensure_ascii=False输出中文
