# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:53:45 2018

@author: Administrator
"""
import requests


class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        r = requests.get(url, headers = headers)
        if r.status_code == 200:
            r.encoding = "utf-8"
            print("响应成功")
            return r.text
        return None