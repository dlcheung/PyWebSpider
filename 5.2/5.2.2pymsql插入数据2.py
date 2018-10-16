# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午5:42'

import pymysql

db = pymysql.connect(host='10.10.10.5', user='root', password='RUIs1996mysql!', db='pyspider')
cursor = db.cursor()

data = {
    'id': '20120002',
    'name': 'Ruis',
    'age': 21
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

try:
    if cursor.execute(sql, tuple(data.values())):
        print('Success')
        db.commit()
except:
    print('Failed')
    db.rollback()

db.close()
