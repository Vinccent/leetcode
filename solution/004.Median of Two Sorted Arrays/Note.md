## 两个排序数组的中位数

### 题目描述

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:
```
nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
```
示例 2:
```
nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
```

### 解法
首先需要注意到本算法要求的时间复杂度是O(log(m+n))，因此普通的排序算法是不适用于本题目的。根据这个时间复杂度，我们可以推算出该题目最基本的思想为分治法。

我们将这两个数组分别做切分，A数组切分位置为i，B数组切分位置为j，令A数组左边的元素个数加上B数组左边的元素个数等于两数组长度之和的一半，这样就能在长度上平分这两个数组了，同时又满足时间复杂度的要求。具体切分如下所示(i是数组A分界线，j是数组B分界线)
```
          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
```
此时我们只要关注边界线上的4个数字`A[i-1]`、`A[i]`、`B[j-1]`、`B[j]`即可，需要注意的是，**此时i不一定等于j**

为了分成上述情形，我们需要满足以下条件
>1. `i+j = m−i+n−j` (或者: `m-i+n-j+1`)
    if `n ≥ m`, then `i = 0 ~ m`, `j = (m+n+1)/2-i `
>2. `B[j-1]` <=` A[i]` and `A[i-1]` <= `B[j]`

接着我们开始寻找边界线i和j
1. `imin = 0`, i`max = len1`, [imin, imax]为i的范围
2. **`i = (imin + imax) / 2`**, **`j = (m+ n + 1) / 2 - i`**
3. 当两部分的元素数量相等时，存在以下三种情况

  * `B[j-1] <= A[i]` and `A[i-1] <= B[j]`

    此时i为符合要求的分界线值

  * `B[j-1] > A[i]`

    边界线需要右移 --> `imin = i + 1`

  * `A[i-1] > B[j]`

    边界线需要左移 --> `imax = i - 1`
数组长度和为奇数时：**`median = max_of_left`**

数组长度和为偶数时：**`median = (max_of_left + min_of_right )  /  2`**

按照我们分组的定义，可以得到 `max_of_left` = `max(A[i-1],B[j-1])`, `min_of_right` = `max(A[i],B[j])`

所以最后我们需要求出 `max_of_left` 和 `min_of_right` 两个值

为了将求解的情况简化，我们发现求解这两个值的时候有临界值：

* `i == 0` : `max_of_left = B[j-1]`
* `j == 0` : `max_of_left = A[i-1]`

* `i == m`: `min_of_right = B[j]`
* `j == n`: `min_of_right = A[i]`
* 其余情况 : `max_of_left` = `max(A[i-1],B[j-1])` ，`min_of_right` = `max(A[i],B[j])`

```python
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
```