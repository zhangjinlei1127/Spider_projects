# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo.items import XiaoshuoItem


class MoocSpider(scrapy.Spider):
    name = 'Mooc'
    allowed_domains = ['tmooc.cn']
    start_urls = ['http://www.tmooc.cn/offline_courses/']

    def parse(self, response):
        txtSelect = response.xpath('//div[@class="text-box"]')
        items = []
        for txt in txtSelect:
            item = XiaoshuoItem()
            item['txtcontent'] = txt.xpath('.//text()').extract()
            items.append(item)
        return items
