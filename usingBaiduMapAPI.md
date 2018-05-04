

*百度地图API的一些学习记录*；包括JS的API和WebAPI，可视化会对于echarts的内容；单纯调用API的可视化会比较少；


## Web API
参考：[webapi](http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi)

```python
import json
import time
def parseBaiduJson4():
	for i in range(1,25):
		u3="http://api.map.baidu.com/place/v2/search?query=超市" \
	   "&bounds=39.830322,116.133196,40.113428,116.647171" \
	   "&output=json&page_size={psize}&page_num={pnum}&ak=yourkey".format(psize="10",pnum=str(i))
		text=getOneUrl(u3) #该函数就是用request库取下页面（json）
		jt=json.loads(text)
		print(len(jt["results"]))
		#print(jt["results"])

		jtxt=jt["results"] #dict
		savep = './超市输出bd09_01.csv'
		with open(savep,'a+',encoding="utf-8") as f:
			for ec in jtxt:
				wtxt=str(ec["name"])+','+str(ec["location"]["lat"])+','+str(ec["location"]["lng"])+','+str(ec["address"])
				f.write(wtxt + '\n')
		time.sleep(2) #百度API对个人用户访问有一定并行限制，所以需要sleep
	print('done')

def parseBaiduJson5(iquery,ibuds,savep):
    #param : 查询内容，如超市；边界 保存路径
    i=1
    ikey="yourkey"
    while (i<100): #100为可变阈值，一般不会超过100
        u3="http://api.map.baidu.com/place/v2/search?query={query}" \
        "&bounds={buds}" \
        "&output=json&page_size={psize}" \
        "&page_num={pnum}&ak={key}".format(query=iquery,buds=ibuds,psize="10",pnum=str(i),key=ikey)
        text=getOneUrl(u3)
        jt=json.loads(text)
        jlen=len(jt["results"])
        print(jlen)
        if jlen==0:
            break
        jtxt=jt["results"] #dict
        with open(savep,'a+',encoding="utf-8") as f:
            for ec in jtxt:
                wtxt=str(ec["name"])+','+str(ec["location"]["lat"])+','+str(ec["location"]["lng"])+','+str(ec["address"])
                f.write(wtxt + '\n')
        i+=1
        time.sleep(2) #百度API对个人用户访问有一定并行限制，所以需要sleep
    print('done;save at ',savep)
parseBaiduJson4()
```



