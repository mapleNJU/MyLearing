# _*_ coding:utf-8 _*_
import numpy as np
import re
import pandas as pd
import jieba


def loadDataSet():  #创建样例数据
    file_path = "Classify/train.txt"

    with open(file_path, "r") as f:
        data = f.readlines()

    pattern = re.compile(r"^(\d+),(.+)$")  #正则以分割标签和文本
    data = [re.match(pattern, x.strip()).groups() for x in data]
    labels, texts = zip(*data)
    new_labels = [int(label) for label in labels]

    seg_list = []

    for text in texts:
        seg_list.append(list(jieba.cut(text)))

    return seg_list, new_labels


def createVocabList(dataSet):  #创建词库 这里就是直接把所有词去重后，当作词库
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList,
                   inputSet):  #文本词向量。词库中每个词当作一个特征，文本中就该词，该词特征就是1，没有就是0
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = np.ones(numWords)  #防止某个类别计算出的概率为0，导致最后相乘都为0，所以初始词都赋值1，分母赋值为2.
    p1Num = np.ones(numWords)
    p0Denom = 2
    p1Denom = 2
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num / p1Denom)  #这里使用了Log函数，方便计算，因为最后是比较大小，所有对结果没有影响。
    p0Vect = np.log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):  #比较概率大小进行判断，
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + np.log(1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():

    test_set_words = []
    with open("Classify/test.txt", 'r') as f2:
        for line in f2:
            # 使用 jieba 分词对当前行文本进行分词，并将分词结果转化为列表形式
            words = list(jieba.cut(line.strip()))
            # 将分词结果添加到测试集经过分词后的结果列表中
            test_set_words.append(words)

    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(np.array(trainMat), np.array(listClasses))
    segment_list = []
    for item in test_set_words:
        thisDoc = np.array(setOfWords2Vec(myVocabList, item))
        segment_list.append(classifyNB(thisDoc, p0V, p1V, pAb))

    # 定义一个文件名，用于保存情感分类结果
    filename = 'Classify/sentiment_result.txt'

    # 将情感分类结果写入到文件中
    with open(filename, 'w') as f:
        # 遍历情感分类结果列表，将每个元素写入文件中，并在元素之间添加换行符
        for sentiment in segment_list:
            f.write(str(sentiment) + '\n')


if __name__ == '__main__':
    testingNB()