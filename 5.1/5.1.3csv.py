# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午5:27'

import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', '睿', 22])


with open('data.csv', 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    for row in reader:
        print(row)