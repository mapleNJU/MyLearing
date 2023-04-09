with open("Classify/sentiment_result.txt", 'r') as f1:
    l1 = f1.readlines()
    l = [int(item) for item in l1]
    print(sum(l) / len(l))
