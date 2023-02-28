import numpy as np
from scipy.optimize import fsolve
from math import cos

def f(x):
    x_0, x_1, x_2 = x.tolist()
    return [3*x_0+1, 4*x_0-2/cos(x_1*x_2), x_1*x_2-3.5]
result = fsolve(f, [0, 0, 0])
print(result)