#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: wardseptember
print "Content-Type:text/javascript"
print


import shapefile
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
sf = shapefile.Reader("./cgi-bin/shapefile/JCborder.shp")
shapes = sf.shapes()

polyline_str = ''''''
lng_num=[0.0]
lat_num=[0.0]
total_points=1
for shp in range(len(shapes)):
    shap = shapes[shp]
    for i in range(len(shap.points)):
    	total_points=total_points+1
    	lng_num.append(shap.points[i][0])
    	lat_num.append(shap.points[i][1])


for j in range(total_points):
    polyline_str=polyline_str+'''
        var point_%d=new T.LngLat(%f, %f);
        var marker_%d = new T.Marker(point_%d);
        map.addOverLay(marker_%d);
        marker_%d.disableDragging();  
    '''% (j,lng_num[j],lat_num[j],j,j,j,j)

polyline_str=polyline_str+'map.removeOverLay(marker_0)'
print polyline_str
