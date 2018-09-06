# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class ZhangzhouspiderSpider(scrapy.Spider):
    name = 'zhangZhouSpider'
    allowed_domains = ['tianqi.com']
    citys = ['zhengzhou']
    start_urls = []
    for city in citys:
        start_urls.append('http://www.tianqi.com/' + city + '/15/')

    def parse(self, response):
        subSelector = response.xpath('//div[@class = "table_day "]')
        items = []
        for sub in subSelector:
            item = WeatherItem()


            #没看东下面的代码　　　　　　　　　　　　　　　　　　　　　　　　　　　　
            cityDates = ''
            for cityDate in sub.xpath('./h3/b//text()').extract():
                cityDates += cityDate


            item['cityDate'] = cityDates
            item['week'] = sub.xpath('./h3//text()').extract()[1]
            item['img'] = sub.xpath('./ul/li/img/@src').extract()[0]
            item['weather'] = sub.xpath('./ul/li[2]//text()').extract()[0]
            item['temperature'] = sub.xpath(
                './ul/li[2]//text()').extract()[1]
            item['wind'] = sub.xpath('./ul/li[4]//text()').extract()[0]
            items.append(item)
        return items
