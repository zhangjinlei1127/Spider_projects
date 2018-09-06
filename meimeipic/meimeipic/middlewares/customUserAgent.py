#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhanglei@maomao.com'


from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from meimeipic.middlewares.userAgents import UserAgents
import random


class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(UserAgents)
        request.headers.setdefault('User-Agent', ua)
