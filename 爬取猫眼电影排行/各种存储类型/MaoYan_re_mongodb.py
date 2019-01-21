# coding = utf-8
__author__ = 'wardseptember'
__date__ = '18-10-26'
import pymongo
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }

def writeMongodb(content):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['maoyan']  # 给数据库命名
    maoyanTable = db['maoyan_top100']  # 表名
    maoyanTable.insert_one(content)

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        writeMongodb(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
    print("全部写入完成")