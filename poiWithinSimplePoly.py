#coding=UTF-8

import csv
import json


# 点是否在外包矩形内
def isPoiWithinBox(poi, sbox, toler=0.0001):
	# sbox=[[x1,y1],[x2,y2]]
	# 不考虑在边界上，需要考虑就加等号
	if poi[0] > sbox[0][0] and poi[0] < sbox[1][0] and poi[1] > sbox[0][1] and poi[1] < sbox[1][1]:
		return True
	if toler > 0:
		pass
	return False


# 射线与边是否有交点
def isRayIntersectsSegment(poi, s_poi, e_poi):  # [x,y] [lng,lat]
	if s_poi[1] == e_poi[1]:  # 排除与射线平行、重合，线段首尾端点重合的情况
		return False
	if s_poi[1] > poi[1] and e_poi[1] > poi[1]:
		return False
	if s_poi[1] < poi[1] and e_poi[1] < poi[1]:
		return False
	if s_poi[1] == poi[1] and e_poi[1] > poi[1]:
		return False
	if e_poi[1] == poi[1] and s_poi[1] > poi[1]:
		return False
	if s_poi[0] < poi[0] and e_poi[1] < poi[1]:
		return False
	xseg = e_poi[0] - (e_poi[0] - s_poi[0]) * (e_poi[1] - poi[1]) / (e_poi[1] - s_poi[1])  # 求交
	if xseg < poi[0]:
		return False
	return True

#只适用简单多边形
def isPoiWithinSimplePoly(poi, simPoly, tolerance=0.0001):
	# 点；多边形数组；容限
	# simPoly=[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]]
	# 如果simPoly=[[x1,y1],[x2,y2],……,[xn,yn]] i循环到终点后还需要判断[xn,yx]和[x1,y1]
	# 先判断点是否在外包矩形内
	if not isPoiWithinBox(poi, [[0, 0], [180, 90]], tolerance):
		return False

	polylen = len(simPoly)
	sinsc = 0  # 交点个数
	for i in range(polylen - 1):
		s_poi = simPoly[i]
		e_poi = simPoly[i + 1]
		if isRayIntersectsSegment(poi, s_poi, e_poi):
			sinsc += 1

	return True if sinsc % 2 == 1 else  False

def isPoiWithinPoly(poi, poly, tolerance=0.0001):
	# 点；多边形三维数组；容限
	# poly=[[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]],[[w1,t1],……[wk,tk]]] 三维数组

	# 先判断点是否在外包矩形内
	if not isPoiWithinBox(poi, [[0, 0], [180, 90]], tolerance):
		return False

	sinsc = 0  # 交点个数
	for epoly in poly: #逐个二维数组进行判断
		for i in range(len(epoly) - 1):  # [0,len-1]
			s_poi = epoly[i]
			e_poi = epoly[i + 1]
			if isRayIntersectsSegment(poi, s_poi, e_poi):
				sinsc += 1
        return sinse %2 !=0 #这样更简洁些
	#return True if sinsc % 2 == 1 else  False


## 应用

### 比较完备的版本
def pointInPolygon(cin_path,out_path,gfile,t=0):
    pindex = [2,3]  # wgslng,wgslat  2,3
    with open(out_path, 'w', newline='') as cut_file:
        fin = open(cin_path, 'r', encoding='gbk')
        gfn = open(gfile, 'r', encoding='utf-8')
        gjson = json.load(gfn)
        if gjson["features"][0]["geometry"]['type']=="MultiPolygon":
            plist=gjson["features"][0]["geometry"]['coordinates'] #四维
            filewriter = csv.writer(cut_file, delimiter=',')

            w = 0
            for line in csv.reader(fin, delimiter=','):
                if w == 0:
                    filewriter.writerow(line)
                    w = 1
                    continue
		point = [float(line[pindex[0]]), float(line[pindex[1]])]
                for polygon in plist:  #
                    if isPoiWithinPoly(point, polygon):
                        filewriter.writerow(line)
		        break
            fin.close()
            gfn.close()
        elif gjson["features"][0]["geometry"]['type']=="Polygon":
            polygon=gjson["features"][0]["geometry"]['coordinates'] #三维
            filewriter = csv.writer(cut_file, delimiter=',')
            w = 0
            for line in csv.reader(fin, delimiter=','):
                if w == 0:
                    filewriter.writerow(line)
                    w = 1
                    continue
                point = [float(line[pindex[0]]), float(line[pindex[1]])]
                if isPoiWithinPoly(point, polygon):
                    filewriter.writerow(line)
            fin.close()
            gfn.close()
        else:
            print('check',gfile)
        print('end')
#调用
def baTch():
    import os
    import glob
    wpath="D:/DigitalC_data/coordConvert" #文件路径
    sname="D:/DigitalC_data/coordConvertOut"
    gpath='D:/cityBoundaryJson/guangzhou_wgs84.json'
    for input_file in glob.glob(os.path.join(wpath, '*.csv')):
        fname=input_file.split('\\')
        pointInPolygon(input_file,os.path.join(sname,fname[1]),gpath)
        print(fname[1])


### 应用方式1
def pointInPolygon1():
	gfile = 'E:/ComputerGraphicsProj/Geojson2kml/J2K_data/深圳poly_bd09.geojson'
	cin_path = 'L:/OtherSys/DigitalCityData/深圳特征图层/city_site_poi_sec_shenzhen.csv'
	out_path = 'L:/OtherSys/DigitalCityData/深圳特征图层/city_site_poi_sec_shenzhen_out1.csv'

	pindex = [4, 5]  # wgslng,wgslat  2,3

	with open(out_path, 'w', newline='') as cut_file:
		fin = open(cin_path, 'r', encoding='gbk')
		gfn = open(gfile, 'r', encoding='utf-8')
		gjson = json.load(gfn)
		polygon = gjson["features"][0]["geometry"]['coordinates'][0]
		filewriter = csv.writer(cut_file, delimiter=',')
		w = 0
		for line in csv.reader(fin, delimiter=','):
			if w == 0:
				filewriter.writerow(line)
				w = 1
				continue
			point = [float(line[pindex[0]]), float(line[pindex[1]])]
			if isPoiWithinSimplePoly(point, polygon):
				filewriter.writerow(line)

		fin.close()
		gfn.close()
	print('done')


#pointInPolygon1()

def csvToDArrary(csvpath):#csv文件转二维数组
	cdata = []
	with open(csvpath, 'r', encoding='gbk') as rfile:
		for line in csv.reader(rfile, delimiter=','):
			cdata.append(line)

	return cdata
### 应用方式2
def pointInPolygon2():
	gfile = 'E:/ComputerGraphicsProj/Geojson2kml/J2K_data/深圳poly_bd09.geojson'
	cin_path = 'L:/OtherSys/DigitalCityData/深圳特征图层/shenzhen_tAllNotIn.csv'
	out_path = 'L:/OtherSys/DigitalCityData/深圳特征图层/shenzhen_tAllNotIn_out2.csv'

	pindex = [4, 5]  # wgslng,wgslat  2,3

	with open(out_path, 'w', newline='') as cut_file:
		gfn = open(gfile, 'r', encoding='utf-8')
		gjson = json.load(gfn)
		polygon = gjson["features"][0]["geometry"]['coordinates'][0]
		filewriter = csv.writer(cut_file, delimiter=',')
		w = 0
		cdata = csvToDArrary(cin_path)
		for line in cdata:
			if w == 0:
				filewriter.writerow(line)
				w = 1
				continue
			point = [float(line[pindex[0]]), float(line[pindex][1])]
			if isPoiWithinSimplePoly(point, polygon):
				filewriter.writerow(line)

		gfn.close()
	print('done')


pointInPolygon()




