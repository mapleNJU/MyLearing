from zhconv import convert

with open("Classify/stop.txt", 'r') as f:
    stop_words = f.readlines()

stop = [convert(item, 'zh-hk') for item in stop_words]

file_name = "Classify/new_stop.txt"
with open(file_name, 'w') as f1:
    # 遍历情感分类结果列表，将每个元素写入文件中，并在元素之间添加换行符
    for sentiment in stop:
        f1.write(sentiment)