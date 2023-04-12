可执行命令如下：

+ python utils.py 从网上下载训练好的搜狗新闻字向量中提取train.txt中所有字的字向量 PS:已提前提取好，同时压缩时已去除下载的字向量，请无视。

+ python main.py 执行主函数，进行模型训练或测试集预测包含参数如下：
  + --train default=y 默认执行train，当为n时执行Test并将结果写入201300062.txt中