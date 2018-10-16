# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午2:17'

import requests
from urllib.parse import quote

import re

lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
    return treat.as_string(response.body)
end
'''

url = 'http://10.10.10.4:8050/execute?lua_source=' + quote(lua)
print(url)
response = requests.get(url, auth=('admin', 'qwe123'))
print(response.text)
ip = re.search('(\d+\.\d+\.\d+\.\d+)', response.text).group(1)
print(ip)