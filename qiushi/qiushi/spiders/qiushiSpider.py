# -*- coding: utf-8 -*-
import scrapy
from qiushi.items import QiushiItem


class QiushispiderSpider(scrapy.Spider):
    name = 'qiushiSpider'
    allowed_domains = ['qiushibaike.com']
    wc = ['/8hr/page/', '/hot/page/', 'text/page/', '/pic/page/']
    pages = 25
    start_urls = []
    for w in wc:
        for i in xrange(1, pages + 1):
            start_urls.append('https://www.qiushibaike.com' + w + str(i) + '/')

    def parse(self, response):
        subSelector = response.xpath('//div[@class = "col1"]')
        items = []
        for sub in subSelector:
            item = QiushiItem()
            # authors = ''
            # for author in sub.xpath('./div/div/a/h2/text()').extract():
            #     authors += author
            # item['author'] = authors
            item['author'] = sub.xpath('./div/div/a/h2/text()').extract()[0]
            item['content'] = sub.xpath(
                './div/a/div/span//text()').extract()
            item['img'] = sub.xpath(
                './div/div[@class="thumb"]/a/img/@src').extract()[0]
            item['funNum'] = sub.xpath(
                './div/div[@class="stats"]/span/i/text()').extract()[0]
            item['talkNum'] = sub.xpath(
                './div/div[@class= "stats"]/\
                span[@class="stats-vote"]/i/text()').extract()[0]
            items.append(item)
        return items
