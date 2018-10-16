# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/13 下午5:43'
import ssl
import http.cookiejar
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# LWPCookieJar 同样可以读取和保存Cookies ，但是保存的格式和MozillaCookieJar 不一样，
# 它会保存成libwww-perl(LWP）格式的Cookies 文件。
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)