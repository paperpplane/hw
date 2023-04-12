import numpy as np

def find_closest_point(matrix, a, b):
    # 将矩阵转换为坐标点的形式
    coordinates = matrix.transpose(1, 2, 0).reshape(-1, 2)

    # 计算给定点与矩阵中每个点的欧氏距离
    distances = np.sqrt(np.sum((coordinates - np.array([a, b]))**2, axis=-1))

    # 找到距离最小的点的索引
    closest_point_index = np.argmin(distances)

    # 返回距离最小的点的 x 和 y 坐标
    closest_point = coordinates[closest_point_index]

    # 将索引转换回矩阵中的位置
    matrix_position = np.unravel_index(closest_point_index, matrix.shape[1:])

    return closest_point, matrix_position

matrix = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
a, b = 3.5,4

closest_point, matrix_position = find_closest_point(matrix, a, b)
print("与点 ({}, {}) 最接近的点为: ({}, {})，在矩阵中的位置为: {}".format(a, b, closest_point[0], closest_point[1], matrix_position))
