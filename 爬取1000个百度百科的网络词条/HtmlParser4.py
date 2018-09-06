# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:21:43 2018

@author: Administrator
"""

import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        """
        用于解析网页内容，抽取URL和数据
        :param page_url : 下载页面的URL
        :param html_cont: 下载的网页内容
        ：return:返回URL和数据
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml', from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    def _get_new_urls(self,page_url,soup):
        """
        抽取新的URL的集合
        :param page_url : 下载页面的URL
        :param soup：soup
        :return : 返回新的URL集合
        """
        new_urls = set()
        # 抽取符合要求的a标记
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接成完整的网址
#            print("new_url:",new_url)
            new_full_url = urljoin(page_url, new_url)
#            print("new_full_url:", new_full_url)
            new_urls.add(new_full_url)
#            print(len(new_urls))
        return new_urls
    
    def _get_new_data(self, page_url, soup):
            '''
            #抽取有效数据
            :param page_url:下载页面的URL
            :param soup:
            ：return :返回有效的数据
            '''
            data = {}
#            print("data",data)
            data['url'] = page_url
    #        print("这是data：",data)
            title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
#            print("title", title)
            data['title'] = title.get_text()
            summary = soup.find('div', class_='lemma-summary')
            # 获取tag中包含的所有文本内容，包括子孙tag中的内容，并将结果作为Unicode字符串返回
            data['summary'] = summary.get_text()
#            print("最后的data:",data)
            return data