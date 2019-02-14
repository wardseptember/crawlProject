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
first_str = '''points = [];'''
polyline_str = ''''''
for shp in range(len(shapes)):
    shap = shapes[shp]
    for i in range(len(shap.points)):
        polyline_str=polyline_str+'''
            points.push(new T.LngLat(%f, %f));
        '''% (shap.points[i][0],shap.points[i][1])
finally_str='''
    var line = new T.Polyline(points);
    map.addOverLay(line);
'''

print first_str+polyline_str
