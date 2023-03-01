'''
0238
难度:中等
给你一个整数数组nums，返回 数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积。
题目数据 保证 数组nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。
请不要使用除法，且在O(n) 时间复杂度内完成此题。
'''
'''
2023/3/1更新:只击败了1/5的人,还有很大改进空间
'''

x = input()
nums = x.split(',')
nums = [int(nums[i]) for i in range(len(nums))]


def productExceptSelf(nums):
    n = len(nums)
    Listleft = [nums[0]]
    Listright = [nums[n - 1]]
    for i in range(1, n, 1):
        Listleft.append(Listleft[i - 1] * nums[i])
        Listright.append(Listright[i - 1] * nums[n - i - 1])
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(Listright[n - 2])
            continue
        elif i == n - 1:
            result.append(Listleft[n - 2])
            continue
        else:
            result.append(Listleft[i - 1] * Listright[n - i - 2])
    return result


print(productExceptSelf(nums))