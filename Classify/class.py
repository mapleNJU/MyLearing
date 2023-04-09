import numpy as np
import jieba
import re


def PrepareData():
    train_file = "Classify/train.txt"
    test_file = "Classify/test.txt"
    stop_file = "Classify/new_stop.txt"

    test_set_words = []
    train_set_words = []
    pattern = re.compile(r"^(\d+),(.+)$")  #正则以分割标签和文本

    with open(train_file, 'r') as f1:
        train_data = f1.readlines()
        data = [re.match(pattern, x.strip()).groups() for x in train_data]
        temp_labels, train_texts = zip(*data)
        labels = [int(label) for label in temp_labels]
        for text in train_texts:
            train_set_words.append(list(jieba.cut(text)))

    with open(test_file, 'r') as f2:
        test_data = f2.readlines()
        for text in test_data:
            test_set_words.append(
                list(jieba.cut(text))
            )  # 使用 jieba 分词对每行文本进行分词，并将分词结果转化为列表形式,将结果添加到测试集经过分词后的结果列表中

    with open(stop_file, 'r') as f3:
        stop_words = f3.readlines()

    train_word = [[item for item in inner_list if item not in stop_words]
                  for inner_list in train_set_words]
    test_word = [[item for item in inner_list if item not in stop_words]
                 for inner_list in test_set_words]  #根据停用词表去除停用词

    return train_word, labels, test_word


def createVocabList(dataset):  #将所有词去重后，当作词库
    vocabSet = set([])
    for document in dataset:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def words2vec(vocablist, words):
    Vec = np.zeros(len(vocablist))

    for word in words:
        if word in vocablist:
            Vec[vocablist.index(word)] = 1

    return Vec


def Train(TrainMat, TrainLabel):
    TextNum = len(TrainLabel)
    numWords = max([len(words) for words in TrainMat])
    positive_p = sum(TrainLabel) / TextNum
    p0Num = np.zeros(numWords)
    p1Num = np.zeros(numWords)
    p0Denom = 0
    p1Denom = 0
    for i in range(TextNum):
        if TrainLabel[i] == 1:
            p1Num += TrainMat[i]
            p1Denom += sum(TrainMat[i])
        else:
            p0Num += TrainMat[i]
            p0Denom += sum(TrainMat[i])
    p1Vect = np.log((p1Num + 1) / (p1Denom + numWords))  #加1平滑
    p0Vect = np.log((p0Num + 1) / (p0Denom + numWords))
    return p0Vect, p1Vect, positive_p


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):  #比较概率大小进行判断，
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + np.log(1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    Train_text, Train_label, Test_text = PrepareData()
    VocabList = createVocabList(Train_text)
    TrainMat = []
    for postinDoc in Train_text:
        TrainMat.append(words2vec(VocabList, postinDoc))
    p0V, p1V, pAb = Train(np.array(TrainMat), np.array(Train_label))
    segment_list = []
    for item in Test_text:
        thisDoc = np.array(words2vec(VocabList, item))
        segment_list.append(classifyNB(thisDoc, p0V, p1V, pAb))

    # 定义一个文件名，用于保存情感分类结果
    filename = 'Classify/201300066.txt'

    # 将情感分类结果写入到文件中
    with open(filename, 'w') as f:
        # 遍历情感分类结果列表，将每个元素写入文件中，并在元素之间添加换行符
        for sentiment in segment_list:
            f.write(str(sentiment) + '\n')

    print("Success! The positive probability equals ",
          sum(segment_list) / len(segment_list))


if __name__ == '__main__':
    testingNB()