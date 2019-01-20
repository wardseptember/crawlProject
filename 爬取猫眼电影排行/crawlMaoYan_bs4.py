# coding = utf-8
__author__ = 'wardseptember'
__date__ = '19-1-20'
import json
import requests
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    soup=BeautifulSoup(html,'lxml')
    result_id=soup.select('.board-index')
    result_title=soup.select('.image-link')
    result_img=soup.select('.board-img')
    result_star=soup.select('.star')
    result_time=soup.select('.releasetime')
    result_score1=soup.select('.integer')
    result_score2 = soup.select('.fraction')
    for i in range(10):
        yield {
            'index': result_id[i].text,
            'image': result_img[i].attrs['data-src'],
            'title': result_title[i].attrs['title'],
            'actor': result_star[i].text.strip()[3:],
            'time': result_time[i].text.strip()[5:],
            'score': result_score1[i].text+result_score2[i].text
        }

def write_to_file(content):
    with open('result_bs4.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        #print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
       main(offset=i*10)