# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午5:31'
import ssl
import http.cookiejar
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context #全局取消ssl证书认证

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')

for item in cookie:
    print(item.name + "=" + item.value)
