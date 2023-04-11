import rasterio
import numpy as np
from pyproj import Proj, Transformer

input_tif = "input.tif"

# 使用 rasterio 读取tif文件
with rasterio.open(input_tif) as src:
    print("UTM区域：", src.bounds)
    
    cols, rows = np.meshgrid(np.arange(src.width), np.arange(src.height))
    x_coords, y_coords = src.xy(rows, cols, offset='center')
    utm_coords = np.column_stack((x_coords.flatten(), y_coords.flatten()))

    # 创建一个坐标转换器，用于将 UTM (EPSG:32650) 坐标转换为经纬度 (EPSG:4326) 坐标
    transformer = Transformer.from_crs("EPSG:32650", "EPSG:4326")

    # 使用 pyproj 执行坐标转换
    lat, lon = transformer.transform(utm_coords[:, 1], utm_coords[:, 0])

    # 将转换后的经纬度坐标重塑为与原始数据相同的形状
    lons = lon.reshape(src.height, src.width)
    lats = lat.reshape(src.height, src.width)

    print("每个格点的经纬度坐标：")
    print(np.column_stack((lons.flatten(), lats.flatten())))
