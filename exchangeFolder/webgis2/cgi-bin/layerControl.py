#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: wardseptember

print "Content-Type:text/javascript"
print

disixi_str1='function disixi2(){'
for i in range(2):
	disixi_str1=disixi_str1+'''
			map.removeOverLay(polygon_dsj%d);
	'''% (i)
disixi_str1=disixi_str1+'}'
disixi_str2='function disixi1(){'
for i in range(2):
	disixi_str2=disixi_str2+'''
			map.addOverLay(polygon_dsj%d);
	'''% (i)
disixi_str2=disixi_str2+'}'
disixi=disixi_str2+disixi_str1


sandie_str1='function sandie2(){'
for i in range(2):
	sandie_str1=sandie_str1+'''
			map.removeOverLay(polygon_sd%d);
	'''% (i)
sandie_str1=sandie_str1+'}'
sandie_str2='function sandie1(){'
for i in range(2):
	sandie_str2=sandie_str2+'''
			map.addOverLay(polygon_sd%d);
	'''% (i)
sandie_str2=sandie_str2+'}'
sandie=sandie_str2+sandie_str1


erdie_str1='function erdie2(){'
for i in range(13):
	erdie_str1=erdie_str1+'''
			map.removeOverLay(polygon_ed%d);
	'''% (i)
erdie_str1=erdie_str1+'}'
erdie_str1=erdie_str1+'function erdie1(){'
for i in range(13):
	erdie_str1=erdie_str1+'''
			map.addOverLay(polygon_ed%d);
	'''% (i)
erdie_str1=erdie_str1+'}'


aotao_str1='function aotao2(){'
for i in range(10):
	aotao_str1=aotao_str1+'''
			map.removeOverLay(polygon_autao%d);
	'''% (i)
aotao_str1=aotao_str1+'}'
aotao_str1=aotao_str1+'function aotao1(){'
for i in range(10):
	aotao_str1=aotao_str1+'''
			map.addOverLay(polygon_autao%d);
	'''% (i)
aotao_str1=aotao_str1+'}'


shitan_str1='function shitan2(){'
for i in range(19):
	shitan_str1=shitan_str1+'''
			map.removeOverLay(polygon_st%d);
	'''% (i)
shitan_str1=shitan_str1+'}'
shitan_str1=shitan_str1+'function shitan1(){'
for i in range(19):
	shitan_str1=shitan_str1+'''
			map.addOverLay(polygon_st%d);
	'''% (i)
shitan_str1=shitan_str1+'}'


hanwu_str='function hanwu2(){'
for i in range(8):
	hanwu_str=hanwu_str+'''
			map.removeOverLay(polygon_hw%d);
	'''% (i)
hanwu_str=hanwu_str+'}'
hanwu_str=hanwu_str+'function hanwu1(){'
for i in range(8):
	hanwu_str=hanwu_str+'''
			map.addOverLay(polygon_hw%d);
	'''% (i)
hanwu_str=hanwu_str+'}'


yuangu_str='function yuangu2(){'
for i in range(5):
	yuangu_str=yuangu_str+'''
			map.removeOverLay(polygon_yg%d);
	'''% (i)
yuangu_str=yuangu_str+'}'
yuangu_str=yuangu_str+'function yuangu1(){'
for i in range(5):
	yuangu_str=yuangu_str+'''
			map.addOverLay(polygon_yg%d);
	'''% (i)
yuangu_str=yuangu_str+'}'


jincheng_str='function jincheng2(){'
jincheng_str=jincheng_str+'''
		map.removeOverLay(line);
'''
jincheng_str=jincheng_str+'}'
jincheng_str=jincheng_str+'function jincheng1(){'
jincheng_str=jincheng_str+'''
		map.addOverLay(line);
'''
jincheng_str=jincheng_str+'}'

print disixi+sandie+erdie_str1+aotao_str1+shitan_str1+hanwu_str+yuangu_str+jincheng_str