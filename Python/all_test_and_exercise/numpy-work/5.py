from scipy.optimize import leastsq
import numpy as np
a = []
b = [[] for j in range(306)]
file = 'train.txt'
with open(file,'r',encoding='utf-8') as f:
    data_list = list(map(lambda l: l.strip(), f.readlines()))
    for i in range(306):
        a.append(data_list[i].replace(' ',':').split(':'))
    for j in range(306):
        for i in range(0,27,2):
            b[j].append(float(a[j][i]))
def hw(x, w):
    s = 0
    for i in range(13):
        s += x[i]*w[i]
    return s
def fw(w, y, x):
    a = 0
    for i in range(306):
        a += (hw(x[i], w)-y)**2
    return (1/2)*a
k = []
l = []
for j in range(306):
    k.append(b[j][0])
    l.append(b[j][1:])
k = np.array(k)
l = np.array(l)
w = [0 for i in range(13)]
w = np.array(w)
m = leastsq(fw, w, args=(k, l), maxfev=500000)
print(m[0])