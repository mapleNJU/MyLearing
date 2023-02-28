import numpy as np
from scipy.optimize import minimize_scalar
from math import sin, exp
from math import pow
def f(x):
    return -((sin(x-2))**2)*exp(-x**2)
res = minimize_scalar(f)
print(-f(res.x))
def g(mat):
    s = len(mat[0])
    a = np.zeros((s, s))
    p = 0
    for i in range(s):
        for j in range(s):
            for k in range(s):
                p += (int(mat[i][k])-int(mat[j][k]))**2
            p = pow(p, 0.5)
            a[i][j] = '{:0.3f}'.format(p)
            print(a[i][j])
            p = 0
    return a
n = input().split()
n1 = int(n[0])
n2 = int(n[1])
a = []
while n1 > 0:
    a.append(input().split())
    n1 = n1-1
print(g(a))
