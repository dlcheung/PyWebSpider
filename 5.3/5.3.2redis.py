# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午6:17'

from redis import StrictRedis

redis = StrictRedis(host='10.10.10.5', password='admin')

redis.set('name', 'Ruis')
print(redis.get('name'))
