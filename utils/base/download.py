# -*- coding: utf-8 -*-

import re
import pycurl
import chardet
import StringIO


def remove_script_style(func):
    flags = re.S | re.I
    remove_tags_lists = [
        re.compile(r'<script.*?>.*?</script>', flags),
        re.compile(r'<style.*?>.*?</style>', flags),
        re.compile(r'<noscript.*?>.*?</noscript>', flags)
    ]

    def html_parse_wrapper(*args, **kwargs):
        _html = func(*args, **kwargs)
        for re_value in remove_tags_lists:
            _html = re_value.sub('', _html)
        return _html
    return html_parse_wrapper


class Download(object):
    """ class get html source by url"""

    @remove_script_style
    def get_html(self, url, data=None):
        """ here don't use urllib2, like as 'sina' site base failed sometimes,
            recommend to use pycurl library
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0'}
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        b = StringIO.StringIO()
        c.setopt(c.WRITEFUNCTION, b.write)
        c.setopt(c.SSL_VERIFYPEER, 0)
        c.setopt(c.SSL_VERIFYHOST, 0)
        c.setopt(c.FOLLOWLOCATION, 1)
        c.perform()
        html = b.getvalue()
        b.close()
        c.close()
        return self.to_utf8(html)

    @staticmethod
    def to_utf8(string):
        """ To different text types of transcoding centrally """
        # return value is a dictionary(have a key is 'encoding')
        charset = chardet.detect(string)['encoding']
        if charset is None:
            return string
        if charset != 'utf-8' and charset == 'GB2312':
            charset = 'gb18030'
        try:
            return string.decode(charset).encode('utf-8')
        except Exception, e:
            print 'chardet error:', e
        return ''

