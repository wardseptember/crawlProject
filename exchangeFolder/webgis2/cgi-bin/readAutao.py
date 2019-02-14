#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: wardseptember
print "Content-Type:text/javascript"
print


import shapefile
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
sf = shapefile.Reader("./cgi-bin/shapefile/aotao.shp")
shapes = sf.shapes()

first_str = '''
	var map;
    var zoom = 9;
    map = new T.Map('allmap', {
        projection: 'EPSG:32650'
    });
    map.centerAndZoom(new T.LngLat(112.858577, 35.497694), zoom);

    var line = new T.Polyline(points);
    map.addOverLay(line);
'''
name_str=''''''
for num in range(len(shapes)):
	name_str=name_str+'''
		points_autao%d=[];
	'''% (num)

first_str=first_str+name_str

polyline_str = ''''''
for shp in range(len(shapes)):
    shap = shapes[shp]
    for i in range(len(shap.points)):
        polyline_str=polyline_str+'''
            points_autao%d.push(new T.LngLat(%f, %f));
        '''% (shp,shap.points[i][0],shap.points[i][1])


finally_str=''
for num in range(len(shapes)):
	finally_str=finally_str+'''
	    var polygon_autao%d = new T.Polygon(points_autao%d,{
	                color: "blue", weight: 3, opacity: 0.5, fillColor: "red", fillOpacity: 0.5
	            });
	    map.addOverLay(polygon_autao%d);
	'''% (num,num,num)

print first_str+polyline_str+finally_str
