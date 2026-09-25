---
class:
tags:
  - cs/linked-lists
  - cs/two-pointers
  - leetcode/medium
source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
related:
author:
date: 2026-09-18
updated: 2026-09-18 16:04:35
aliases:
---
[[Leetcode]] #19

## Problem
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
	The number of nodes in the list is sz.
	1 <= sz <= 30
	0 <= Node.val <= 100
	1 <= n <= sz

Follow up: Could you do this in one pass?

### My Solution: (Two Pointer)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        - fast, slow, prev
            - fast slow maintain gap of n-1
            - while fast.next
                - fast.next, slow.next, prev.next
        """
        slow = fast = head
        prev = None
        for i in range(n-1):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not prev:
                prev = head
            else:
                prev = prev.next
        
        # remove slow
        if prev:
            temp = slow.next
            slow.next = None
            prev.next = temp
            return head
        else:
            return slow.next
```

there's actually a cleaner way to implement this solution. instead of slow being the node to remove, slow can be the prev in this case. then, we just need to remove left.next. 

### Cleaner Solution (Two Pointer):
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
```


