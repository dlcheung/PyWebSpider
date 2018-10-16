# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午7:13'

from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
import requests
import json

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'HOST': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2947937725',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '5640205295',
        'containerid': '1076035640205295',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json_data):
    if json_data:
        items = json_data.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


if __name__ == '__main__':
    client = MongoClient(host='10.10.10.5', port=27017)
    db = client['weibo']
    collection = db['weibo']


    def save_to_mongo(result):
        if collection.insert_one(result):
            print('Save to mongo')


    all_data = []
    for page in range(2, 11):
        json_data = get_page(page)
        results = parse_page(json_data)
        for result in results:
            print(result)
            save_to_mongo(result)
            all_data.append(result)

    with open('data.json', 'w') as jf:
        jf.write(json.dumps(all_data, indent=2, ensure_ascii=False))
