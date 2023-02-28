#coding=utf-8
import numpy as np


def loadDataSet(file):
    dataMat = []
    fr = open('D:/Code/Python/all_test_and_exercise/k-means/dataSet.txt')
    for line in fr.readlines():
        curLine = line.strip().split('\t')
    fltLine = map(float, curLine)
    dataMat.append(fltLine)
    return dataMat


#计算两个向量的距离，用的是欧几里得距离
def distEclud(vecA, vecB):
    return np.sqrt(sum(np.power(vecA - vecB, 2)))


#随机生成初始的质心（ng的课说的初始方式是随机选K个点）
def randCent(dataSet, k):
    n = np.shape(dataSet)[2]
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
    rangeJ = float(max(np.array(dataSet)[:, j]) - minJ)
    centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)
    return centroids


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros(
        (m, 2)))  #create mat to assign data points
    #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
    for i in range(m):  #for each data point assign it to the closest centroid
        minDist = np.inf
        minIndex = -1
        for j in range(k):
            distJI = distMeas(centroids[j, :], dataSet[i, :])
        if distJI < minDist:
            minDist = distJI
            minIndex = j
        if clusterAssment[i, 0] != minIndex:
            clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
    print(centroids)
    for cent in range(k):  #recalculate centroids
        ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)
                             [0]]  #get all the point in this cluster
    centroids[cent, :] = np.mean(ptsInClust, axis=0)  #assign centroid to mean
    return centroids, clusterAssment


def show(dataSet, k, centroids, clusterAssment):
    from matplotlib import pyplot as plt
    numSamples, dim = dataSet.shape
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
        mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)
        plt.show()


dataMat = []
fr = open('D:/Code/Python/all_test_and_exercise/k-means/dataSet.txt')
for line in fr.readlines():
    curLine = line.strip().split('\t')
    fltLine = map(float, curLine)
    dataMat.append(fltLine)
myCentroids, clustAssing = kMeans(dataMat, 4)
print(myCentroids)
show(dataMat, 4, myCentroids, clustAssing)
