# -*- coding: utf-8 -*-

import pycurl
from django.test import TestCase
import requests
import json


def test_crawl():
    url = 'http://127.0.0.1:8000/api/crawl/url/'
    data = {
        # 'url': 'http://finance.sina.com.cn/trust/20151030/104123630527.shtml'
        'url': 'http://finance.eastmoney.com/news/1374,20151030560716685.html'
    }

    # r = requests.get(url)
    # print r.content
    r = requests.post(url, data)
    # print r.content
    data = json.loads(r.content)
    print 'test:', data['t']
    print 'c:', data['c']


if __name__ == '__main__':
    test_crawl()

