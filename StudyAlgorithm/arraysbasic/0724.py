'''
简单题0724
给你一个整数数组nums ，请计算数组的 中心下标 。
数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
'''

x = input()
nums = x.split(',')
nums = [int(nums[i]) for i in range(len(nums))]


def pivotIndex(nums):
    total = sum(nums) - nums[0]
    lefttotal = 0
    if total == 0:
        return 0
    for i in range(0, len(nums) - 1):
        lefttotal = lefttotal + nums[i]
        total = total - nums[i + 1]
        if total == lefttotal:
            return i + 1
        else:
            continue
    return -1


result = pivotIndex(nums)
print(result)
