# NLP第一次实验报告

`201300066 麻超 人工智能学院`

### 作业要求

不使用预训练模型完成文本情感分类

我利用了朴素贝叶斯分类器方法来实现对该文本的情感分类，最后的分类正确率在0.821左右。

运行方法：直接运行`class.py`即可，注意文件路径，其他的文件没有对主体产生影响，其中`compare.py`是我为了验证每一次实验结果和上一次的结果相比有多大的提升而写，`convert.py`是实现了中文词语的简繁转换，`stop.txt`是我从网上下载的停词表，`stop_hk.txt`是我将原分词表转化为繁体并加入一些数字及符号的结果。

### 朴素贝叶斯分类器

朴素贝叶斯分类器是一种基于贝叶斯定理和特征独立假设的分类方法。其基本思想是，对于给定的待分类样本，利用贝叶斯定理求出后验概率最大的类别作为样本的分类。在特征独立假设的条件下，朴素贝叶斯分类器将样本的特征向量看作一个离散随机变量，并用条件概率分布来描述各个特征对于样本分类的影响。具体来说，设样本$x$的特征向量为$x=(x_1,x_2,\cdots,x_n)$，类别集合为$C={c_1,c_2,\cdots,c_k}$，则朴素贝叶斯分类器的决策规则为：
$$
y=\arg \max\limits_{c_i\in C}P(c_i)\prod_{j=1}^n P(x_j|c_i)
$$
其中，$P(c_i)$为类别$c_i$的先验概率，$P(x_j|c_i)$为在类别$c_i$条件下$x_j$特征的条件概率。

在情感分类问题中，$x$通常表示一段文本，$x_j$表示文本中的一个词语，$c_i$表示文本的情感类别，比如正面、负面或中性。对于每个词语，可以根据训练数据计算出其在各个情感类别下的条件概率，从而得到该文本属于各个情感类别的概率，并选择概率最大的类别作为该文本的情感类别。

### 实验过程

在实现利用朴素贝叶斯分类器完成文本分类的过程中，主要有以下几个过程：

* 数据准备：对训练集和测试集进行转换和分词
* 特征提取：基于词袋模型的方法，并且加入停用词过滤，统计每条评论中每个词出现的次数，得到一个特征向量
* 计算后验概率，并且处理可能产生的其他问题，利用朴素贝叶斯算法对特征向量进行分类
* 得到测试集每个文本的可能的概率情况，并写入数据

### 实验细节

在之前几次的实验中，对于训练集的文本处理总是出现bug，我一直以为在python中可以区分中文逗号和英文逗号，但按中文逗号划分每一行文本的文字和标签时总会出现bug，所以我在这里利用了正则表达式处理，以确保对标签和文字的划分总会基于每一行的第一个逗号。

```python
pattern = re.compile(r"^(\d+),(.+)$")
...
data = [re.match(pattern, x.strip()).groups() for x in train_data]
    temp_labels, train_texts = zip(*data)
    labels = [int(label) for label in temp_labels]
```

随后，我利用一个已经比较成熟的中文分词库`jieba`来对中文语料进行分词，其效果较好，使用也非常简单，直接使用`jieba.cut(text)`即可得到一个分词后的列表。

在特征提取方面，我们使用了基于词袋模型的方法，并加入了停用词过滤。首先对所有文本进行分词，并去除停用词。停用词表是我在网上下载的，但是我在利用停用词表测试后，得到结果正确率仅仅从0.818提升到0.819……经过分析之后意识到我下载的是简体的停用词表，于是利用`zhconv`这个库中的`convert`方法将其转为繁体，同时对概率计算进行修正，提高了准确度到0.821。随后，将分词后的结果收集起来，训练集去重后得到的所有词作为词库，在测试过程中，我也尝试了将训练集和测试集合并后得到的词库作为整体词库，但得到的结果与之前相比差距不大，还下降了0.001（也即有一个样本反而错误了）

然后，对于每个样本，统计其中每个词出现的次数，得到一个特征向量。

随后计算条件概率，首先计算整个训练集中正样本出现的概率，再根据条件概率的公式计算测试集中每条样本的后验概率，我们使用了加一平滑来避免出现概率为0的情况，这种方法可以解决零概率问题，避免出现条件概率为0的情况。加一平滑的公式如下：
$$
P(w_i|c_j)=\frac{count(w_i,c_j)+1}{\sum_{k=1}^n(count(w_k,c_j)+1)}
$$
其中，$w_i$ 是某个单词，$c_j$ 是某个类别，$count(w_i,c_j)$ 表示在类别 $c_j$ 中单词 $w_i$ 出现的次数，$\sum_{k=1}^{n}(count(w_k,c_j)+1)$ 表示类别 $c_j$ 中所有单词出现次数之和再加上词表大小（即词表中单词的总数），$n$ 表示词表中单词的个数。

通过加一平滑，我们可以在保证每个单词的条件概率不为0的情况下，将原本过于极端的概率值进行平滑，避免出现过拟合问题。

同时在处理的过程中，对于多个特征的情况，使用乘法计算可能会导致概率值过小而出现下溢的情况。为了避免这个问题，通常会将概率值取对数，然后改用加法进行计算。因为取对数后，乘法运算变成了加法运算，从而可以避免概率值下溢的问题。同时对数函数是单调的，不会影响其概率的选择。

另外，我还考虑了将训练集和测试集都转化为简体中文再进行训练，但结果不尽如人意，只能达到0.813左右的准确率，因此该方法不是很可行。

### 实验反思

朴素贝叶斯的原理比较好理解，但其效果自然也不是最好的，自然只能得到不是很高的准确率，为了提高准确度，可以考虑一些其他的办法，例如：

* 可以考虑使用TF-IDF等方法进行特征提取，这样可以过滤掉一些高频出现但是并不重要的词汇。
* 可以尝试使用n-gram来提取特征，这样可以捕捉更多的文本上下文信息。
* 使用词向量等深度学习技术进行特征提取也是一种选择。
* 可以考虑使用交叉验证等技术来选择模型参数。
* 尝试使用其他的分类模型，如SVM、决策树、随机森林等。
* 可以考虑使用深度学习方法，如卷积神经网络、循环神经网络等，进一步提高模型的准确率。