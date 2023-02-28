import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

def load_data():
    # 以feature, label的形式返回数据集
    feature, label = datasets.load_iris(return_X_y=True)
    print(feature.shape) # (150, 4)
    print(label.shape) # (150,)
    return feature, label

def class_check(label:np.ndarray):
    # check the distribution of class/label
    count0, count1, count2 = 0,0,0
    for i in label: 
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        elif i == 2: 
            count2 += 1
    # return count0/len(label), count1/len(label), count2/len(label)
    return count0, count1, count2

if __name__ == "__main__":
    feature, label = load_data()
    feature_train, feature_test, label_train, label_test = \
        train_test_split(feature, label, test_size=0.2, random_state=0)


    my_nb = GaussianNB()
    my_nb.fit(feature_train, label_train)
    print(my_nb.score(feature_test, label_test))
    
    pro_nb = GaussianNB(priors=(1/3,1/3,1/3))
    pro_nb.fit(feature_train, label_train)
    print(pro_nb.score(feature_test, label_test))

    class0 = np.array([feature_train[i] for i in range(feature_train.shape[0]) if label_train[i] == 0])
    class1 = np.array([feature_train[i] for i in range(feature_train.shape[0]) if label_train[i] == 1])
    class2 = np.array([feature_train[i] for i in range(feature_train.shape[0]) if label_train[i] == 2])

    class_list = [class0, class1, class2]

    # draw histograms
    # fig, axs = plt.subplots(3, 4)
    cases = [
             ["P(x_0 | 0)", "P(x_1 | 0)", "P(x_2 | 0)", "P(x_3 | 0)"], 
             ["P(x_0 | 1)", "P(x_1 | 1)", "P(x_2 | 1)", "P(x_3 | 1)"], 
             ["P(x_0 | 2)", "P(x_1 | 2)", "P(x_2 | 2)", "P(x_3 | 2)"], 
            ]

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)
    plt.rcParams.update({'font.size': 7})

    for i in range(3):
        for j in range(4):
            print(f"{i}, {j}, {4*(i)+(j+1)}")
            plt.subplot(3,4, 4*(i)+(j+1))
            plt.hist(class_list[i][:, j])
            plt.title(f"{cases[i][j]}") #, fontsize=10)
    
    plt.show()

    # print(class0.shape)
    # print(class1.shape)
    # print(class2.shape)
    


