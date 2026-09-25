---
class:
tags:
  - cs/arrays
  - cs/two-pointers
  - cs/binary-search
  - cs/bit-manipulation
  - cs/pigeonhole-principle
  - cs/floyds-cycle-finding-algorithm
  - leetcode/medium
source: https://leetcode.com/problems/find-the-duplicate-number/
related:
author:
date: 2026-09-22
updated: 2026-09-22 19:51:52
aliases:
---
[[Leetcode]] #287

## Problem
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
 
Constraints:
	1 <= n <= 105
	nums.length == n + 1
	1 <= nums[i] <= n
	All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
	How can we prove that at least one duplicate number must exist in nums?
	Can you solve the problem in linear runtime complexity?

### My Solution (LinkedList, Two Pointers)
```python
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        - hashset seen []
            - for n in nums
                - if seen return n
                - else seen.append
        - O(n) time 

        - "linkedlist" (two pointer)
        - n in nums is a node:
            - nums[i] = next
        - slow, fast
            - find cycle 
        """
        slow = fast = nums[0] # or 0
        # part 1: detect cycle 
        while True:
            # slow.next
            slow = nums[slow]
            # fast.next
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # part 2: find cycle entrance
        ## reset one pointer
        ## move both by 1 step
        slow = nums[0] # or 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```
