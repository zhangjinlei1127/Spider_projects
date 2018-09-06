# -*- coding: utf-8 -*-
import scrapy
from meizipic.items import MeizipicItem


class MeizispiderSpider(scrapy.Spider):
    name = 'meiziSpider'
    allowed_domains = ['27270.com']
    wds = ['875', '866', '748', '642', '637', '634',
           '566', '480', '426', '421', '335', '331', '239',
           '183', '86', '636', '267', '1948',
           ]
    start_urls = []
    for w in wds:
        for i in xrange(3, 8):
            start_urls.append('http://www.27270.com/tag/' +
                              str(w) + '_' + str(i) + '.html')

    def parse(self, response):
        subSelector = response.xpath('//li')
        items = []
        for sub in subSelector:
            item = MeizipicItem()
            item['imgName'] = sub.xpath("./a/span/text()").extract()
            item['img'] = sub.xpath('./a/img/@src').extract()

            items.append(item)
        return items
