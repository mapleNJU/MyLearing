import numpy as np
 
def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float,line) for line in stringArr]
    return np.mat(datArr)
 
def pca(dataMat, topNfeat=999999):
    meanVals = np.mean(dataMat, axis=0)
    DataAdjust = dataMat - meanVals           #减去平均值
    covMat = np.cov(DataAdjust, rowvar=0)
    eigVals,eigVects = np.linalg.eig(np.mat(covMat)) #计算特征值和特征向量
    #print eigVals
    eigValInd = np.argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]   #保留最大的前K个特征值
    redEigVects = eigVects[:,eigValInd]        #对应的特征向量
    lowDDataMat = DataAdjust * redEigVects     #将数据转换到低维新空间
    reconMat = (lowDDataMat * redEigVects.T) + meanVals   #重构数据，用于调试
    return lowDDataMat, reconMat