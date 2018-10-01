# 分割数组

## 题目描述
给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 `left` 和 `right`， 使得：

* `left` 中的每个元素都小于或等于 `right` 中的每个元素。
* `left` 和 `right` 都是非空的。
* `left` 要尽可能小。

在完成这样的分组后返回 `left` 的长度。可以保证存在这样的划分方法。

 

示例 1：
```
输入：[5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
```
示例 2：
```
输入：[1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]
``` 

提示：

1. `2 <= A.length <= 30000`
2. `0 <= A[i] <= 10^6`
3. 可以保证至少有一种方法能够按题目所描述的那样对 `A` 进行划分。

## 解法
我们需要找到一个分界线，该分界线左边的最大值小于右边的最小值。那么我们通过遍历数组找出`A[:1],A[:2],...,A[:n]`中的最大值以及`A[:-1],A[:-2],...,A[:-n]`中的最小值，再通过比较分界线两边数组的最大值和最小值的关系来确定是否为所求的分界线
**小技巧** : `max(A[:n]) = max(max(A[:n-1]),A[n-1])`

```python
def partitionDisjoint(A):
    """
    :type A: List[int]
    :rtype: int
    """
    max_left = [None] * len(A)
    min_right = [None] * len(A)

    temp = A[0]
    for i in range(len(A)):
        temp = max(temp, A[i])
        max_left[i] = temp
    
    temp = A[len(A)-1]
    for i in range(len(A)-1, -1, -1):
        temp = min(temp, A[i])
        min_right[i] = temp

    for i in range(1,len(A)):
        if max_left[i-1] < min_right[i]:
            return i
```

