import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1,2,66,-1], [-2,6,58,-1], [-3,8,45,-2], [1,9,36,1], [2,10,62,1], [3,5,83,2]])  #�������ݣ�ά��Ϊ4
pca = PCA(n_components=2)   #����2ά
pca.fit(X)                  #ѵ��
newX=pca.fit_transform(X)   #��ά�������
# PCA(copy=True, n_components=2, whiten=False)
print(pca.explained_variance_ratio_)  #���������
print(newX)                  #�����ά�������