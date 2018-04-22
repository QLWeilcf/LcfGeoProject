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
