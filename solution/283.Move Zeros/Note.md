# 移动零

## 题目描述
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

## 解法
使用指针标记的方式，这里有一个trick，将按照顺序将所有非0的数字转移到前面，记录非0数字的个数，然后最后再将剩下的数字赋值为0。

```python
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
    return nums
```