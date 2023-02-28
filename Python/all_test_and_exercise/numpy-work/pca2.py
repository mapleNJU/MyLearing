import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3, 3, 3], [0, 0, 0], [1, 1, 1], [2, 2, 2]],cluster_std=[0.2, 0.1, 0.2, 0.2], random_state=9)

fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
plt.scatter(X[:, 0], X[:, 1], X[:, 2], marker='o')
plt.show()
eigvalue, eigvector = np.linalg.eig(np.cov(X.T))
print("特征值:\n",eigvalue,"\n特征值向量:\n",eigvector)
a = np.hstack((eigvector[:, 0].reshape(3, -1), eigvector[:, -1].reshape(3, -1)))
print("两个合适的特征向量构成的矩阵:\n",a)#第一个和第三个特征向量构成的矩阵
X = X - X.mean(axis=0)
X_new1 = X.dot(a)
print("降维后的结果:\n",X_new1)#降维后的结果
fig = plt.scatter(X_new1[:, 0], X_new1[:, 1], marker='o')
plt.show()