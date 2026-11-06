---
class:
tags:
  - cs/arrays
  - leetcode/easy
source: https://leetcode.com/problems/max-consecutive-ones/
related:
author:
date: 2026-10-02
updated: 2026-10-02 15:29:25
aliases:
---
[[Leetcode]] #485

## Problem
Given a binary array nums, return the maximum number of consecutive 1's in the array.
 
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
	1 <= nums.length <= 105
	nums[i] is either 0 or 1.

### My Solution:
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        - brute force:
            - int max
            - iterate through
            - while 1: count++, 
            - max = max(max, count)
            - reset count
        """
        res = 0
        count = 0
        for n in nums:
            if n == 1:
                count+=1
            else:
                count = 0
            res = max(res,count)
        return res
```
