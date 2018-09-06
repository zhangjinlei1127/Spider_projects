# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:47:47 2018

@author: Administrator
"""

import codecs

class DataOutput(object):
    
    def __init__(self):
        self.datas = []
        
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    
    def output_html(self):
        
        with open("百度百科1.txt",'a',encoding="utf-8") as f:
            for data in self.datas:
                f.write("url"+data['url']+ '\n')
                f.write("title: "+data['title']+'\n')
                f.write("summary: "+data['summary'].strip()+'\n\n')
                
                
                
        with codecs.open("百度百科2.txt",'a',encoding="utf-8") as f:
            for data in self.datas:
                f.write("url"+data['url']+ '\n')
                f.write("title: "+data['title']+'\n')
                f.write("summary: "+data['summary'].strip()+'\n\n')
                
                
        with codecs.open('百度百科.html','a', encoding = 'utf-8') as fout:
            
            fout.write('<html>')
            fout.write('<body>')
            fout.write('<table border=1 style="color:red">')
            for data in self.datas:
                fout.write('<tr>')
                fout.write('<td>%s</td>'%data['url'])
                fout.write('<td>%s</td>'%data['title'])
                fout.write('<td>%s</td>'%data['summary'])
                fout.write('</tr>')
                self.datas.remove(data)
            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')
            fout.close()


                #出现的状况值保存一般的值
#        