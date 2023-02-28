import random

all_num = 500000
a_list = [i for i in range(all_num)]
num = 300000

b_length = 1
b_list = []
while b_length <= num:
    random_number = random.randint(-all_num, all_num - 1)
    if random_number not in b_list:
        b_list.append(str(random_number))
        b_length = len(b_list) + 1

l = ["A", "B", "C", "D"]
str = ' '
f = open("k.txt", "w")
f.write(str.join(b_list))
f.close()