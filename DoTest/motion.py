import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# 准备训练数据
train_texts = ['这个东西不错', '那个东西很好', '这个商品很棒', '那个产品非常好']
train_labels = [1, 1, 1, 0]

# 准备测试数据
test_texts = ['这个产品很好用', '那个东西非常实用']
test_labels = [1, 0]

# 特征选择
vectorizer = CountVectorizer()
train_features = vectorizer.fit_transform(train_texts)
test_features = vectorizer.transform(test_texts)

# 训练模型
clf = MultinomialNB()
clf.fit(train_features, train_labels)

# 预测结果
predictions = clf.predict(test_features)
print(predictions)
