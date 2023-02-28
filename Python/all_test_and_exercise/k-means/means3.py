from sklearn.cluster import KMeans
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt
 
data = np.random.rand(1000,2)#随机生成一个1000*2的矩阵，作为数据集
estimator=KMeans(n_clusters=3)#此处n_cluster表示簇的个数，即想要分为几类
res=estimator.fit_predict(data)#调用数据
lable_pred=estimator.labels_
centroids=estimator.cluster_centers_
inertia=estimator.inertia_
#print res
print (lable_pred)
print (centroids)
print (inertia)
 
for i in range(len(data)):
  if int(lable_pred[i])==0:
    plt.scatter(data[i][0],data[i][1],color='red')
  if int(lable_pred[i])==1:
    plt.scatter(data[i][0],data[i][1],color='black')
  if int(lable_pred[i])==2:
    plt.scatter(data[i][0],data[i][1],color='blue')
plt.show()