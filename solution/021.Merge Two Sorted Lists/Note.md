# 合并两个有序链表

## 题目描述
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例:
```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

## 解法
链表具有天然的递归性，`l1`为空的时候，把`l2`接上；`l2`为空的时候，把`l1`接上。如果 `l1.val < l2.val` ，那么就返回 `l1.next = mergeTwoLists(l1.next, l2)`；否则返回 `l2.next = self.mergeTwoLists(l1, l2.next)`

```python
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    while l1 and l2:
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    if l1.next == None:
        return l2
    else:
        return l1
```

