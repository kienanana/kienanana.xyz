---
class:
tags:
  - cs/arrays
  - cs/two-pointers
  - cs/sorting
  - leetcode/medium
source: https://leetcode.com/problems/3sum/
related:
author:
date: 2026-09-04
updated: 2026-09-04 14:30:07
aliases:
---
[[Leetcode]] #15

## Problem
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
	3 <= nums.length <= 3000
	-105 <= nums[i] <= 105

### My Awful Solution
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        - for i in len
            - if nums[i] seen before continue
            - 2 sum with target = 0 - num
                - append num to 2sum solution as res triplet
            - return list of res triplets 
        """
        res = set()
        seen = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in seen:
                continue
            seen.add(num)
            target = 0 - num

            seen2 = set()
            for j in range(i+1, len(nums)):
                n = nums[j] 
                diff = target - n
                if diff in seen2:
                    trip = tuple(sorted([nums[i], diff, n]))
                    res.add(trip) # dupe detection already built into set
                seen2.add(n) 
        return [list(t) for t in res]
```

my solution was genuinely terrible, i was whipping up O(n^2) shit in a kettle

![[Pasted image 20260904143154.png|289]]

### Rewrote Optimal Solution
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        - sort nums
        - iterate through nums[i]
        - if nums[i] > 0
            - all remaining nums > 0
            - impossible to get target 0 
            - break
        - two pointer
            - l,r
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            if num > 0: # remaining all >0
                break
            if i > 0 and num == nums[i-1]: # handle dupes
                continue
            
            l,r = i+1,len(nums)-1
            while l < r:
                sum = num + nums[l] + nums[r]
                if sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    # move l past dupes
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
```




