
**地理学的一些vlookupg功能**







## py-根据坐标比对


```
# 公用代码
def categrizeByCoord(c1,c2,threshold=0.0475):
    #要求是同一坐标系
    d1=abs(c1[0]-c2[0])
    d2=abs(c1[1]-c2[1])
    if (d1<threshold and d2<threshold):
        return True
    return False
    
def csvTotdArray(csv_path):
    import csv
    cdata = csv.reader(open(csv_path,'r',encoding='utf-8'))
    lst = []
    for i in cdata:  # type(i)-->list
        lst.append(i)

    return lst[1:] #去掉标题行，如果不需去掉就直接写 lst

def arrayToCsv(arr,spath): #二维数组写入csv 不用pandas
    with open(spath,'w', newline='') as sf:
        filewriter = csv.writer(sf, delimiter=',')
        for line in arr:
            filewriter.writerow(line)
	    
def listToStr(lst,w=','): #列表变一行csv  后面的 \n 看情况放
    return w.join(lst)+'\n'
```
### 应用：


```


'''
循环电影院的表，这个表只需要跑一次，所以用csv读(或pd读)
获取每一行的百度坐标，去找美团电影院的表；做geoVLookup

#['name','mins','avgpri','gcjlng','gcjlat','bdlng','bdlat','score','adds','','','','','']
'''

def cinemaLookup():
	c_path='L:/OtherSys/DigitalCityData/guangzhou_cinema_poi_bd092.csv'
	look_path='H:/DigitalC_data/广州特征图层/美团电影院评价_guangzhouTrue.csv'
	c_out='L:/OtherSys/DigitalCityData/guangzhou_cinema_poi_bd09.csv'
	cinema=pd.read_csv(c_path)
	#cinema =pd.read_excel(c_path)
	lc=[5,6,7] #score表 look_path
	cn=[2,3,6] #vlook
	lst=csvTotdArray(look_path)
	for i in range(len(cinema)):
		c1=[cinema.iloc[i,cn[0]],cinema.iloc[i,cn[1]]]
		for j in lst:
			if categrizeByCoord(c1,[j[lc[0]],j[lc[1]]]):
				cinema.iloc[i, cn[2]]=j[lc[2]]
				break

	cinema.to_csv(c_out,index=False,encoding='gbk')

```



