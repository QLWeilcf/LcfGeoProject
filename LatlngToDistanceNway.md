# 经纬度转距离的n种方式
*包括验证方式*

## 代码实现类

### Python
```python
def xyTodis(d1,d2):
    #经纬度算距离
    #d1[lng,lat]
    start_lat=d1[1]
    start_lng=d1[0]
    end_lat = d2[1]
    end_lng = d2[0]
    lat1 = (math.pi / 180) * float(start_lat)
    lat2 = (math.pi / 180) * float(end_lat)
    lon1 = (math.pi / 180) * float(start_lng)
    lon2 = (math.pi / 180) * float(end_lng)
    R = 6371 #地球半径
    dist = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1)
                         * math.cos(lat2) * math.cos(abs(lon2 - lon1))) * R*1000

    return dist
```

```
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

def checkLatOrder(point):
    #输入一个二元数组；返回经纬度顺序
    if (point[1]>90 and point[0]>90):
        return [0,0] #输入本身不合法
    if (point[1]>90):
        return [point[1],point[0]]
    return point

```





### R


## 调用API类


## 在线计算
- [在线验证1](http://www.storyday.com/wp-content/uploads/2008/09/latlung_dis.html)


## 测试用例


### 参考资料
1，[距离换算](http://www.cnblogs.com/zhoug2020/p/3950933.html)
