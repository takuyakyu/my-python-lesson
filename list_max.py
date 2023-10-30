def find_max(nums):
    if len(nums) == 0:
        return None
    else:
        max_number = nums[0]
        for i in nums:
            if max_number < i:
                max_number = i
    return max_number   

# 以下のリストから最大値を見つける例
numbers = [12, 45, 7, 23, 56, 89, 34, 8, 86, 23, 34, 56,109]
maximum = find_max(numbers)
print("最大値は:", maximum)
