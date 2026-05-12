---
class:
tags:
  - cs/linked-lists
  - cs/math
  - cs/recursion
  - leetcode/medium
source: https://leetcode.com/problems/add-two-numbers/description/
related:
author:
date: 2026-05-05
updated: 2026-05-05 22:53:57
aliases:
---
[[Leetcode]] #2

This one took me really long, because I just tried to brute force it at first, only to find myself running into so many issues with my for / while loops. When I realised the solution was just a simple recursion, with the reverse order of the digits allowing us to treat this like a Primary School addition, everything made much more sense and this became a breeze to implement save for some really stupid syntax errors on my part. 

## Problem

![[Screenshot 2026-05-05 at 11.02.43 PM.png]]

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode add(ListNode l1, ListNode l2, int carry) {
        /*
        - basically addition for kids
        - starting from ones place
            - add
            - carry over 1 if have
            - new node
            - repeat for next place  
        */
        if (l1 == null && l2 == null && carry == 0) {
            return null;
        } 
        
        int v1 = (l1 != null) ? l1.val : 0;
        int v2 = (l2 != null) ? l2.val : 0;
        int sum = v1 + v2 + carry;
        int newCarry = sum/10;
        int digit = sum%10;

        ListNode next1 = (l1 != null) ? l1.next : null;
        ListNode next2 = (l2 != null) ? l2.next : null;
        return new ListNode(
            digit,
            add(next1, next2, newCarry)
        ); 
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return add(l1, l2, 0);
    }
}
```
