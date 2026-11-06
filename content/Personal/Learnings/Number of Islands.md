---
class:
tags:
  - cs/arrays
  - cs/graphs
  - cs/union-find
  - cs/matrices
  - leetcode/medium
source: https://leetcode.com/problems/number-of-islands/
related:
author:
date: 2026-11-03
updated: 2026-11-03 15:16:21
aliases:
---
[[Leetcode]] #200

## Problem
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:
	m == grid.length
	n == grid[i].length
	1 <= m, n <= 300
	grid[i][j] is '0' or '1'.

### My DFS Solution:
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - visited = deepcopy(grid)
        - directions = [...]
        - res = 0

        - find new island start 
            - for i
                - for j 
                    - if visited[i][j] == 1
                    - dfs 
                    - res++

        - dfs(x,y) x,y: new island start
            - mark visited[x][y] = #
            - newX, newY in 4 directions
                - 0 <= newX < len(grid)
                - 0 <= newY < len(grid[0])
                - visited[newX][newY] == 1
        """
        visited = deepcopy(grid)
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
            visited[x][y] = "#"
            for dx, dy in dirs:
                newX = x+dx
                newY = y+dy
                if (0 <= newX < rows) and (0 <= newY < cols) and visited[newX][newY] == "1":
                    dfs(newX,newY)

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == "1":
                    dfs(i,j)
                    res+=1                
        return res
```

### My BFS Solution:
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [
            (0,1),
            (0,-1),
            (-1,0),
            (1,0)
        ]        
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(x,y):
            q = deque()
            grid[x][y] = "0"
            q.append((x,y))

            while q:
                r,c = q.popleft()
                for dx, dy in dirs:
                    newX = r+dx
                    newY = c+dy
                    if (0 <= newX < rows) and (0 <= newY < cols) and grid[newX][newY] == "1":
                        q.append((newX,newY))
                        grid[newX][newY] = "0"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    res+=1                
        return res 
```