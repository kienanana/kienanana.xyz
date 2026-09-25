---
class:
tags:
  - cs/arrays
  - cs/binary-search
  - leetcode/medium
source: https://leetcode.com/problems/koko-eating-bananas/
related:
author:
date: 2026-09-11
updated: 2026-09-11 14:30:32
aliases:
---
[[Leetcode]] #875

not sure why my solution is so slow? might be a python thing. it's the optimal approach and i'm pretty proud that i arrived at that solution myself. 
![[Screenshot 2026-09-11 at 2.31.46 PM.png]]

## Problem
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
	1 <= piles.length <= 104
	piles.length <= h <= 109
	1 <= piles[i] <= 109

### My Solution:
```python
import math
class Solution: 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        - eating speed k
            - k bananas per move
            - if pile < k : eat all
        - finish within h moves

        - possible k range: [1, max(piles)] 
        - binary searcg through k range:
        - while l < r
            - for any k:
                - moves = 0 
                    - for pile in piles
                        - if pile <= k: moves++
                        - else: ceiling division: 
                            moves += math.ceil(pile,k)
            - target: h
                - REVERSE LOGIC! 
                - if moves <
                    - eating too fast, k is ok, but can be bigger
                    - search left
                - if moves > 
                    - eating too slowly
                    - search right
        - return final k settled on
        """
        l,r = 1, max(piles)
        while l < r:
            m = l + (r-l)//2
            moves=0
            for pile in piles:
                moves += math.ceil(pile/m)
            if moves > h:
                l = m+1
            else:
                # m is acceptable! just seeing if can be improbed
                r = m
        return l
```
