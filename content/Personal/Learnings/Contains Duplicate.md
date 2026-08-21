---
class:
tags:
  - cs/arrays
  - cs/hashing
  - cs/sorting
  - leetcode/easy
source: https://leetcode.com/problems/contains-duplicate/
related:
author:
date: 2026-08-20
updated: 2026-08-20 18:21:33
aliases:
---
[[Leetcode]] #217
## Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
	1 <= nums.length <= 105
	-109 <= nums[i] <= 109

### My Solution:
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (!map.containsKey(num)) {
                map.put(num, i);
            } else {
                return true;
            }
        }

        return false;
    }
}
```

The optimal solution is a one liner lol

### Optimal Solution
```java
public class Solution {
    public boolean hasDuplicate(int[] nums) {
        return Arrays.stream(nums).distinct().count() < nums.length;
    }
}
```
