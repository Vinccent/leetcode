# 两个数组的交集II

## 题目描述
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
```
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
```
示例 2:
```
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
```
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 `nums1` 的大小比 `nums2` 小很多，哪种方法更优？
如果 `nums2` 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
## 解法
利用 `dict` 来记录下数组的下标和数值，先将其中一个数组 `nums1` 中的每一个数字存在 `dict` 中， `value` 值为出现的次数，然后再判断该数字是否在 `nums2` 中，如果有的话就存入结果数组中，并将 `record` 中的该数字计数-1

```python
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
```
