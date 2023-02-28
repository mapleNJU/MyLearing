import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs
 
X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3, 3, 3], [0, 0, 0], [1, 1, 1], [2, 2, 2]],cluster_std=[0.2, 0.1, 0.2, 0.2], random_state=9)
 
pca = PCA(n_components=2)
pca.fit(X)

print(pca.explained_variance_)
print(pca.components_)
X_new = pca.transform(X)
print(X_new)
fig = plt.figure()
plt.scatter(X_new[:, 0], X_new[:, 1], marker='o')
plt.show()