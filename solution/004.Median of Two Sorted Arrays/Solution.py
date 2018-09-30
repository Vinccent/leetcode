def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    len1, len2 = len(nums1), len(nums2)
    if len1 > len2:
        nums1, nums2, len1, len2 = nums2, nums1, len2, len1
    if len2 == 0:
        raise ValueError
    
    imin, imax, halflen = 0, len1, (len1 + len2 + 1) / 2 # fit for odd and even situation
    while imin < imax:
        i = (imin + imax) / 2
        j = halflen - i
        if i < len1 and nums2[j-1] > nums1[i]:
            # i is too small so that we need to increase it
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too large so that we need to decrease it 
            imax = i - 1
        else:
            # i is perfect for split them into two parts
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1],nums2[j-1])
            
            if (len1 + len2) % 2 == 1:
                return max_of_left

            if i == len1:
                min_of_right = nums2[j]
            elif j == len2:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i],nums2[j])

            return (max_of_left + min_of_right) / 2.0

