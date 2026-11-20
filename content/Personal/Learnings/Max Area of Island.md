---
class:
tags:
  - cs/arrays
  - cs/graphs
  - cs/union-find
  - cs/matrices
  - leetcode/medium
source: https://leetcode.com/problems/max-area-of-island/
related:
author:
date: 2026-11-17
updated: 2026-11-17 18:24:38
aliases:
---
[[Leetcode]] #695

## Problem
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
 
Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 
Constraints:
	m == grid.length
	n == grid[i].length
	1 <= m, n <= 50
	grid[i][j] is either 0 or 1.

### My DFS Solution:
```python
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        dirs = [
            (0,1),
            (0,-1),
            (-1,0),
            (1,0)
        ]
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x,y):
            grid[x][y] = 0
            area = 1
            for dx, dy in dirs:
                newX = x+dx
                newY = y+dy
                if (0 <= newX < rows) and (0 <= newY < cols) and grid[newX][newY] == 1:
                    area += dfs(newX,newY)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res
```

### My BFS Solution:
```python
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        dirs = [
            (0,1),
            (0,-1),
            (-1,0),
            (1,0)
        ]
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        # BFS solution
        def bfs(a,b):
            q = deque()
            grid[a][b] = 0
            area = 1
            q.append((a,b))

            while q:
                x,y = q.popleft()
                for dx, dy in dirs:
                    newX = x+dx
                    newY = y+dy
                    if (0 <= newX < rows) and (0 <= newY < cols) and grid[newX][newY] == 1:
                        q.append((newX,newY))
                        grid[newX][newY] = 0
                        area += 1
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res,bfs(i,j))
        return res
```