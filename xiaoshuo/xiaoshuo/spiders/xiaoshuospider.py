# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo.items import XiaoshuoItem


class XiaoshuospiderSpider(scrapy.Spider):
    name = 'xiaoshuospider'
    allowed_domains = ['txt53.com']
    start_urls = []
    for i in range(1, 3):
        start_urls.append('http://txt53.com/read/44818_' + str(i) + ".html")

        def parse(self, response):
            # 嵌套选择　 选择整个网页中以div为标签的class属性为view_content的块
            # nestSelect是一个列表，里面装的是选择器
            nestSelect = response.xpath('//div[@class="view_content"]')

            items = []
            for nest in nestSelect:
                item = XiaoshuoItem()
                item['txtcontent'] = nest.xpath('./div//text()').extract()
                items.append(item)
            return items

# # 比去看网
# class XiaoshuospiderSpider(scrapy.Spider):
#     name = 'xiaoshuospider'
#     allowed_domains = ['biqukan.com']
#     start_urls = []
#     for i in range(64, 100):
#         start_urls.append(
#             'http://www.biqukan.com/1_1496/4503' + str(i) + ".html")

#         def parse(self, response):
#             # 嵌套选择　 选择整个网页中以div为标签的class属性为view_content的块
#             # nestSelect是一个列表，里面装的是选择器
#             nestSelect = response.xpath('//div[@class="view_content"]')

#             items = []
#             for nest in nestSelect:
#                 item = XiaoshuoItem()
#                 item['txtcontent'] = nest.xpath('./div//text()').extract()
#                 items.append(item)
#             return items
