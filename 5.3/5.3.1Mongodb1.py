# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午5:59'

import pymongo

client = pymongo.MongoClient(host='10.10.10.5', port=27017)

# 或以字符串形式连接
# client = pymongo.MongoClient('mongodb://10.10.10.5:27017')


db = client.pyspider

# 等价
# db = client['pyspider']

collection = db.students

student1 = {
    'id': '20170103',
    'name': 'Ruis',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170104',
    'name': '汤',
    'age': 29,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result)

print(result.inserted_ids)

result = collection.find({'name': 'Ruis'})
print(type(result))
print(result)
for i in result:
    print(i)
