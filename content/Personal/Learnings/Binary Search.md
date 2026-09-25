---
class:
tags:
  - cs/arrays
  - cs/binary-search
  - leetcode/easy
source: https://leetcode.com/problems/binary-search/
related:
author:
date: 2026-09-09
updated: 2026-09-09 19:17:27
aliases:
---
[[Leetcode]] #704

## Problem
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 
Constraints:
	1 <= nums.length <= 104
	-104 < nums[i], target < 104
	All the integers in nums are unique.
	nums is sorted in ascending order.

### My Solution:
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                # explore left
                r = m-1
            else:
                # explore right
                l = m+1
        return -1
```
