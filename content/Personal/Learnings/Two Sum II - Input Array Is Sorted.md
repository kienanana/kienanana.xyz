---
class:
tags:
  - cs/arrays
  - cs/two-pointers
  - cs/binary-search
  - leetcode/medium
source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
related:
author:
date: 2026-09-03
updated: 2026-09-03 20:03:17
aliases:
---
[[Leetcode]] #167

## Problem
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
 
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
	2 <= numbers.length <= 3 * 104
	-1000 <= numbers[i] <= 1000
	numbers is sorted in non-decreasing order.
	-1000 <= target <= 1000
	The tests are generated such that there is exactly one solution.

### My Solution
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        a = 0
        b = length-1
        sum = numbers[a] + numbers[b]
        while sum != target:
            if sum < target:
                a+=1
            elif sum > target:
                b-=1
            sum = numbers[a] + numbers[b]
        return [a+1, b+1]
```

i only wrote the while condition to be sum != target because the question specifies that there definitely exists a solution. however, i should be writing something like this instead:

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
```




