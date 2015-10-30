# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

CONFIGS = {
    # sina site, eg: http://roll.finance.sina.com.cn/finance/cj4/cj_gsxw/index.shtml
    'sina':
        {
            't': re.compile(r'id="artibodyTitle".*?>(.*?)</h1>', re.S),
            'c': re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S)
        },

    # http://finance.ifeng.com/business/
    'ifeng':
        {
            't': re.compile(r'id="artical_topic">(.*?)</h1>', re.S),
            'c': re.compile(r'id="main_content".*?>(.*?)</div>', re.S)
        },

    'nbd':
        {
            't': re.compile(r'<span class="fl">(.*?)</span>', re.S),
            'c': re.compile(r'<div class="main-left-article">(.*?)<div', re.S)
        },

    'eastmoney':
        {
            't': re.compile(r'<h1>(.*?)</h1>', re.S),
            'c': re.compile(r'<div id="ContentBody".*?>(.*?)<div class="BodyEnd">', re.S)
        }
}
