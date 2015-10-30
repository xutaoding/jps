# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import json
import urlparse
from .. import Download, CONFIGS


class Crawler(Download):
    def __init__(self, url=None):
        self._url = url
        self._document = None

        if self._url:
            self._config = self.select_site()

    def select_site(self):
        configs = CONFIGS.copy()
        suffix = {'com', 'cn', 'net', 'www', 'org'}

        hostname = urlparse.urlparse(self._url).hostname
        host_split = [_host for _host in hostname.split('.') if _host not in suffix]

        for _site, _config in configs.iteritems():
            if _site in host_split:
                return _config
        raise ValueError("DOn't find site config in according to your URL.")

    def title(self):
        try:
            regex = self._config['t']
            tit = regex.findall(self._document)[0]
            return self.section_blank(tit)
        except (AttributeError, TypeError, IndexError) as e:
            print('tit error: {}'.format(e))

    def content(self):
        try:
            regex = self._config['c']
            con = regex.findall(self._document)[0]
            return self.section_blank(self.remove_js_tags(con))
        except (IndexError, TypeError) as e:
            print('con error: {}'.format(e))

    @staticmethod
    def remove_js_tags(text):
        flags = re.S | re.I
        remove_tags_lists = [
            re.compile(r'<!--[if !IE]>.*?<![endif]-->', flags),
            re.compile(r'<!--.*?-->', flags), re.compile(r'<!.*?>', flags),
            re.compile(r'<script.*?>.*?</script>', flags), re.compile(r'<style.*?>.*?</style>', flags),
            re.compile(r'<noscript.*?>.*?</noscript>', flags), re.compile(r"<img.*?>", flags)
        ]

        for re_value in remove_tags_lists:
            text = re_value.sub('', text)
        return re.compile(r'<.*?>', re.S).sub('', text)

    @staticmethod
    def section_blank(text):
        patterns = {
            'blank': re.compile(r'\s+', re.S),
            'chz': re.compile(r'\u3000+', re.S)
        }

        def wrapper(k):
            def repl(regex):
                if k == 'blank':
                    return ' '
                elif k == 'chz':
                    return ''
            return repl

        for key, pattern in patterns.iteritems():
            text = pattern.sub(wrapper(key), text)
        return text

    def parse(self):
        if not self._url:
            message = {'url': self._url, 'error': 'URL empty', 't': None, 'c': None}
            return json.dumps(message)

        self._document = unicode(self.get_html(self._url), 'u8')
        tit = self.title()
        con = self.content()
        return json.dumps({'t': tit, 'c': con})
