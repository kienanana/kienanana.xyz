---
class:
tags:
  - cs/arrays
  - cs/hashing
  - cs/divide-and-conquer
  - cs/sorting
  - cs/heaps
  - cs/bucket-sort
  - cs/quickselect
  - leetcode/medium
source: https://leetcode.com/problems/top-k-frequent-elements/
related:
author:
date: 2026-08-29
updated: 2026-08-29 14:04:22
aliases:
---
[[Leetcode]] #347

Quite straightforward, but this time I decided to revert to Python3 instead of Java to really hone in on Python in preparation for the upcoming job application cycle. Also had two beers while doing this one. :) 

## Problem
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:
	1 <= nums.length <= 105
	-104 <= nums[i] <= 104
	k is in the range [1, the number of unique elements in the array].
	It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

### My Solution
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        - freq {} 
        - for num in nums 
            - freq[num]++
        - sort freqs
            - break once sorted first k

        """        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freqSorted = dict(sorted(freq.items(), key = lambda item : item[1], reverse=True))
        return list(freqSorted.keys())[:k]
```

### Optimal Solution
The optimal solution uses Bucket Sort. We build a freq map that counts how many times each number appears: freq[i] stores numbers that appear i times. Then, res = [], and we iterate in reverse order from freq, adding until we have added k nums to res. 

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
```

