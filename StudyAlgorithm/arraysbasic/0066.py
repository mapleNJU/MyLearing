'''
简单题0066
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
'''

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