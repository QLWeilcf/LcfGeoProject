## 地理数据交换
*（注意坐标系统、投影方式）*

### 主流数据类型
（部分参考自[awesome-gis](https://github.com/sshuair/awesome-gis#data-format)）

- Shp
   - e00
- kml  -> OSM
- geojson
- dxf
- gpx


- geotiff
- img
- ENVI hdr


### 代码转换

**I try**：
- [geojson2kml in C#]()

**others excellent project**

- [kml2geojson in Python](https://github.com/mrcagney/kml2geojson)
- [osmtogeojson in js(node)](https://github.com/tyrasd/osmtogeojson)
- [osm-and-geojson](https://github.com/aaronlidman/osm-and-geojson) Converts OSM XML to GeoJSON
### 数据获取

#### GIS

- [GADM Data](https://gadm.org/download_country_v3.html)


#### RS

- [地理空间数据云](http://www.gscloud.cn/) 有较全的LANDSAT系列数据；

### API

### 在线工具
- [mapshaper.org/](http://mapshaper.org/) 支持shp、geojson、topojson、csv、dbf文件的导入和导出
- [geojson.io](http://geojson.io/#map=11/40.8424/116.6185)支持shp、geojson、topojson、kml、csv、WKT的导出（一般我是把geojson传进去导出kml）




