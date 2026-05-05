---
class:
tags:
  - cs/hashing
  - leetcode/easy
source: https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=plakya4j
related:
author:
date: 2026-05-05
updated: 2026-05-05 21:53:41
aliases:
---
Kicking off the reboot of my [[Leetcode]] grind with this classic problem. I say that but I literally forgot the solution immediately and took way longer than I should've. 
- wow am I rusty at Java
- forgot almost everything about the syntax, classes, functions etc. 
- attempted to do a two pointer solution at first, but it seemed like too much work and also most definitely not the fastest solution 
- got a hint from the internet and remembered that the HashMap class exists 
	- referred to [[L7 Hashing]]
- pretty smooth sailing from there, but getting to that point was truly a struggle. I had to shake so much rust off, but it felt good to get there in the end. 


## Problem 
Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

**Example 1:**
**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**
**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

**Example 3:**
**Input:** nums = [3,3], target = 6
**Output:** [0,1]

**Constraints:**
- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **Only one valid answer exists.**


```java
import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        - use hashmap 
        - idx, val of each num in nums 
        - iterate through hashmap
            - check if complement of that num is in hashmap 
            - if it is, return 
            - else continue 
        */
        HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>(); 
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int comp = target - num;

            if (hashmap.containsKey(comp)) {
                return new int[] {i, hashmap.get(comp)};
            } 
            hashmap.put(num, i);
        }
        return new int[] {};
    }
}
```


