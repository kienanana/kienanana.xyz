---
class:
tags:
  - cs/arrays
  - cs/heaps
  - leetcode/easy
source: https://leetcode.com/problems/last-stone-weight/
related:
author:
date: 2026-10-05
updated: 2026-10-05 20:08:03
aliases:
---
[[Leetcode]] #1046

## Problem
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
	If x == y, both stones are destroyed, and
	If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
 
Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1
 
Constraints:
	1 <= stones.length <= 30
	1 <= stones[i] <= 1000

### My Max Heap Solution:
```python
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        - max heap
        - heappop_max 2x 
        - heappush_max remaining 
        """
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        while len(maxHeap) > 1:
            y = heapq.heappop_max(maxHeap)
            x = heapq.heappop_max(maxHeap)

            if y-x:
                heapq.heappush_max(maxHeap, y-x)
        
        if maxHeap: 
            return heapq.heappop_max(maxHeap)
        else:
            return 0
```

### Cleaner Max Heap Solution:
```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
```

there takes O(n log n) time and O(n) space, but we can actually get an even more optimal solution by using bucket sort: O(n + w) time and O(w) space, where n is length of stones, and w is max value in stones 

### Optimal Bucket Sort Solution:
- since all stone values lie within a limited numeric range, we can avoid sorting or using a heap by using bucket sort / freq counting
- instead of tracking every stone individually, we store how many stones exist for each possible weight 

1. Find the maximum stone weight.
2. Create a frequency array bucket of size maxWeight + 1.
3. Count how many stones of each weight exist.
4. Start from the heaviest weight and repeat:
	- If the count at this weight is even, all stones cancel in pairs.
    - If odd, one stone remains; find the next heaviest stone to smash with it.
    - Compute the difference and update the bucket.
	- Move the pointer to the next heaviest relevant weight.
5. When only one weight remains with an odd count, return it.
6. If all stones cancel out, return 0.

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1

        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1

            if j == 0:
                return first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first
```