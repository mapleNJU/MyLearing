import random
import numpy as np

l = list()

for i in range(1, 100000):
    p = False
    for j in range(1, 100):
        if j <= 50:
            x = random.randint(1, 100)
            if x <= 2:
                p = True
                l.append(j)
                break
        else:
            x = random.randint(1, 100)
            if x <= (j - 49) * 2:
                p = True
                l.append(j)
                break
re = np.mean(l)
print(re)