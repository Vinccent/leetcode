# 最长回文串

## 题目描述
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

 

示例 1：
```
输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
``` 

## 解法
字符的个数分为两种情况，一种是偶数，一种是奇数；偶数的话直接加到结果中，奇数的话减掉一个以后便可以加入，但是还要考虑最中间可以放一个字母，所以要加一个flag来确定是否还存在单独的字母用来存放。

```python
def longestPalindrome(A):
    """
    :type s: str
    :rtype: int
    """
    sets = set(s)
    flag, res = 0, 0
    for letter in sets:
        num = s.count(letter)
        if num % 2 == 0:
            res += num
        else:
            flag = 1
            res += num - 1
    return res + flag
```
