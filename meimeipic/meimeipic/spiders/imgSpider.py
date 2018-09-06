# -*- coding: utf-8 -*-
import scrapy
from meimeipic.items import MeimeipicItem


class ImgspiderSpider(scrapy.Spider):
    name = 'imgSpider'
    allowed_domains = ['27270.com']
    wbs = ['meinvtupian/2017/226226', 'meinvtupian/2017/174240', 'meinvtupian/2017/174016',
           'meinvtupian/2017/173745', 'lianglimeimo/2016/165082', 'rentiyishu/2016/164738',
           'meinvtupian/2018/256998', 'meinvtupian/2017/226268', 'meinvtupian/2016/167284']
    start_urls = []
    for w in wbs:
        for i in xrange(1, 8):
            start_urls.append(
                'http://www.27270.com/ent/' + str(w) + '_' + str(i) + '.html')

    def parse(self, response):
        # 获取大的图片
        subSelector = response.xpath('//div[@class = "articleV4Body"]')
        items = []
        for sub in subSelector:
            item = MeimeipicItem()
            # item['imgName'] = sub.xpath("./p/a/img/@alt").extract()[0]
            item['img'] = sub.xpath("./p/a/img/@src").extract()[0]
            items.append(item)
        return items
