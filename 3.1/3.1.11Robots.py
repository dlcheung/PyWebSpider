# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午6:16'
import ssl
from urllib.robotparser import RobotFileParser

ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消ssl证书认证
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=l&type=collections'))
