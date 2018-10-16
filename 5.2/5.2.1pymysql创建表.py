# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午5:32'

import pymysql

db = pymysql.connect(host='10.10.10.5', user='root', password='RUIs1996mysql!', db='pyspider')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL ,name VARCHAR (255) NOT NULL ,age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)

db.close()
