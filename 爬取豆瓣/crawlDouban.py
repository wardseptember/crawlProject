# coding = utf-8
__author__ = 'wardseptember'
__date__ = '18-10-18'
#!/usr/bin/python
# -*- coding: utf-8 -*- #
import requests,sys,re,pymysql,time
from bs4 import BeautifulSoup
'''
(1366, "Incorrect string value: '\\xE8\\x82\\x96\\xE7\\x94\\xB3...' 
for column 'movieName' at row 1")
如果遇到这个错误见
https://blog.csdn.net/sunhuaqiang1/article/details/51444018
https://www.cnblogs.com/mafeng/p/7987019.html
https://www.cnblogs.com/curious2017/p/6308839.html
'''

print('正在从豆瓣电影Top250抓取数据......')
# --------------------------创建列表用于存放数据-----------------------------#
nameList=[]
linkList=[]

#---------------------------------爬取模块------------------------------------#
def topMovie():
    for page in range(10):
        url='https://movie.douban.com/top250?start='+str(page*25)
        print('正在爬取第---'+str(page+1)+'---页......')
        html=requests.get(url)
        html.raise_for_status()
        try:
            soup=BeautifulSoup(html.text,'html.parser')
            soup=str(soup) # 利用正则表达式需要将网页文本转换成字符串
            name=re.compile(r'<span class="title">(.*)</span>')
            links=re.compile(r'<a class="" href="(.*)">')
            movieNames=re.findall(name,soup)
            movieLinks=re.findall(links,soup)
            for name in movieNames:
                if name.find('/')==-1: # 剔除英文名(英文名特征是含有'/')
                    nameList.append(name)
            for link in movieLinks:
                linkList.append(link)
        except Exception as e:
            print(e)
    print('爬取完毕！')
    return nameList,linkList

# ---------------------------------储存为文本文件-----------------------------------#
def save_to_txt():
    print('txt文件存储中......')
    try:
        f=open('data.txt','w')
        for i in range(250):
            f.write(nameList[i])
            f.write('\t'*3)
            f.write(linkList[i])
            f.write('\n')
        f.close()
    except Exception as e:
        print(e)
    print('txt文件存储结束！')

# ---------------------------------储存到文数据库-----------------------------------#
def save_to_MySQL():
    print('MySQL数据库存储中......')
    try:
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="156352", db="doubanDB", charset="utf8mb4")
        cursor = conn.cursor()
        print("数据库连接成功")
        #cursor.execute('Drop table if EXISTS MovieTop250') # 如果表存在就删除
        time.sleep(3)
        cursor.execute('''create table if not EXISTS MovieTop250(
                           movieName VARCHAR(50),
                           link VARCHAR(50))''')
        for i in range(250):
            nameList[i].encode('utf-8')
            linkList[i].encode('utf-8')
            sql='insert into MovieTop250(movieName,link) VALUES (%s,%s)'
            param=(nameList[i],linkList[i])
            cursor.execute(sql,param)
            conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    print('MySQL数据库存储结束！')

# -------------------------------------主模块--------------------------------------#
if __name__=="__main__":
    try:
        topMovie()
        save_to_txt()
        save_to_MySQL()
    except Exception as e:
        print(e)