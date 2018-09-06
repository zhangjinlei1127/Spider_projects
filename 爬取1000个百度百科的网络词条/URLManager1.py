# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:14:05 2018

@author: Administrator
"""

'''
创建两个集合来去重
：一个为 未爬取的URL集合
: 一个为 已经爬取的URL集合
'''
import urllib.parse



class UrlManager(object):
    def __init__(self):
        self.new_urls = set() #未爬取的URL的集合
        self.old_urls = set() #已获取的URL的集合
        
        
    #接口
    #1. 判断  是否有代取的URL has_new_url()
    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        ：return
        '''
        return self.new_url_size() != 0
    
    
    #2.获取一个未爬取的URL
    def get_new_url(self):
        '''
        获取一个未爬取的URL
        ：return
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        print("new_url",new_url)
        return new_url
    
    #3.添加新的URL到未爬取的集合中 
    def add_new_url(self,url):
        '''
        将新的URL添加到未爬取的URL集合中
        :param url:单个URL
        :retu： 
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(urllib.parse.unquote(url))
            
            
    def add_new_urls(self,urls):
        """
        将新的URL添加到未爬取的URL集合中
        ：param urls:url 集合
        :return
        """
        if urls is None or len(urls)==0:
            return 
        for url in urls:
            self.add_new_url(url)
        
    #4.获取未爬取URL集合的大小
    def new_url_size(self):
        '''
        获取未爬取URL集合的大小
        : return: 
        '''
        print(len(self.new_urls))
        return len(self.new_urls)
    #5.获取已经爬取的URL集合的大小
    def old_url_size(self):
        """
        获取已经爬取URL集合的大小
        :return
        """
        return len(self.old_urls)