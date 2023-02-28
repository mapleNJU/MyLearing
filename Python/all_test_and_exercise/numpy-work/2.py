import numpy as np
import matplotlib.pyplot as plt

"""
����˵���������ı�����

Parameters:
filename - �ļ���
delim - ÿһ�в�ͬ��������֮��ķָ���ʽ��Ĭ����tab����\t��

Returns:
j��float������ֵ�б�ת��Ϊ���󷵻�

"""
def loadDataSet(filename, delim='\t'):
    fr = open(filename)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [list(map(float, line)) for line in stringArr]
    return np.mat(datArr)


"""
����˵����PCA����ά��ѹ������

Parameters:
dataMat - ���ݼ�����
topNfeat - ��Ҫ����������ά�ȣ���Ҫѹ���ɵ�ά������Ĭ��4096

Returns:
lowDDataMat - ѹ��������ݾ���
reconMat - ѹ��������ݾ��󷴹���ԭʼ���ݾ���

"""
def pca(dataMat, topNfeat=4096):
    # �����ÿһ�еľ�ֵ
    meanVals = np.mean(dataMat, axis=0)
    # ���ݾ���ÿһ��������ȥ����������ֵ
    meanRemoved = dataMat - meanVals
    # ����Э������󣬴���n-1��Ϊ�˵õ�Э�������ƫ����
    # cov(x, 0) = cov(x)������n-1(nΪ��������)
    # cov(x, 1)������n
    covMat = np.cov(meanRemoved, rowvar=0)
    # ����Э������������ֵ����Ӧ����������
    # ����������Ӧ�ľ�����
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    # sort():������ֵ��������(��С����)
    # argsort():���������������С�������򣬷��ض�Ӧ����������
    eigValInd = np.argsort(eigVals)
    # �������ľ������һ����ʼ���¶���ѡȡ����N������ֵ���������Ӧ������
    eigValInd = eigValInd[: -(topNfeat+1): -1]
    # ������ֵ����N������ֵ��Ӧ����������������ȡ���������ѹ������
    redEigVects = eigVects[:, eigValInd]
    # ��ȥ����ֵ��ľ���*ѹ������ת�����µĿռ䣬ʹά�Ƚ���ΪN
    lowDDataMat = meanRemoved * redEigVects
    # ���ý�ά��ľ��󷴹���ԭ���ݾ���(�������ԣ��ɸ�δѹ����ԭ����ȶ�)
    # �˴���ת�ú���Ľ��һ��redEigVects.I
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    print(reconMat)
    # ����ѹ��������ݾ��󼰸þ��󷴹���ԭʼ���ݾ���
    return lowDDataMat, reconMat


if __name__ == '__main__':
    dataMat = loadDataSet('����.txt')
    lowDmat, reconMat = pca(dataMat, 1)
    print(np.shape(lowDmat))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:, 0].flatten().A[0], dataMat[:, 1].flatten().A[0], marker='^', s=90)
    ax.scatter(reconMat[:, 0].flatten().A[0], reconMat[:, 1].flatten().A[0], marker='o', s=90, c='red')
    plt.show()