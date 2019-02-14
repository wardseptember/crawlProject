#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: wardseptember

print "Content-Type:text/javascript"
print


import shapefile
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
sf = shapefile.Reader("./cgi-bin/shapefile/yuangu.shp")
shapes = sf.shapes()

first_str = '''
'''
name_str=''''''
for num in range(len(shapes)):
	name_str=name_str+'''
		points_yg%d=[];
	'''% (num)

first_str=first_str+name_str

polyline_str = ''''''
for shp in range(len(shapes)):
    shap = shapes[shp]
    for i in range(len(shap.points)):
        polyline_str=polyline_str+'''
            points_yg%d.push(new T.LngLat(%f, %f));
        '''% (shp,shap.points[i][0],shap.points[i][1])


finally_str=''
for num in range(len(shapes)):
	finally_str=finally_str+'''
	    var polygon_yg%d = new T.Polygon(points_yg%d,{
	                color: "blue", weight: 3, opacity: 0.5, fillColor: "#005614", fillOpacity: 0.5
	            });
	    map.addOverLay(polygon_yg%d);
	'''% (num,num,num)

print first_str+polyline_str+finally_str
