#导入相关库
import numpy as np
from scipy import optimize as op

#定义决策变量范围
x1 = (0, 1)
x2 = (0, 1)
x3 = (0, 1)
x4 = (0, 1)
x5 = (0, None)  #v

#定义目标函数系数
c = np.array([0, 0, 0, 0, 1])

#定义约束条件系数
A_ub = np.array([[1, -2, 6, -4, -1], [2, -7, 2, 4, -1], [-3, 4, -4, -3, -1],
                 [-8, 3, -2, 3, -1]])
B_ub = np.array([0, 0, 0, 0])
A_eq = np.array([[1, 1, 1, 1, 0]])
B_eq = np.array([1])

#求解
res = op.linprog(c, A_ub, B_ub, A_eq, B_eq, bounds=(x1, x2, x3, x4, x5))
print(res)