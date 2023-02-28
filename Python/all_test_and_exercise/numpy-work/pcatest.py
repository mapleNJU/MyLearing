import numpy as np
 
def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float,line) for line in stringArr]
    return np.mat(datArr)
 
def pca(dataMat, topNfeat=999999):
    meanVals = np.mean(dataMat, axis=0)
    DataAdjust = dataMat - meanVals           #��ȥƽ��ֵ
    covMat = np.cov(DataAdjust, rowvar=0)
    eigVals,eigVects = np.linalg.eig(np.mat(covMat)) #��������ֵ����������
    #print eigVals
    eigValInd = np.argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]   #��������ǰK������ֵ
    redEigVects = eigVects[:,eigValInd]        #��Ӧ����������
    lowDDataMat = DataAdjust * redEigVects     #������ת������ά�¿ռ�
    reconMat = (lowDDataMat * redEigVects.T) + meanVals   #�ع����ݣ����ڵ���
    return lowDDataMat, reconMat