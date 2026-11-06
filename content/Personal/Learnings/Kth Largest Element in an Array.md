---
class:
tags:
  - cs/arrays
  - cs/divide-and-conquer
  - cs/sorting
  - cs/heaps
  - cs/quickselect
  - leetcode/medium
source: https://leetcode.com/problems/kth-largest-element-in-an-array/
related:
author:
date: 2026-10-08
updated: 2026-10-08 15:42:31
aliases:
---
[[Leetcode]] #215

quick select maxxing.

## Problem
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
	1 <= k <= nums.length <= 105
	-104 <= nums[i] <= 104

### My Min Heap Solution:
```python
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        - min heap:
            - size k  
        """
        minHeap = nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return minHeap[0]
```

### One Liner Min Heap Solution:
```python
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
```


these, however, aren't the optimal solution - just implementing the min heap likely wouldn't pass the interview. although the worst case for quick select is o(n^2), that is only for the cases when the input is already sorted (and can be mitigated by different pivot-picking approach). 

> In the real interview scenario, this is the pefect case for follwing up with the interviewer about the expected input shape and pattern, and propose / implement the quick-select if that's a fair tradeoff. 

~ some dude

### Quick Select Solution: 
> TLE on leetcode

when you always choose last element as pivot, instead of eliminating roughly half the elements each iteration, we're only eliminating one element at a time, which becomes really inefficient for large arrays -> O(n^2) worst case

```python
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # quickselect
        k = len(nums)-k

        def quickselect(l,r):
            pivot, pos = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    pos += 1
            nums[pos], nums[r] = nums[r], nums[pos]
            if pos > k:
                return quickselect(l, pos-1)
            elif pos < k:
                return quickselect(pos+1, r)
            else:
                return nums[pos]

        return quickselect(0, len(nums)-1)
```

the *optimal version* of quick select improves it by:
- choosing a pivot more intelligently (using a 3 element median-like technique)
- reducing worst-case behaviour 
- partitioning the array efficiently so that large elements move left and small elements move right 
i honestly don't even know what's going on here. is it actually better?

### OPTIMAL Quick Select Solution:
```python
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        mid = (left + right) >> 1
        nums[mid], nums[left + 1] = nums[left + 1], nums[mid]

        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] < nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] < nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]

        pivot = nums[left + 1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] > pivot:
                    break
            while True:
                j -= 1
                if not nums[j] < pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j

    def quickSelect(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        while True:
            if right <= left + 1:
                if right == left + 1 and nums[right] > nums[left]:
                    nums[left], nums[right] = nums[right], nums[left]
                return nums[k]

            j = self.partition(nums, left, right)

            if j >= k:
                right = j - 1
            if j <= k:
                left = j + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, k - 1)
```