import numpy as np

def get_centered_submatrix(matrix, x, y, size=15):
    # 计算子矩阵的边界
    half_size = size // 2
    x_start = x - half_size
    x_end = x + half_size + 1
    y_start = y - half_size
    y_end = y + half_size + 1

    # 初始化全为 0 的子矩阵
    submatrix = np.zeros((size, size), dtype=matrix.dtype)

    # 计算原始矩阵中有效区域的边界
    x_slice_start = max(x_start, 0)
    x_slice_end = min(x_end, matrix.shape[0])
    y_slice_start = max(y_start, 0)
    y_slice_end = min(y_end, matrix.shape[1])

    # 计算子矩阵中有效区域的边界
    sub_x_slice_start = max(0, -x_start)
    sub_x_slice_end = size - max(0, x_end - matrix.shape[0])
    sub_y_slice_start = max(0, -y_start)
    sub_y_slice_end = size - max(0, y_end - matrix.shape[1])

    # 从原始矩阵中提取有效区域并将其复制到子矩阵中
    submatrix[sub_x_slice_start:sub_x_slice_end, sub_y_slice_start:sub_y_slice_end] = matrix[x_slice_start:x_slice_end, y_slice_start:y_slice_end]

    return submatrix

# 示例
matrix = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
x, y = 95,95
print(matrix)
print(matrix[88:100,88:100])
centered_submatrix = get_centered_submatrix(matrix, x, y, size=15)
print("以位置 ({}, {}) 为中心的 15x15 子矩阵：\n{}".format(x, y, centered_submatrix))
