# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:56:25 2018

@author: Administrator
"""

from URLManager1 import UrlManager
from HtmlDownloader2 import   HtmlDownloader
from HtmlParser4 import HtmlParser
from DataOutput5 import DataOutput

class SpiderMan(object):
    
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
        
    def crawl(self,root_url):
        #添加入口URL
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的URL，同时判断抓取多少个URL
        while(self.manager.has_new_url() and self.manager.old_url_size()<1000):
            try:
                #从URL管理器获取新的url
                new_url = self.manager.get_new_url()
                #HTML 下载器下载页面
                html = self.downloader.download(new_url)
#                print(html)
                #HTML 解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url, html)
                #将抽取的URL添加到URL管理其中
                
                self.manager.add_new_urls(new_urls)
                #将数据存储成txt
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception:
                print("crawl dailed")
             # 数据存储器将文件输出成指定格式
        self.output.output_html()


if __name__ == "__main__":
    spider_man = SpiderMan()
#    url = "https://baike.baidu.com/item/"
    baike = input("请输入你要搜索的词语: ")
    spider_man.crawl("https://baike.baidu.com/item/"+ baike)
                