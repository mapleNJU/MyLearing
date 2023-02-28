x = input()
xl = x.split(',')
xl = [int(xl[i]) for i in range(len(xl))]
for i in range(len(xl[::-1]) - 1, -1, -1):
    if xl[i] == 9:
        xl[i] = 0
        if i == 0:
            xl.insert(0, 1)
        continue
    if xl[i] != 9:
        xl[i] = xl[i] + 1
        break
print(xl)