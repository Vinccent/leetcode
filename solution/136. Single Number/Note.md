# 只出现一次的数字

## 题目描述
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
```
输入: [2,2,1]
输出: 1
```
示例 2:
```
输入: [4,1,2,1,2]
输出: 4
```
## 解法
先用一个 `dict` 记录数字出现的次数，然后当次数为2时 `pop` 出去，剩下最后一个自然是只出现一次的数字

### 别人的解法
2 * (a + b + c) - (a + a + b + b + c) = c

```python
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
```
