---
class:
tags:
  - cs/arrays
  - cs/math
  - cs/divide-and-conquer
  - cs/sorting
  - cs/heaps
  - cs/quickselect
  - cs/k-d-tree
  - leetcode/medium
source: https://leetcode.com/problems/k-closest-points-to-origin/
related:
author:
date: 2026-10-06
updated: 2026-10-06 15:12:51
aliases:
---
[[Leetcode]] #973

## Problem
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
 
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
Constraints:
	1 <= k <= points.length <= 104
	-104 <= xi, yi <= 104

### My PQ (Min Heap) Solution:
```python
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []
        res = []
        for point in points:
            heapq.heappush(pq, (point[0]**2 + point[1]**2, point))
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
```

### My Max Heap Solution:
maintain size k
```python
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # max heap
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, [-(x**2 + y**2), x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
```


the optimal solution is actually to use **QuickSelect**, the same idea used in [[L4 Sorting#Quick Sort]]'s partition step

### Optimal Quick Select Solution:
- pick a pivot point
- partition all points into:
	- points closer than the pivot
	- points farther than the pivot 
- after partitioning, the pivot ends at its correct position in the final sorted order 
- if the pivot ends up at index p 
	- if p == k: then left side already contains k closest points
	- if p < k: search the right half
	- if p > k: search left half 

```python
class Solution:
    def kClosest(self, points, k):
        # Squared distance preserves the ordering; no square root needed.
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            # Use the last point as the pivot.
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            # i is the next slot for a point with distance <= pivotDist.
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            # Place the pivot between the closer/equal and farther groups.
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        # If k == len(points), return all points without partitioning.
        pivot = len(points)

        # At index k, the pivot has k closest points before it.
        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                # The cutoff is to the right of the pivot.
                L = pivot + 1
            else:
                # Search left; if pivot == k, the loop stops next.
                R = pivot - 1
        # These k points need not be sorted internally.
        return points[:k]
```
