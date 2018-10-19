## 地理数据交换
*（注意坐标系统、投影方式）*
包括：地理数据常用格式、地理数据的获取，各种格式之间的转换。
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
- [osm-and-geojson](https://github.com/aaronlidman/osm-and-geojson) Converts OSM XML to GeoJSON; [geojson2osm](https://github.com/Rub21/geojson2osm) & [geojsontoosm](https://github.com/tyrasd/geojsontoosm)
### 数据获取

#### GIS

- [GADM Data](https://gadm.org/download_country_v3.html)
- http://www.opengis.net/kml/2.2

#### RS

- [地理空间数据云](http://www.gscloud.cn/) 有较全的LANDSAT系列数据；
- [遥感免费数据源合集](https://rs-freedatasource.readthedocs.io/zh_CN/latest/) 包含Landsat、MODIS、Sentinel、CBERS等遥感数据源的下载方法和预处理过程


### API

### 在线工具
- [mapshaper.org/](http://mapshaper.org/) 支持shp、geojson、topojson、csv、dbf文件的导入和导出（可以拿来当格式转换工具，并且还有一个非常重要的功能是简化数据（多边形边界简化））
- [geojson.io](http://geojson.io/#map=11/40.8424/116.6185)支持shp、geojson、topojson、kml、csv、WKT的导出（一般我是把geojson传进去导出kml）




