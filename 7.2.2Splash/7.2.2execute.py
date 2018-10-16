# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午1:32'

import requests

from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end
'''
print(quote(lua))
url = 'http://10.10.10.5:8050/execute?lua_source=' + quote(lua)

response = requests.get(url)
print(response.text)

lua2 = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
        return {
            html = treat.as_string(response.body),
            url = response.url,
            status=response.status
        }
end
'''

url2 = 'http://10.10.10.5:8050/execute?lua_source=' + quote(lua2)
print(url2)
response2 = requests.get(url2)

print(response2.text)