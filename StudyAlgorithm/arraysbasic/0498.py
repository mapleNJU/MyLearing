'''
0498
难度:中等
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
'''
n = int(input())
x = input()
temp = x.split(',')
nums = []
for i in range(n):
    nums.append([int(temp[j + i * n]) for j in range(n)])


def FindOrder(nums):
    m = len(nums)
    n = len(nums[0])
    Lia = []
    for i in range(m):
        for j in range(n):
            Lia.append(nums[i][j])


print(FindOrder(nums))