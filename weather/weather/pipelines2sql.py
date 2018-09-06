# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import os.path


class WeatherPipeline(object):
    def process_item(self, item, spider):
        cityDate = item['cityDate'].encode('utf8')
        week = item['week'].encode('utf8')
        img = os.path.basename(item['img'])
        weather = item['weather'].encode('utf8')
        temperature = item['temperature'].encode('utf8')
        wind = item['wind'].encode('utf8')

        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            charset='utf8',
            db='scrapydbweather')
        cur = conn.cursor()
        cur.execute(
            "insert into \
            weather(cityDate,week,img,weather,temperature,wind) \
            values(%s,%s,%s,%s,%s,%s)",
            (cityDate, week, img, weather,
                temperature, wind))
        cur.close()
        conn.commit()
        conn.close()

        return item
