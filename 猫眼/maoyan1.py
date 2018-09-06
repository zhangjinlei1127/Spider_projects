# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 23:07:30 2018

@author: MAIBENBEN
"""

import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool
from multiprocessing import  Manager
import functools


def get_ono_page(url):
    """
    获取一个页面数据
    """
    headers = {
            "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
            }
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
    
    
def deal_one_page(html):
    pattern = re.compile('<p class="name">[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    results = re.findall(pattern, html)
    for item in results:
        yield{
              'title':item[0].strip(),
              'stars':item[1].strip(),
              'releasetime':item[2].strip()
                }


def write2File(item):
    """
    将抓取到数据一条条写入maoyan.txt
    """
    with open ("maoyam.txt" , "a" , encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False)+'\n')
    

def crawlpage(lock, offset):
#获取一个网页
    url="http://maoyan.com/board/4?offset=" + str(offset)
#下载页面
    html = get_ono_page(url)
#提取信息，写入到本地的文件系统或者数据库
    for item in deal_one_page(html):
        lock.acquire()
        write2File(item)
        lock.release()
    
if __name__ =="__main__":
    manager = Manager()
    lock = manager.Lock()
    #使用一个函数包装器
    pcrawlpage = functools.partial(crawlpage, lock)
    pool = Pool()
    pool.map(pcrawlpage, [i*10 for i in range(10)])
    pool.close()
    pool.join() #等待进程
    print("OK")
