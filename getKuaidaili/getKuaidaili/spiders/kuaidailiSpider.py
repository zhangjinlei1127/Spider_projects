# -*- coding: utf-8 -*-
import scrapy
from getKuaidaili.items import GetkuaidailiItem


class KuaidailispiderSpider(scrapy.Spider):
    name = 'kuaidailiSpider'
    allowed_domains = ['kuaidaili.com']
    wds = ['inha', 'intr']
    pages = 20
    start_urls = []
    for type1 in wds:
        for i in xrange(1, pages + 1):
            start_urls.append(
                'https://www.kuaidaili.com/free/' + type1 + '/' + str(i))

    def parse(self, response):
        subSelector = response.xpath('//tr/')
        items = []
        for sub in subSelector:
            item = GetkuaidailiItem()
            item['ip'] = sub.xpath('./td[1]/text()').extract()[0]
            item['port'] = sub.xpath('./td[2]/text()').extract()[0]
            item['type1'] = sub.xpath('./td[3]/text()').extract()[0]
            item['loction'] = sub.xpath('./td[5]/text()').extract()[0]
            item['protocol'] = sub.xpath('./td[4]/text()').extract()[0]
            item['socure'] = "kuaidaili"
            items.append(item)
        return items
