'''
3.1每日一题
难度:简单

给你一个大小为 n x n 的整数矩阵 grid 。

生成一个大小为(n - 2) x (n - 2) 的整数矩阵 maxLocal ，并满足：

maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
换句话说，我们希望找出 grid 中每个3 x 3 矩阵中的最大值。

返回生成的矩阵。
'''

n = int(input())
x = input()
temp = x.split(',')
nums = []
for i in range(n):
    nums.append([int(temp[j + i * n]) for j in range(n)])


def FindMax(i, j, nums):
    max = nums[i][j]
    for k in range(i, i + 3):  #python的range(i,j)函数意为从i到j,不包括j
        for l in range(j, j + 3):
            if nums[k][l] > max:
                max = nums[k][l]
                continue
    return max


def largestLocal(nums):
    n = len(nums)
    arr = []
    for i in range(n - 2):
        for j in range(n - 2):
            temp = FindMax(i, j, nums)
            arr.append(temp)
    return arr


arr = largestLocal(nums)
li = []
for j in range(n - 2):
    li.append([arr[i + j * (n - 2)] for i in range(n - 2)])
print(li)