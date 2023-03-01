'''
简单题0238

给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
'''

x = input()
nums = x.split(',')
nums = [int(nums[i]) for i in range(len(nums))]


def FindMaxConsecutiveOnes(nums):
    temp = 0
    result = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            temp = temp + 1
            if result < temp:
                result = temp
        else:
            temp = 0
    return result


result = FindMaxConsecutiveOnes(nums)
print(result)