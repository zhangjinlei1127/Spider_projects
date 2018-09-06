# -*- coding: utf-8 -*-
import scrapy
from fruitday.items import FruitdayItem


class FruitdayspiderSpider(scrapy.Spider):
    name = 'fruitdaySpider'
    allowed_domains = ['fruitday.com']
    start_urls = ['http://staging.www.fruitday.com/prolist/index/277/']

    def parse(self, response):
        subSelector = response.xpath('//li')
        items = []
        for sub in subSelector:
            item = FruitdayItem()
            item['img'] = sub.xpath(
                './div/div[@class="s-img"]/a/img/@src').extract()
            item['name'] = sub.xpath(
                './div/div[@class="s-name"]/text()').extract()
            item['price'] = sub.xpath(
                './div/div[@class="s-unit"]/text()').extract()
            items.append(item)
        return items
