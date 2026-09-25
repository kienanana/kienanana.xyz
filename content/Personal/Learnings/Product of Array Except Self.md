---
class:
tags:
  - cs/arrays
  - cs/prefix-suffix
  - leetcode/medium
source: https://leetcode.com/problems/product-of-array-except-self/
related:
author:
date: 2026-08-29
updated: 2026-08-29 19:05:49
aliases:
---
[[Leetcode]] #238

## Problem
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
	2 <= nums.length <= 105
	-30 <= nums[i] <= 30
	The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

### My Solution
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        - totalProd & nonZeroProd
        - res = [totalProd]*length
        - for i in length
            - num = nums[i]
            - res[i] //= num 
        """
        length = len(nums)
        totalProd = 1 
        nonZeroProd = 1
        zeroCount = 0

        for i in range(length):
            num = nums[i]
            totalProd *= num
            if (num != 0):
                nonZeroProd *= num
            else:
                zeroCount += 1 

        if zeroCount > 1:
            return [0]*length

        res = [totalProd]*length

        for j in range(length):
            num = nums[j]
            if (num==0):
                res[j] = nonZeroProd
            else:
                res[j] //= num
        return res
```

### Optimal Solution
optimal solution is a Prefix & Suffix approach. res = [1] x length. they first iterate from elft to right, setting res[i] = prefix (product of all elements to the left) and update prefix x= nums[i]. Then they iterate from right to left, res[i] x= postfix (product of all elements to the right) and postfix x= nums[i]

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
```
