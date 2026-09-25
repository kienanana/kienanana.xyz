---
class:
tags:
  - cs/arrays
  - cs/binary-search
  - cs/matrices
  - leetcode/medium
source: https://leetcode.com/problems/search-a-2d-matrix/
related:
author:
date: 2026-09-09
updated: 2026-09-09 23:40:49
aliases:
---
[[Leetcode]] #74

## Problem
You are given an m x n integer matrix matrix with the following two properties:
	Each row is sorted in non-decreasing order.
	The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 100
	-104 <= matrix[i][j], target <= 104

### My Solution:
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        - binary search first col
            - when l>r
                - binary search r's row
        """
        rows = len(matrix)
        cols = len(matrix[0])
        l,r = 0, rows-1
        while l <= r:
            m = l + (r-l)//2
            num = matrix[m][0]
            if num == target:
                return True
            elif num > target:
                r = m-1
            else:
                l = m+1
        
        l2, r2 = 0, cols-1
        while l2 <= r2:
            m2 = l2 + (r2- l2)//2
            num2 = matrix[r][m2]
            if num2 == target:
                return True
            elif num2 > target:
                r2 = m2-1
            else:
                l2 = m2+1
        return False
```

and here's the One Pass Binary Search approach:

> because the matrix is sorted row-wise and each row is sorted left-to-right, the entire matrix behaves like one big sorted array. 
> if we imagine flattening the matrix into a single list, the order of elements doesn't change

this means we can run one binary search from index 0 to ROWS x COLS - 1.
for any mix index m, we can map it back to the matrix using:
- row = m // COLS
- col = m % COLS

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        - one pass binary search
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r-l)//2
            # m//COLS: how many complete rows have we passed
            # m%COLS: (remainder) how far into the row are we
            row, col = m // COLS, m % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m-1
            else:
                l = m+1
        return False
```

