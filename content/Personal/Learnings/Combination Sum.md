---
class:
tags:
  - cs/arrays
  - cs/backtracking
  - leetcode/medium
source: https://leetcode.com/problems/combination-sum/
related:
author:
date: 2026-10-23
updated: 2026-10-23 10:54:51
aliases:
---
[[Leetcode]] #39

## Problem
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
 
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
 
Constraints:
	1 <= candidates.length <= 30
	2 <= candidates[i] <= 40
	All elements of candidates are distinct.
	1 <= target <= 40

### My Backtracking Solution:
```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        - res []
        - def backtrack(idx, selection: list[int], currSum)
            - explore selecting every avail int 
                - avoid duplicate combis:
                    - only explore >= curr index 
                if currSum + int <= target
            - if newSum == target:
                - selection.append(int)
                - res.append(selection.copy())
        - backtrack([]) 
        """
        res = []
        def backtrack(idx, selection, currSum):
            if currSum == target:
                res.append(selection.copy()) 
            for i in range(idx, len(candidates)):
                # explore options from idx on
                num = candidates[i]
                if ((currSum + num) <= target):
                    selection.append(num)
                    backtrack(i, selection, currSum + num)
                    selection.pop()
        backtrack(0,[],0)
        return res
```
