import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
import numpy as np
m=15
x=np.random.rand(m)
y=np.random.rand(m)
plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.scatter(x, y)
plt.title("默认情况下")