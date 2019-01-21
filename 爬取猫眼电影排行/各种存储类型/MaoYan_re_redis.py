# coding = utf-8
__author__ = 'wardseptember'
__date__ = '18-10-26'
import json
import requests
from requests.exceptions import RequestException
import re
from redis import StrictRedis

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

def write_to_file(content):
    redis=StrictRedis(host='localhost',port=6379,db=0,password='foobared')
    redis.lpush('index',content['index'])
    redis.lpush('image',content['image'])
    redis.lpush('title',content['title'])
    redis.lpush('actor',content['actor'])
    redis.lpush('time',content['time'])
    redis.lpush('score',content['score'])
    res=redis.pipeline()
    keys=redis.keys()
    key_list=[]
    for key in keys:
        key_list.append(key)
        res.get(key)
    for k,v in zip(key_list,res.execute()):
        print(k,v)

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        #print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)