# coding = utf-8
__author__ = 'wardseptember'
__date__ = '18-10-26'


"""测试单号：9792274485882
"""

import json
import requests


def getExpressInfo(num):

    #这里是用来找特定文件提取特定的单号对应的公司信息
    urlpara = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text={}'
    paga =requests.get(urlpara.format(num))
    if paga.status_code!=200:
        print('查询失败！')
        exit()
    else:
        jsonobj = json.loads(paga.text)
        #print(jsonobj)
        for item in jsonobj.get('auto'):
            com=item.get('comCode')
            url='https://www.kuaidi100.com/query?type={}&postid={}'.format(com,num)
            response = requests.get(url)
            if response.status_code!=200:
                print('查询失败!')
            else:
                mes=json.loads(response.text)
                #print(com+mes.get('message'))
                if mes.get('message')=='ok':
                    #print(mes.get('data'))
                    for data in mes.get('data'):
                        print('%s %s' % (data.get('time'), data.get('context')))
            break


if __name__ == "__main__":

    num = input('请输入要查单号:')
    getExpressInfo(num)