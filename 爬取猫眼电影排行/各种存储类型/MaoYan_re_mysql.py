# coding = utf-8
__author__ = 'wardseptember'
__date__ = '18-10-26'
import json
import requests
from requests.exceptions import RequestException
import re
import pymysql

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
        yield (int(item[0]),item[2],item[1],item[3].strip()[3:],item[4].strip()[5:],float(item[5]+item[6]))

def createDatabase():
    db = pymysql.connect(host='localhost', user='root', password='156352', port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version:', data)
    cursor.execute("CREATE DATABASE IF NOT EXISTS MaoYanDB DEFAULT CHARACTER SET utf8")
    print("MaoYanDB数据库创建成功")
    db.close()

def createTableMaoYanDB():
    db=pymysql.connect(host='localhost',user='root',password='156352',port=3306,db='MaoYanDB',charset='utf8')
    cursor=db.cursor()
    sql_table = 'CREATE TABLE IF NOT EXISTS maoyan (id INT NOT NULL, title VARCHAR(255) NOT NULL, ' \
                'image VARCHAR(255) NOT NULL, actor VARCHAR(255) NOT NULL, releasetime VARCHAR(255) NOT NULL, ' \
                'score FLOAT NOT NULL, PRIMARY KEY(id))'
    cursor.execute(sql_table)
    print("maoyan表创建成功")
    db.close()

def writeMysql(content):
    db=pymysql.connect(host='localhost',user='root',password='156352',port=3306,db='MaoYanDB',charset='utf8')
    cursor=db.cursor()
    sql_insert='INSERT INTO maoyan(id,title,image,actor,releasetime,score) values(%s, %s, %s, %s, %s, %s)'
    cursor.execute(sql_insert,(content))
    db.commit()
    db.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        writeMysql(item)


if __name__ == '__main__':
    createDatabase()
    createTableMaoYanDB()
    for i in range(10):
        main(offset=i*10)
    print("全部写入成功")