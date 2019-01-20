# coding = utf-8
__author__ = 'wardseptember'
__date__ = '19-1-20'
import json
import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    doc=pq(html)
    result_id=doc('.board-index')
    result_title=doc('.image-link')
    result_img=doc('.board-img')
    result_star=doc('.star')
    result_time=doc('.releasetime')
    result_score1=doc('.integer')
    result_score2 = doc('.fraction')

    result_id=[item.text() for item in result_id.items()]
    result_img=[item.attr('data-src') for item in result_img.items()]
    result_title=[item.attr('title') for item in result_title.items()]
    result_star=[item.text() for item in result_star.items()]
    result_time=[item.text() for item in result_time.items()]
    result_score1 = [item.text() for item in result_score1.items()]
    result_score2 = [item.text() for item in result_score2.items()]
    '''
    print(result_img)
    print(result_title)
    print(result_star)
    print(result_id)
    print(result_time)
    print(result_score1[0]+result_score2[0])
    '''
    for i in range(10):
        yield {
            'index': result_id[i],
            'image': result_img[i],
            'title': result_title[i],
            'actor': result_star[i].strip()[3:],
            'time': result_time[i].strip()[5:],
            'score': result_score1[i]+result_score2[i]
        }


def write_to_file(content):
    with open('result_pyquery.txt', 'a', encoding='utf-8') as f:
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