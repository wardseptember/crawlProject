#!/usr/bin/python
# -*- coding:utf-8 -*-
print "Content-Type:text/html"
print


import sys
reload(sys)
sys.setdefaultencoding('utf-8') 



first_str = '''points = [];'''
polyline_str = ''''''
with open('./cgi-bin/border.txt', 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if not lines:
        break
    p_tmp, e_tmp = [float(i) for i in lines.split()]
    polyline_str = polyline_str + '''
        points.push(new T.LngLat(%f, %f));
    ''' % (p_tmp, e_tmp)

finally_str='''
    var line = new T.Polyline(points);
    map.addOverLay(line);
'''

print first_str+polyline_str