# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import urllib2
import os


class MeizipicPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime("%Y%m%d", time.localtime())
        fileName = today + 'meiziimg.txt'
        imgDir = 'IMG'
        if os.path.isdir(imgDir):
            pass
        else:
            os.mkdir(imgDir)
        with open(fileName, 'a') as fp:
            fp.write('-' * 50 + '\n')
            fp.write("图片名字: \t %s \n" % (item['imgName'][0].encode('utf8')))
            try:
                imgUrl = item['img'][0]
            except IndexError:
                pass
            else:
                picName = os.path.basename(imgUrl)
                fp.write("img:\t %s\n" % (picName))
                imgpathName = imgDir + os.sep + picName
                with open(imgpathName, 'wb') as fpi:
                    response = urllib2.urlopen(imgUrl, timeout=3)
                    fpi.write(response.read())

            fp.write('*' * 50 + '\n' + '\n')

        return item
