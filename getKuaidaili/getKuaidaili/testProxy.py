#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
__author__ = 'hstking hsting@hotmail.com'
import urllib2
import re
import threading
import time


class TestgetKuaidaili(object):
    def __init__(self):
        self.sFile = r'xicidaili.txt'
        self.dFile = r'alive.txt'
        self.URL = r'http://www.baidu.com/'
        self.threads = 10
        self.timeout = 3
        self.regex = re.compile(r'baidu.com')
        self.aliveList = []

        self.run()

    def run(self):
        with open(self.sFile, 'r') as fp:
            lines = fp.readlines()

            line = lines.pop()
            while lines:
                for i in xrange(self.threads):
                    t = threading.Thread(
                        target=self.linkWithXicidaili, args=(line,))
                    t.start()
                    if lines:
                        line = lines.pop()
                    else:
                        continue

        time.sleep(15)

        with open(self.dFile, 'w') as fp:
            for i in xrange(len(self.lis)):
                fp.write(self.lis[i])
        print("文档输入结束")

        #遇到的问题　当一个进程调取另一个京城时　
            #调取的进程数据还没有放给调取的函数导致数据没有写入函数
            #冷静分析问题
            #一部一部的剖析

    def linkWithXicidaili(self, line):
        lineList = line.split('\t')
        protocol = lineList[2].lower()
        server = protocol + r' ://' + lineList[0] + ":" + lineList[1]
        opener = urllib2.build_opener(
            urllib2.ProxyHandler({protocol: server}))

        urllib2.install_opener(opener)

        try:
            response = urllib2.urlopen(self.URL, timeout=self.timeout)#爬虫代理词　用来反复测试
        except:
            print('%s connect failed' % server)
            return
        else:
            try:
                str = response.read()
            except:
                print('%s connext failed' % server)
                return
            if self.regex.search(str):
                print('%s connect success ..................' % server)
                self.aliveList.append(line)
                self.lis = self.aliveList
            print(len(self.aliveList))


if __name__ == "__main__":
    TP = TestgetKuaidaili()
 