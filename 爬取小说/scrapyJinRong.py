# -*- coding: utf-8 -*-
__author__ = 'wardseptember'
__date__ = '18-10-18'


import requests
from bs4 import BeautifulSoup
import time

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
    books = ['射雕英雄传','天龙八部','鹿鼎记','神雕侠侣','笑傲江湖','碧血剑','倚天屠龙记',\
             '飞狐外传','书剑恩仇录','连城诀','侠客行','越女剑','鸳鸯刀','白马啸西风',\
             '雪山飞狐']
    order = [1,2,3,4,5,6,7,8,10,11,12,14,15,13,9]  #order of books to scrapy
    #list to store each book's scrapying range
    page_range = [1,43,94,145,185,225,248,289,309,329,341,362,363,364,374,385]

    for i,book in enumerate(books):
        # linux版本,wardseptember替换成你的linux主机名
        with open('//home//wardseptember//jinyong//%s.txt' % book, 'w', encoding='utf-8') as f1:
        #with open('D://jinyong//%s.txt'%book, 'w', encoding='gb18030') as f1:#window版本
            f1.close()
            pass
        for num in range(page_range[i],page_range[i+1]):
        #for num in range(185,225):
            url = "http://jinyong.zuopinj.com/%s/%s.html"%(order[i],num)
            # 错误处理机制
            try:
                title, chapter = get_chapter(url)
                time.sleep(2)
                # linux版本,wardseptember替换成你的linux主机名
                with open('//home//wardseptember//jinyong//%s.txt'%book, 'a', encoding='utf-8') as f:
                #with open('D://jinyong1//%s.txt'%book, 'a', encoding='gb18030') as f:#windows版本
                    print(book+':'+title+'-->写入成功！')
                    f.write(title+'\n\n\n')
                    f.write(chapter+'\n\n\n')
                    f.close()
            except Exception as e:
                print(str(e))
    print('全部写入完毕!')

main()
