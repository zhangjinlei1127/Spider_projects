# -*- coding: utf-8 -*-
import scrapy


class DoupoSpider(scrapy.Spider):
    name = 'doupo'
    allowed_domains = ['txt53.com']
    start_urls = ['http://txt53.com/']

    def parse(self, response):
        pass
