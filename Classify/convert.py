from zhconv import convert

with open("Classify/stop.txt", 'r') as f:
    stop_words = f.readlines()

stop = [convert(item, 'zh-hk') for item in stop_words]

file_name = "Classify/stop_hk.txt"
with open(file_name, 'w') as f1:
    for sentiment in stop:
        f1.write(sentiment)