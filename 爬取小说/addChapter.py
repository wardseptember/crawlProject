# -*- coding: utf-8 -*-
__author__ = 'wardseptember'
__date__ = '19-01-27'


import requests
import os
from pyquery import PyQuery as pq
import time


def getChapter(chapterUrl):
    # 获取网页的源代码
    try:
        html = requests.get(chapterUrl, timeout=100)
        html.encoding = html.apparent_encoding
        content = html.content
        doc = pq(content)
        # 获取章节的内容
        text = doc('.content .ncon .nc_l .contentbox p').text()
        # 处理章节的内容，使得格式更加整洁、清晰
        content = text.replace('\n', '\n    ')
        content = '    ' + content
        return content
    except Exception as e:
        print(str(e))
        return " "


def writeToTxt():
    key='檀香刑'
    print('正在爬取 ' + key)
    chapterUrl = 'http://moyan.zuopinj.com/986/34787.html'
    # 创建txt文件
    bookPathName = '补充缺少章.txt'
    with open(bookPathName, 'w', encoding='utf-8') as f:
        f.close()
        print(bookPathName + '创建成功')
    try:
        chapter = getChapter(chapterUrl)
        time.sleep(2)
        with open(bookPathName, 'a', encoding='utf-8') as f:
            f.write(chapter + '\n')
            f.close()
            print(key + ':缺失章-->写入成功！')
    except Exception as e:
        print(str(e))

if __name__=='__main__':
    writeToTxt()