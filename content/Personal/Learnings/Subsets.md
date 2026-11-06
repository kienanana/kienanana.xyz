---
class:
tags:
  - cs/arrays
  - cs/backtracking
  - cs/bit-manipulation
  - leetcode/medium
source: https://leetcode.com/problems/subsets/
related:
author:
date: 2026-10-15
updated: 2026-10-15 01:36:16
aliases:
---
[[Leetcode]] #78

## Problem
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
 
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
	1 <= nums.length <= 10
	-10 <= nums[i] <= 10
	All the numbers of nums are unique.

### My Backtracking Solution:
```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        - res = []
        - subset = []

        - at each step:
            - save curr state
            - explore including / excluding every remaining num

        def backtrack(start)
        - save curr state
            - res.append(subset.copy())
            - use copy if not all entries reference same thing
        - explore
            - for i in range(start,len) 
                - subset.append(nums[i])
                - backtrack(i+1)
                - subset.pop()
        """
        res = []
        subset = []
        
        def backtrack(start):
            # save curr state
            res.append(subset.copy())

            # explore incl / excl every rem num
            for i in range(start, len(nums)):
                # include 
                subset.append(nums[i])
                backtrack(i+1)
                # exclude, decide on next num
                subset.pop()
        
        backtrack(0)
        return res
```

time complexity: O(n * 2^n)

### Other version of Backtracking Solution:
```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        
        def dfs(i):
            # no more choices 
            if i >= len(nums):
                res.append(subset.copy())
                return
            # include i
            subset.append(nums[i])
            dfs(i+1)
            # exclude i
            subset.pop()
            dfs(i+1)

        dfs(0) 
        return res
```


### Iteration Solution:
we can also just adding the curr number to every subset and appending that to the res.

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
```

still O(n * 2^n) time complexity

### Divide and Conquer Solution:
- base case: if nums empty, return [[]] 
- divide:
	- recursively generate all subsets of nums[1:] (excl the first element)
- conquer:
	- store the returned subsets in leftover
- combine:
	- excl nums[0] : keep all subsets in leftover
	- include nums[0] : create new subsets by prepending to each subset in leftover
- concat both collections, return

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if (len(nums) == 1):
            return [[], nums]
        else:
            leftover = self.subsets(nums[1:])
            leftover2 = leftover.copy()
            for i in range(len(leftover2)):
                leftover2[i] = [nums[0]] + leftover2[i] 
            return leftover + leftover2
```

