def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    dic = {}
    for index, num in enumerate(nums):
        if num in dic:
            return [dic[num], index]
        dic[target - num] = index        

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))