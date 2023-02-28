import numpy as np


def bin_split_data_set(data_set, feature, value):
    """对数据集进行二元切分"""
    # np.nonzero(data_set[:,feature] > value)[0] 返回feture值 大于 value 的行号
    mat0 = data_set[np.nonzero(data_set[:, feature] == value)[0], :]
    mat1 = data_set[np.nonzero(data_set[:, feature] != value)[0], :]
    return mat0, mat1


def filter_reg_values(data_set):
    """过滤矩阵最后一列数据转为 list[float]"""
    result = list(np.array(data_set[:, -1].flatten())[0])
    result = np.array(result, dtype='float_')
    return result
