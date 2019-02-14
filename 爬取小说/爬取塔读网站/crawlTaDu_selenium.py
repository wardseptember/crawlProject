# -*- coding: utf-8 -*-
__author__ = 'wardseptember'
__date__ = '19-01-27'

import requests
import os
from pyquery import PyQuery as pq
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


'''
爬取塔读文学(http://www.tadu.com)上的小说
此例子爬取"聊斋志异"
'''

#如果想爬取其他书籍只需更改bookUrl
bookUrl = 'http://www.tadu.com/book/catalogue/735'
chapterDict = {}
bookName = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36'
}
browser = webdriver.Chrome()  # 启动浏览器，可以发现弹出一个浏览器


# 获取所有章节标题和链接
def getChapterDict(url):
    try:
        html = requests.get(url, timeout=100, headers=headers)
        html.encoding = html.apparent_encoding
        content = html.content
        doc = pq(content)
        global bookName
        bookName = doc('#container .right .book-detail.catalog-tip h1 a').text()
        items = doc('#container .right .detail-chapters ul li h5 a').items()
        for item in items:
            chapterDict[item.text().strip()] = 'http://www.tadu.com' + item.attr('href')
    except Exception as e:
        print(str(e))


def getChapter(chapterUrl):
    # 获取网页内容
    try:
        browser.get(chapterUrl)
        time.sleep(3)
        # 等网页加载完成,才能获得text,继续向下进行
        text = browser.find_element(By.CSS_SELECTOR, '.main_ .text-content-.f-l .article_.c-3').text
        # 处理所的内容，使其更整洁
        text = text.replace('\n', '\n\n    ')
        text = '    ' + text
        return text
    except Exception as e:
        print(str(e))
        return " "


# 写入txt文件
def writeToTxt():
    global bookName
    bookName = bookName + '.txt'
    with open(bookName, 'w', encoding='utf-8') as f:
        f.close()
    try:
        for chapterName, value in chapterDict.items():
            text = getChapter(value)
            with open(bookName, 'a', encoding='utf-8') as f:
                f.write(chapterName + '\n\n\n')
                f.write(text + '\n')
                print(bookName[:-4] + ':' + chapterName + '-->写入成功')
                f.close()
        print("所有章节写入完成")
    except Exception as e:
        print(str(e))


def main():
    getChapterDict(bookUrl)
    writeToTxt()
    browser.close()


if __name__ == '__main__':
    main()