# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import urllib2
import os


class MeimeipicPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime("%Y-%s-%d", time.localtime())
        fileName = today + "美女.txt"
        imgDir = 'IMG'
        if os.path.isdir(imgDir):
            pass
        else:
            os.mkdir(imgDir)
        with open(fileName, 'a') as fp:
            # fp.write("图片名字: \t %s \n" % (item['imgName'][0].encode('utf8')))
            fp.write("12312456")
            try:
                imgurl = item['img']
            except IndexError:
                pass
            else:
                picName = os.path.basename(imgurl)
                fp.write("img:\t %s \n " % (picName))
                imgpathName = imgDir + os.sep + picName
                with open(imgpathName, 'wb') as fpi:
                    response = urllib2.urlopen(imgurl, timeout=3)
                    fpi.write(response.read())
        return item
