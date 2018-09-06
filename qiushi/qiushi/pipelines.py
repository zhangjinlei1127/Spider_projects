# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import time
# import urllib2
# import os


class QiushiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%s-%d', time.localtime())
        fileName = today + 'qiushi.txt'
        # imgDir = 'IMG'
        # if os.path.isdir(imgDir):
        #     pass
        # else:
        #     os.mkdir(imgDir)
        with open(fileName, 'a') as fp:
            fp.write('-' * 50 + '\n' + '*' * 50 + '\n')
            fp.write("author:\t %s\n" % (item['author'].encode('utf8')))
            # fp.write("content:\t %s\n" % (item['content'].encode('utf8')))
            try:
                for i in range(100):
                    fp.write("\t %s\n" %
                             (item['content'][i].encode('utf8')))

            except IndexError:
                pass

            # else:
            #     imgName = os.path.basename(imgUrl)
            #     fp.write('img:/t %s\n' % (imgName))
            #     imgPathName = imgDir + os.sep + imgName
            #     with open(imgPathName, 'wb') as fpi:
            #         response = urllib2.urlopen(imgUrl)
            #         fpi.write(response.read())
            # imgName = os.path.basename(item['img'])
            # fp.write(imgName + '\t')
            # if os.path.exists(imgName):
            #     pass
            fp.write('fun:%s\t' % (item['funNum'].encode('utf8')))
            fp.write('talk:%s\n' % (item['talkNum'].encode('utf8')))
            fp.write('#' * 50 + '\n' + '&' * 50 + '\n' * 10)
        return item
