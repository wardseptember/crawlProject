# -*- coding: utf-8 -*-
__author__ = 'wardseptember'
__date__ = '19-01-27'


import requests
import os
from pyquery import PyQuery as pq
import time



'''
爬取塔读文学(http://www.tadu.com)上的小说
此例子爬取"聊斋志异"
'''

bookUrl='http://www.tadu.com/book/catalogue/735'
chapterDict={}
bookName=''
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36'
}

def getChapterDict(url):
    try:
        html = requests.get(url, timeout=100,headers=headers)
        html.encoding = html.apparent_encoding
        content = html.content
        doc = pq(content)
        global bookName
        bookName=doc('#container .right .book-detail.catalog-tip h1 a').text()
        items=doc('#container .right .detail-chapters ul li h5 a').items()
        for item in items:
            chapterDict[item.text().strip()]='http://www.tadu.com'+item.attr('href')
    except Exception as e:
        print(str(e))

def getChapter_2(chapterUrl):
    try:
        html=requests.get(chapterUrl,timeout=100,headers=headers)
        html.encoding=html.apparent_encoding
        content=html.content
        doc=pq(content)
        textUrl=doc('body #bookPartResourceUrl').attr('value')
        htmlTxt=requests.get(textUrl,timeout=100,headers=headers)
        con=htmlTxt.content
        htmlstr=con.decode('utf-8')[19:-3]
        doc_2=pq(htmlstr)
        items=doc_2('p').items()
        text='    '
        for item in items:
            text=text+item.text()+'\n'
        text = text.replace('\n', '\n\n    ')
        return text
    except Exception as e:
        print(str(e))
        return " "

def writeToTxt():
    global bookName
    bookName=bookName+'.txt'
    with open(bookName, 'w', encoding='utf-8') as f:
        f.close()
    try:
        for chapterName,value in chapterDict.items():
            text=getChapter_2(value)
            with open(bookName,'a',encoding='utf-8') as f:
                f.write(chapterName+'\n\n\n')
                f.write(text+'\n')
                print(bookName[:-4]+':'+chapterName+'-->写入成功')
                f.close()
        print("所有章节写入完成")
    except Exception as e:
        print(str(e))

def main():
    getChapterDict(bookUrl)
    writeToTxt()


if __name__=='__main__':
    main()