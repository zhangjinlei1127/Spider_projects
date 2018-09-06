# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo.items import XiaoshuoItem


class FreespiderSpider(scrapy.Spider):
    name = 'freeSpider'
    allowed_domains = ['tmooc.cn']
    start_urls = ['http://tmooc.cn/free/']

    def parse(self, response):
        txtSelect = response.xpath('//div[@class="bd-word bgcolor-fff"]')
        items = []
        for txt in txtSelect:
            item = XiaoshuoItem()
            item['txtcontent'] = txt.xpath('./h4/a//text()').extract()
            items.append(item)
        return items
