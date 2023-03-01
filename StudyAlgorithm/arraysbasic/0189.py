'''
0189
难度:中等
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
'''
'''
Update:虽然这个题结果写对了,但还是有点糊里糊涂的,而且肯定还有改进空间.
'''
x = input()
nums = x.split(',')
nums = [int(nums[i]) for i in range(len(nums))]
k = int(input())


def rotate(nums, k):
    length = len(nums)
    rot = k % length
    result = []
    for i in range(length):
        result.append(nums[length - ((i + rot)) % length - 1])
    for i in range(length):
        nums[i] = result[i]
    nums.reverse()


rotate(nums, k)
print(nums)