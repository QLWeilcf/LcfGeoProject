import requests
from PIL import Image
import numpy as np

def getOneUrl(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print(111)
        return -1  #页面没正常下下来



url="http://api.map.baidu.com/staticimage/v2?ak=sbyWciweqv78BbudKs3LYFVf5uY8nEDc" \
    "&mcode=666666&center=116.403874,39.914888&width=200&height=200&copyright=1&zoom=17"

#a=getOneUrl(url)

#print(type(a))





'''
chengdu:
左下角：103.801536,30.389814
右上角：104.299382,30.836448

http://online3.map.bdimg.com/tile/?qt=tile&x=22568&y=6898&z=17&styles=pl&scaler=1&udt=20180601
http://online4.map.bdimg.com/tile/?qt=tile&x=22676&y=7008&z=17&styles=pl&scaler=1&udt=20180601

'''

def urlToImg():
    url = "http://api.map.baidu.com/staticimage/v2?ak=sbyWciweqv78BbudKs3LYFVf5uY8nEDc" \
          "&mcode=666666&center=116.403874,39.914888&width=200&height=200&copyright=1&zoom=17"
    r=requests.get(url)
    with open("D:/选区模型/beijing02.png",'ab') as pngf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pngf.write(chunk)
                pngf.flush()

def savePngByXYZ(url,x,y,z=17):
    r = requests.get(url)
    sname="D:/选区模型/chengdu2/cd_{y}_{x}.png".format(x=x,y=y)
    with open(sname, 'ab') as pngf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pngf.write(chunk)
                pngf.flush()

def getTileByXYZ():
    z=17   #成都[[22568,22678],[6897,7009]]
    xidx=[22568,22678]
    yidx=[6897,7009]
    for y in range(yidx[0], yidx[1] + 1):
        for x in range(xidx[0], xidx[1] + 1):
            url="http://online3.map.bdimg.com/tile/?qt=tile&x={x}&y={y}&z=17&styles=pl" \
                "&scaler=1&udt=20180601".format(x=x,y=y)
            savePngByXYZ(url, x, y, z)
        print(y)

import os
import glob
def complieImg():
    #命名规则：cd_x_y.png 左下坐标系
    #同一个x 同1列，y增加，图片在上面
    #假设输入排好序了

    p = "D:/选区模型/chengduImg" #chengduImg
    plst = glob.glob(os.path.join(p, '*.png'))

    xmin=((plst[0].split("\\")[1]).split(".")[0]).split('_')[1]
    alst=[] #3维
    qlst=[]
    for f in plst:
        w=((f.split("\\")[1]).split(".")[0]).split('_') #['cd', '22568', '6898']
        w[0] = f
        if w[1]==xmin:
            qlst.append(w.copy())
        else:
            alst.append(qlst.copy())
            xmin=w[1]
            qlst=[]
    m2 = [256*len(alst[0]), 256 * len(alst)]
    #im2=Image.new('RGBA', (m2[0], m2[1]))
    print(m2)
    psave = "D:/选区模型/complexLevel"
    iw=0
    for k in alst:#k里面装的是x相同的值，y应该递增
        plen=len(k)
        #print(k[0])
        msize = [256, 256 * (plen+1)]
        print(msize)
        toImage = Image.new('RGBA', (msize[0], msize[1]))
        for i in range(plen):
            fromImage = Image.open(k[plen - i - 1][0])
            toImage.paste(fromImage, (0 * msize[0], i * msize[0]))

        #print(k[0])
        sname="/m_{x}.png".format(x=k[0][1])
        iw+=1
        #im2.paste(toImage)
        toImage.save(psave+sname)

    #im2.save(psave  + '/chengduMap.png')
    # 还是应该循环两次


def complieImgInY():
    #命名规则：cd_x_y.png 左下坐标系
    #同一个x 同1列，y增加，图片在上面
    #假设输入排好序了

    p = "D:/选区模型/complexLevel" #chengduImg
    plst = glob.glob(os.path.join(p, '*.png'))

    xmin=((plst[0].split("\\")[1]).split(".")[0]).split('_')[1]
    ima21=Image.open(plst[0])
    w=np.array(ima21).shape
    print(w)
    psave = "D:/选区模型"
    plen=len(plst)
    msize = [w[1]*plen/2, w[0]/2]
    print(msize)
    toImage = Image.new('RGBA', (int(msize[0]), int(msize[1])))
    for i in range(plen):
        fromImage = Image.open(plst[i])
        fromImage=fromImage.resize((int(256/2),int(msize[1])), Image.ANTIALIAS)
        toImage.paste(fromImage, (int(i * 256/2), 0))

    #print(k[0])
    sname="/chengduMap02.png"

    toImage.save(psave+sname)

    #im2.save(psave  + '/chengduMap.png')
    # 还是应该循环两次

def resizeImg():
    img="D:/选区模型/chengduMap.png"
    img2=Image.open(img)

    toImage = img2.resize((54*256,56*256), Image.ANTIALIAS)
    toImage.save("D:/选区模型/chengduMap01.png")

def knowImgInfo():
    png="D:/选区模型/testingComplie/cd_22568_6898.png"
    bdimg = np.array(Image.open(png)) #256*256

    print(bdimg.shape)
    
    
    
getTileByXYZ()
