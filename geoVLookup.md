
**地理学的一些vlookup功能**


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


- [x] cinemaLookup()
```
'''
循环电影院的表(c_path)，这个表只需要跑一次，所以用csv读(或pd读)
获取每一行的百度坐标，去找美团电影院的表，做geoVLookup，
满足坐标条件，将美团评分加到c_path里(写入新表)
#['name','mins','avgpri','gcjlng','gcjlat','bdlng','bdlat','score','adds','','','','','']
'''

#import pandas
def cinemaLookup():
	c_path='./guangzhou_cinema_poi_bd092.csv'
	look_path='./美团电影院评价_guangzhouTrue.csv'
	c_out='./guangzhou_cinema_poi_bd09.csv'
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

- [x] geovlookup5()
```
'''
满足坐标条件则更新cin中某一特定列的内容，
内容从look表里拿；(本来是想加入新列，也不难改)
'''
def geovlookup5():
    cin='F:/DigitalCityData/beijing_secondarySchool_v522.csv'
    cout='F:/DigitalCityData/beijing_secondarySchool_v523.csv'
    look_path='D:/coordConvert_out.csv' #从中查数据的表
    #统一用csv读写
    lc=[0,1,2] #score表 look_path 加的数据，lng lat
    cn=[7,4,5] #vlook 加的位置，lng lat
    lst=csvTotdArray(look_path,False) #统一对二维数组进行循环
    
    with open(cout,'a+') as wf:
        w=0
        with open(cin,'r') as rf:
            for line in csv.reader(rf):
                if w==0:
                    wf.write(listToStr(line)) #标题影响
                    w=1
                    continue
                outline=line[:] #深复制
                for j in lst:
                    c1=[line[cn[1]],line[cn[2]]] #[lng,lat]
                    c2=[j[lc[1]],j[lc[2]]]
                    if categrizeByCoord(c1,c2,threshold=0.0025):
                        outline[cn[0]]=outline[cn[0]]+'_'+j[lc[0]]
                wf.write(listToStr(outline)) 

```
- [x] geovlookup7()

```
'''
对两个表进行去重，如果cin的表中有和look表中名称相同
且满足一定坐标条件的值，删掉该行；(目前通过写入新表不写重复行实现)
'''
def geovlookup7(t='金融',ik=0):
    city=['beijing','guangzhou','hangzhou','nanjing','shanghai','shenzhen','tianjin','wuhan']
    tin='city_c_{t}公司_{ct}.csv'.format(t=t,ct=city[ik])
    cin = './CityCutSplitDone/'+tin #打开文件的路径
    cout = './CITYcompany/'+tin   #.replace('_c_', '_k_')  #输出路径
    look_path = './city_c_文化公司_{ct}.csv'.format(ct=city[ik])  # 从中对照的表

    lst = csvTotdArray(look_path, False)

    with open(cout, 'a+') as wf:
        w = 0

        with open(cin, 'r') as rf:
            for line in csv.reader(rf):
                kw = 0
                if w == 0:
                    wf.write(listToStr(line))  # 标题影响
                    w = 1
                    continue
                outline = line[:]  # 深复制
                for j in lst: 
                    if line[1] == j[1]:
                        kw=1 #存在相同的情况
                        break
                if kw==0:
                    wf.write(listToStr(outline))


```


