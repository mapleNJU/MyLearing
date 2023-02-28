# -*- coding:utf-8 -*-
import numpy as np


def load_data_set():
    train_data = [[1.0, 2, 3], [1.0, 8, 1], [1.0, 7, 4], [
        1.0, 5, 6], [1.0, 4, 3], [1.0, 2, 9], [1.0, 1, 7]]
    train_label = [25, 41, 53, 55, 34, 58, 43]
    return train_data, train_label


def grad_desc(train_data, train_labels):
    """梯度下降"""
    data_mat = np.matrix(train_data)
    label_mat = np.matrix(train_labels).transpose()
    n = np.shape(data_mat)[1]
    # 步长
    alpha = 0.001
    # 最大循环次数
    max_cycles = 100
    # 初始化回归系数weights
    weights = np.ones((n, 1))
    for index in range(max_cycles):
        h = data_mat * weights-label_mat
        weights = weights - alpha * data_mat.transpose() * h
        # 返回压平的系数数组
    return np.asarray(weights).flatten()


def random_grad_desc(train_data, train_labels):
    """随机梯度下降"""
    data_mat = np.asarray(train_data)
    label_mat = np.asarray(train_labels)
    m, n = np.shape(data_mat)
    # 步长
    alpha = 0.001
    # 初始化回归系数weights
    weights = np.ones(n)
    for i in range(m):
        h = sum(data_mat[i] * weights)-label_mat[i]
        weights = weights - alpha * h * data_mat[i]
    return weights


def advanced_random_grad_desc(train_data, train_labels):
    """随机梯度下降改进"""
    data_mat = np.asarray(train_data)
    label_mat = np.asarray(train_labels)
    m, n = np.shape(data_mat)
    # 步长
    alpha = 0.001
    # 初始化回归系数weights
    weights = np.ones(n)
    max_cycles = 500
    for j in range(max_cycles):
        data_index = list(range(m))
        for i in range(m):
            random_index = int(np.random.uniform(0, len(data_index)))
            h = sum(data_mat[random_index] * weights)-label_mat[random_index]
            weights = weights - alpha * h * data_mat[random_index]
            del data_index[random_index]
    return weights


def test():
    train_data, train_labels = load_data_set()
    weights = advanced_random_grad_desc(train_data, train_labels)
    weights = np.asarray(weights)
    print(weights)


test()
