import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import numpy as np
from pyproj import Proj, Transformer

# 1. 打开tif文件
input_tif = "input.tif"
output_tif = "output.tif"
src_crs = "EPSG:32650"
dst_crs = "EPSG:4326"

# 2. 将tif文件的坐标从UTM的EPSG：32650转换为经纬度坐标
with rasterio.open(input_tif) as src:
    transform, width, height = calculate_default_transform(src.crs, dst_crs, src.width, src.height, *src.bounds)
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': dst_crs,
        'transform': transform,
        'width': width,
        'height': height
    })

    with rasterio.open(output_tif, 'w', **kwargs) as dst:
        for i in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=Resampling.nearest)

# 3. 确认经纬度区域和每个格点的经纬度坐标
with rasterio.open(output_tif) as src:
    # 获取经纬度范围
    print("经纬度区域：", src.bounds)

    # 获取经纬度网格
    cols, rows = np.meshgrid(np.arange(src.width), np.arange(src.height))
    x_coords, y_coords = src.xy(rows, cols, offset='center')
    print("每个格点的经纬度坐标：")
    print(np.column_stack((x_coords.flatten(), y_coords.flatten())))
