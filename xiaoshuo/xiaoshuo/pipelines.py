# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time


class XiaoshuoPipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'xiaoshuo' + now + '.txt'
        with open(fileName, 'a') as fp:
            for i in range(500):
                fp.write(item['txtcontent'][i].encode('utf8') + "\n")
                # a = fp.write(item['txtcontent'][i].encode('utf8'))
                # if a == "\r":
                #     pass
                # else:
                #     a
        return item
