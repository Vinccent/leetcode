# 两数之和

## 题目描述
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:
```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
## 解法
利用 `HashMap` 来记录下数组的下标和数值，对数组中的每一个数字 `nums[i]` ,判断差值 `target-nums[i]` 是否在 `HashMap` 里头，存在的话，就返回这两个数值的下标组成的数组。在 `Python` 里， `HashMap` 用 `dict` 代替

```python
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
```

