---
class:
tags:
  - cs/arrays
  - cs/backtracking
  - leetcode/medium
source: https://leetcode.com/problems/permutations/
related:
author:
date: 2026-10-27
updated: 2026-10-27 02:15:41
aliases:
---
[[Leetcode]] #46

## Problem
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
 
Constraints:
	1 <= nums.length <= 6
	-10 <= nums[i] <= 10
	All the integers of nums are unique.

### My Backtracking Solution:
```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        - res []
        - def backtrack(selection)
            - if len == len(nums): res.append
            - iterate through options in nums
                - if nums not in selection:
                    - explore selection.append
                    - backtrack(newSelection)
                    - selection.pop
        """
        res = []
        def backtrack(selection):
            if len(selection) == len(nums):
                res.append(selection.copy())
                return
            for num in nums:
                if num not in selection:
                    selection.append(num)
                    backtrack(selection)
                    selection.pop()
        backtrack([])
        return res
```

### Optimal Backtracking Solution (In-place Swapping):
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:]) # same as .copy()
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]
```