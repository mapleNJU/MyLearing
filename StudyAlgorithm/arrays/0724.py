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
