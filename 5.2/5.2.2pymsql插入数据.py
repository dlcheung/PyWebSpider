# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午5:42'

import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='10.10.10.5', user='root', password='RUIs1996mysql!', db='pyspider')

cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values (%s, %s, %s)'

try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()

db.close()
