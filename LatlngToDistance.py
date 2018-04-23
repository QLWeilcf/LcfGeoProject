#coding=utf-8

#Latitude & longitude to distance 
from math import cos,sqrt,pi
def latlngToDis1(poiA,poiB):
    #输入为两个点，元组或列表 [经度，纬度] 浮点数
    #输出单位为km   1° ==>111km
    p_a=checkLatOrder(poiA)
    p_b=checkLatOrder(poiB)
    lat=111*abs(p_a[1]-p_b[1])  #纬度距离差
    mus_lng=abs(p_a[0]-p_b[0])
    lng=111*cos(mus_lng*pi/180)
    
    return sqrt(lat**2+lng**2)
    
def latlngToDis2(poiA,poiB):
    p_a=checkLatOrder(poiA)
    p_b=checkLatOrder(poiB)
    mus_lat=abs(p_a[1]-p_b[1])
    dis=111.3195*sqrt(mus_lat**2+(p_a[0]-p_b[0])**2*(cos(mus_lat/2))**2)
    
    return dis
    
    
def checkLatOrder(point):
    #输入一个二元数组；返回经纬度顺序
    if (point[1]>90 and point[0]>90):
        return [0,0] #输入本身不合法
    if (point[1]>90):
        return [point[1],point[0]]
    return point
from math import cos,sin,asin,sqrt,pi

def latlngToDis(poiA,poiB):
    
    #对于a，b的顺序不敏感
    p_a=checkLatOrder(poiA)
    p_b=checkLatOrder(poiB)
    radpa=poiA[1]*pi/180
    radpb=poiB[1]*pi/180
    mlat=radpa-radpb
    mlng=poiA[0]*pi/180-poiB[0]*pi/180
    res=2*asin(sqrt(sin(mlat/2)**2+cos(radpa)*cos(radpb)*(sin(mlng/2)**2)))
    return res*6378.137
    
    
    #写法还值得优化
#[在线验证](http://www.storyday.com/wp-content/uploads/2008/09/latlung_dis.html)
#参考资料：1，[距离换算](http://www.cnblogs.com/zhoug2020/p/3950933.html)
#还有经纬度的 度分秒改为小数写法；
	
	
a1=[116.318849,39.997952]
b1=[116.31884365936072, 39.99794559510289]
latlngToDis(a1,b1)  #在线工具计算得输出为0.8m 差距在0.1米（当然可能不同地方产生的误差不同）
#并且现在发现两个不同的在线工具结果不同；需要结合arcgis进一步确认。
