# -*- coding: utf-8 -*-
__author__ = 'wardseptember'
__date__ = '18-10-18'

#爬取渡边淳一小说大全
import requests
from bs4 import BeautifulSoup
import time
import os

TXTNAME='渡边淳一全集'
#获取每本书的章节内容
def get_chapter(url):
    # 获取网页的源代码
    try:
        html=requests.get(url,timeout=100)
        html.encoding = html.apparent_encoding
        content=html.content
        # 将网页源代码解析成HTML格式
        soup = BeautifulSoup(content, "lxml")
        title = soup.find('h1').text    #获取章节的标题
        text = soup.find('div', id='htmlContent')    #获取章节的内容
        #处理章节的内容，使得格式更加整洁、清晰
        content = text.get_text('\n','br/').replace('\n', '\n    ')
        content = content.replace('　　', '\n　　')
        return title, '    '+content
    except Exception as e:
        print(str(e))
        return "超时，未下载成功"


def main():
    # 书本列表
    books = ['男人这东西','失乐园','不分手的理由','红花','如此之爱','野蒿园','异恋']
    order = [5584,5585,5587,5588,5589,5586,5590]  #order of books to scrapy
    #list to store each book's scrapying range
    page_range = [210770,210789,210802,210813,210824,210834,210843,210872]
    if not os.path.exists(TXTNAME):
        os.makedirs(TXTNAME)
    for i,book in enumerate(books):
        bookPathName = TXTNAME + '/%s.txt' % book
        os.mknod(bookPathName)
        for num in range(page_range[i],page_range[i+1]):
            url = "http://dubianchunyi.zuopinj.com/%s/%s.html"%(order[i],num)
            try:
                title, chapter = get_chapter(url)
                time.sleep(2)
                with open(bookPathName, 'a', encoding='utf-8') as f:
                    print(book+':'+title+'-->写入成功！')
                    f.write(title+'\n\n\n')
                    f.write(chapter+'\n\n\n')
                    f.close()
            except Exception as e:
                print(str(e))
main()
