with open("Classify/second.txt", 'r') as f:
    l1 = f.readlines()
with open("Classify/201300066.txt", 'r') as f:
    l2 = f.readlines()
count = 0
for i in range(len(l1)):
    if l1[i] != l2[i]:
        count += 1
print(count)