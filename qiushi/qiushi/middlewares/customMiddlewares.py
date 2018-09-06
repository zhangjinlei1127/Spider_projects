#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hstking hstking@hotmail.com'


from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class CustomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = "Mozilla/5.0 (X11; Ubuntu; \
        Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
        request.headers.setdefault('User-Agent', ua)


class CustomProxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://180.118.243.105:808'
