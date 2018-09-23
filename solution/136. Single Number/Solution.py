def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    record = {}
    for num in nums:
        record[num] = record.get(num, 0) + 1
        if record[num] == 2:
            record.pop(num)
    
    return record.popitem()[0]

nums = [4,3,4,3,2]
print(singleNumber(nums))
