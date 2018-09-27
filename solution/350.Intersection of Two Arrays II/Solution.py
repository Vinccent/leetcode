def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    record, result = {},[]
    for num in nums1:
        record[num] = record.get(num, 0) + 1
        if num in nums2:
            result.append(num)
            record[num] -= 1
    return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))