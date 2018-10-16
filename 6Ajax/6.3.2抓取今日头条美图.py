# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/15 下午8:11'

import os
from hashlib import md5
import requests
from urllib.parse import urlencode
# 利用了多线程的线程池，调用其map （）方法实现多线程下载。
from multiprocessing.pool import Pool


# 伪造请求爬取页面参数
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


# 获取图片参数
def get_images(json_data):
    if json_data.get('data'):
        for item in json_data.get('data'):
            title = item.get('title')
            if title is None:  # 判断当前是否有title
                continue
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': image.get('url').strip("//"),
                    'title': title
                }


# 保存图片
def save_image(item):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        url = "http://" + item.get('image')
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Faild to Save Image')


def main(offset):
    json_data = get_page(offset)
    for item in get_images(json_data):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
