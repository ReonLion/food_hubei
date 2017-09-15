#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Reon'

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class CustomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57'
        request.headers.setdefault('User-Agent', ua)
        
class CustomProxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://117.62.144.144:37185'