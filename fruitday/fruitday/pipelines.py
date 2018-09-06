# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import urllib2
import os


class FruitdayPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime("%Y-%m-%d", time.localtime())
        fileName = today + "fruitday.txt"
        imgDir = 'IMG'
        if os.path.isdir(imgDir):
            pass
        else:
            os.mkdir(imgDir)
        with open(fileName, 'a') as fp:
            # fp.write("图片名字： \t %s \n " % (item['name'][0].encode('utf8')))
            # fp.write("价格：　\t %s \n" % (item['price'][0].encode("utf8")))
            fp.write("dada")
            try:
                imgurl = item['img'][0]
            except IndexError:
                pass
            else:
                picName = os.path.basename(imgurl)
                fp.write("img:\t %s \n " % (picName))
                imgpathName = imgDir + os.sep + picName

                with open(imgpathName, 'wb') as fpi:
                    response = urllib2.urlopen(imgurl, timeout=5)
                    fpi.write(response.read())
        return item
