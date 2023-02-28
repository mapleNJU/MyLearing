import numpy as np
from decision_tree.tree_prune import prune
from decision_tree.tools import bin_split_data_set
from decision_tree.tree_plot import plot
import decision_tree.tools as tools

"""回归树相关方法"""


def load_data_set(file_name):
    """读取数据到列表"""
    data_mat = []
    fr = open(file_name)
    for line in fr.readlines():
        cur_line = line.strip().split(',')
        data_mat.append(cur_line)
    return data_mat


def reg_leaf(data_set):
    """生成叶子结点"""
    # 计算平均值
    result = tools.filter_reg_values(data_set)
    value = np.mean(result)
    return value


def reg_err(data_set):
    """总方差"""
    # np.val 计算标准差
    result = tools.filter_reg_values(data_set)
    return np.var(result) * np.shape(data_set)[0]


def create_tree(data_set, ops=(1, 4)):
    """创建回归树"""
    feat, val = choose_best_split(data_set, ops)
    if feat is None:
        return val
    ret_tree = dict()
    ret_tree['feature'] = feat
    ret_tree['value'] = val

    # 左右子树
    left_data, right_data = bin_split_data_set(data_set, feat, val)
    ret_tree['left'] = create_tree(left_data, ops)
    ret_tree['right'] = create_tree(right_data, ops)

    return ret_tree


def flatten(l):
    """将多位数组压平到一维数组"""
    for k in l:
        if not isinstance(k, (list, tuple)):
            yield k
        else:
            yield from flatten(k)


def choose_best_split(data_set, ops=(1, 4)):
    """
        选取最好的划分特征值
        data_set:数据集
        ops(x,y):x--误差减少最小值  y--分类后样本最少个数
    """
    tols = ops[0]
    toln = ops[1]

    # 所有分类相同（mat.flatten()  将矩阵数据压平）
    if len(set(np.array(data_set[:, -1].flatten()[0])[0])) == 1:
        return None, reg_leaf(data_set)

    m, n = np.shape(data_set)
    s = reg_err(data_set)

    # np.inf 无限大的数
    best_s = np.inf
    best_index = 0
    best_value = 0

    # 遍历每一个特征
    for feat_index in range(n - 1):
        # 遍历当前特征的所有值
        for value in set(flatten(np.array(data_set)[:, feat_index])):
            mat0, mat1 = bin_split_data_set(data_set, feat_index, value)
            # 分类后样本个数较少，则退出本次循环
            if np.shape(mat0)[0] < toln or np.shape(mat1)[0] < toln:
                continue
            # 计算新的误差
            new_s = reg_err(mat0) + reg_err(mat1)

            # 更新最小误差
            if new_s < best_s:
                best_index = feat_index
                best_value = value
                best_s = new_s

    # 如果误差减小不大，则退出
    if s - best_s < tols:
        return None, reg_leaf(data_set)

    # 如果切片分出的数据集很小，就退出
    mat0, mat1 = bin_split_data_set(data_set, best_index, best_value)
    if mat0.shape[0] < toln or mat1.shape[0] < toln:
        return None, reg_leaf(data_set)

    return best_index, best_value


def change(node, labels):
    """改变树的样子用于显示"""
    if isinstance(node, dict):
        name = str(labels[node['feature']]) + "=" + str(node['value'])
        name = name.strip()
        new_dict = {}
        new_dict[name] = {}
        new_dict[name]['1'] = change(node["left"], labels)
        new_dict[name]['0'] = change(node["right"], labels)
        return new_dict
    else:
        return node


def test():
    train_data = np.mat(load_data_set('data/reg_train_data.txt'))
    my_tree = create_tree(train_data, ops=(1, 2))
    print(my_tree)
    test_data = np.mat(load_data_set('data/reg_test_data.txt'))
    # 剪枝
    prune_tree = prune(my_tree, test_data)

    labels = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'Y1']
    new_dict = change(prune_tree, labels)
    # 绘图
    plot(new_dict)


test()
