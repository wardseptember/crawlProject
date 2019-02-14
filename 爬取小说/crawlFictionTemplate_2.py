# -*- coding: utf-8 -*-
__author__ = 'wardseptember'
__date__ = '19-01-27'


import requests
import os
from pyquery import PyQuery as pq
import time

index_url = 'http://moyan.zuopinj.com/'
bookDict={}     #存放书籍和链接
dirName=''      #谁的作品集
class Book():

    #解析index_url得到所有书名和链接
    def getAllBookUrl(self):
        html=requests.get(index_url,timeout=100)
        html.encoding = html.apparent_encoding
        content=html.content
        doc=pq(content)
        global dirName
        dirName=doc('.head .logo a').text()
        items=doc('.content .box .books.section-cols .bk h3 a').items()
        for item in items:
            bookDict[item.text()]=item.attr('href')

    # 获取每本书的章节内容
    def getChapter(self,chapterUrl):
        # 获取网页的源代码
        try:
            html = requests.get(chapterUrl, timeout=100)
            html.encoding = html.apparent_encoding
            content = html.content
            doc=pq(content)
            # 获取章节的内容
            text=doc('.content .ncon .nc_l .contentbox p').text()
            # 处理章节的内容，使得格式更加整洁、清晰
            content = text.replace('\n', '\n    ')
            content='    '+content
            return content
        except Exception as e:
            print(str(e))
            return " "

    def writeToTxt(self):
        for key, value in bookDict.items():
            print('正在爬取 '+key)
            html=requests.get(value,timeout=100)
            html.encoding = html.apparent_encoding
            content = html.content
            doc=pq(content)
            chapterUrls=doc('.content .section .book_list ul li a').items()
            # 创建txt文件
            bookPathName = dirName + os.path.sep + key + '.txt'
            with open(bookPathName,'w',encoding='utf-8') as f:
                f.close()
                print(key+'.txt 创建成功')
            for item in chapterUrls:
                chapterName=item.text()
                chapterUrl=item.attr('href')
                try:
                    chapter=self.getChapter(chapterUrl)
                    time.sleep(2)
                    with open(bookPathName,'a',encoding='utf-8') as f:
                        f.write(chapterName+'\n\n\n')
                        f.write(chapter + '\n\n\n')
                        f.close()
                        print(key + ':' + chapterName + '-->写入成功！')
                except Exception as e:
                    print(str(e))
            print(key+' -->写入成功！')
        print("全部写入完成")

    def main(self):
        self.getAllBookUrl()
        # 创建文件夹
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        self.writeToTxt()



if __name__=='__main__':
    book=Book()
    book.main()