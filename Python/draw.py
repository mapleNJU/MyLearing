from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

x_axis_data = [0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 1.0]
y_axis_data = [0.25, 0.5, 0.5, 0.75, 0.75, 1.0, 1.0, 1.0]

plt.plot(x_axis_data,
         y_axis_data,
         'ro-',
         color='black',
         alpha=0.8,
         linewidth=1)

plt.legend(loc="upper right")

plt.xlabel('FPR')
plt.ylabel('TPR')

plt.show()