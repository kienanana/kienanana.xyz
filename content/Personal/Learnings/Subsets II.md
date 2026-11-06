---
class:
tags:
  - cs/arrays
  - cs/backtracking
  - cs/bit-manipulation
  - leetcode/medium
source: https://leetcode.com/problems/subsets-ii/
related:
author:
date: 2026-10-29
updated: 2026-10-29 21:45:48
aliases:
---
[[Leetcode]] #90

## Problem
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
 
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
	1 <= nums.length <= 10
	-10 <= nums[i] <= 10

### My Backtracking Solution:
```python
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        - res []
        - subset [] 
        - def backtrack(start) 
            - explore incl/ excl every rem num
                - subset.append()
                - backtrack(i+1)
                - subset.pop()
        """
        res = []
        subset = []
        
        def backtrack(start):
            res.append(subset.copy())
            prev = None
            for i in range(start,len(nums)):
                if nums[i] != prev:
                    subset.append(nums[i])
                    backtrack(i+1)
                    subset.pop()
                    prev = nums[i]
        nums.sort()
        backtrack(0)
        return res
```

### Iteration Solution:
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_Idx = idx = 0

        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res
```