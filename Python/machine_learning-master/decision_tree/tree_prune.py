import decision_tree.tools as tools
import numpy as np


def is_tree(obj):
    """判断是否是树"""
    return isinstance(obj, dict)


def get_mean(tree):
    """返回树的平均值"""
    if is_tree(tree['right']):
        tree['right'] = get_mean(tree['right'])
    if is_tree(tree['left']):
        tree['left'] = get_mean(tree['left'])

    value = (tree['left'] + tree['right']) / 2.0
    return float('%.2f' % value)


def prune(tree, test_data):
    """对树进行剪枝"""
    # 测试数据为空
    if np.shape(test_data)[0] == 0:
        return get_mean(tree)

    # 切分测试数据
    if is_tree(tree['left']) or is_tree(tree['right']):
        l_set, r_set = tools.bin_split_data_set(test_data, tree['feature'], tree['value'])

        # 递归对左右子树进行剪枝
        if is_tree(tree['left']):
            tree['left'] = prune(tree['left'], l_set)
        if is_tree(tree['right']):
            tree['right'] = prune(tree['right'], r_set)

    # 左右都为叶子结点
    if not is_tree(tree['left']) and not is_tree(tree['right']):
        l_set, r_set = tools.bin_split_data_set(test_data, tree['feature'], tree['value'])

        # 未合并的误差
        error_no_merge = sum(tools.filter_reg_values(l_set) - tree['left'], 2) + sum(
            np.power(tools.filter_reg_values(r_set) - float(tree['right']), 2))
        # 合并左右结点之后的误差
        tree_mean = (tree['left'] + tree['right']) / 2.0
        error_merge = sum(np.power(tools.filter_reg_values(test_data) - tree_mean, 2))

        # 如果合并后误差减小，则进行合并
        if error_merge < error_no_merge:
            print('merging')
            return float('%.2f' % tree_mean)
        else:
            return tree
    else:
        return tree
