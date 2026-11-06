---
class:
tags:
  - cs/arrays
  - cs/strings
  - cs/backtracking
  - cs/graphs
  - cs/matrices
  - leetcode/medium
source: https://leetcode.com/problems/word-search/
related:
author:
date: 2026-11-02
updated: 2026-11-02 22:34:11
aliases:
---
[[Leetcode]] #79

this was pretty tricky, i had thought of the inoptimal ways to track visited cells, but not the "#" method initially. 

## Problem

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
 
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:
	m == board.length
	n = board[i].length
	1 <= m, n <= 6
	1 <= word.length <= 15
	board and word consists of only lowercase and uppercase English letters.
 
Follow up: Could you use search pruning to make your solution faster with a larger board?

### My Backtracking Solution:
```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        def backtrack(x,y,idx)
        - idx: idx of word 
        - options:
            - up: x, y+1
            - down: x, y-1
            - left: x-1, y
            - right: x+1, y
        - option valid if
            - 0 <= newX < len(board)
            - 0 <= newY < len(board[0])
        """
        # dx, dy
        directions = [
            (0,1),
            (0,-1),
            (-1,0),
            (1,0)
        ]

        def backtrack(x,y,i):
            if board[x][y] != word[i]:
                return False
            elif i == len(word)-1:
                return True
            
            temp = board[x][y]
            board[x][y] = "#"

            for dx, dy in directions:
                newX = x + dx
                newY = y + dy
                if  0 <= newX < len(board) and 0 <= newY < len(board[0]) and board[newX][newY] != "#":
                    if backtrack(newX, newY, i+1):
                        board[x][y] = temp
                        return True
            board[x][y] = temp
            return False
        
        # starting points
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
        return False 
```