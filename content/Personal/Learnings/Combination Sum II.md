---
class:
tags:
  - cs/arrays
  - cs/backtracking
  - leetcode/medium
source: https://leetcode.com/problems/combination-sum-ii/
related:
author:
date: 2026-10-30
updated: 2026-10-30 17:47:17
aliases:
---
[[Leetcode]] #40

## Problem
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
 
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 
Constraints:
	1 <= candidates.length <= 100
	1 <= candidates[i] <= 50
	1 <= target <= 30

### My Backtracking Solution:
```python
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        - backtrack(start, selection, currSum)
        """
        res = []
        def backtrack(start, selection, currSum):
            if currSum == target:
                res.append(selection.copy())
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                if (i > start) and num == candidates[i-1]:
                    continue
                if ((currSum + num) <= target):
                    selection.append(num)
                    backtrack(i+1, selection, currSum+num)
                    selection.pop()
        
        candidates.sort()
        backtrack(0,[],0)
        return res
```
