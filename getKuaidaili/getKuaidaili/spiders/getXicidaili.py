# -*- coding: utf-8 -*-
import scrapy
from getKuaidaili.items import GetkuaidailiItem


class GetxicidailiSpider(scrapy.Spider):
    name = 'getXicidaili'
    allowed_domains = ['xicidaili.com']
    wds = ['nn', 'nt', 'wn', 'wt']
    pages = 20
    start_urls = []
    for type1 in wds:
        for i in xrange(1, pages + 1):
            start_urls.append('http://www.xicidaili.com/' +
                              type1 + '/' + str(i))

    def parse(self, response):
        subSelector = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        items = []
        for sub in subSelector:
            item = GetkuaidailiItem()
            item['ip'] = sub.xpath('.//td[2]//text()').extract()[0]
            item['port'] = sub.xpath('.//td[3]//text()').extract()[0]
            item['type1'] = sub.xpath('.//td[4]//text()').extract()[0]
            if sub.xpath('.//td[4]/a/text()'):
                item['loction'] = sub.xpath('//td[4]/a/text()').extract()[0]
            else:
                item['loction'] = sub.xpath('.//td[4]/text()').extract()[0]
            item['protocol'] = sub.xpath('.//td[6]/text()').extract()[0]
            item["source"] = 'xicidaili'
            items.append(item)
        return items
