---
class:
tags:
  - cs/arrays
  - cs/hashing
  - cs/matrices
  - leetcode/medium
source: https://leetcode.com/problems/valid-sudoku/
related:
author:
date: 2026-09-02
updated: 2026-09-02 16:49:04
aliases:
---
[[Leetcode]] #36

Holy shit man thats a lot of loops. Still O(1) though, based question.

## Problem
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
	Each row must contain the digits 1-9 without repetition.
	Each column must contain the digits 1-9 without repetition.
	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
	Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
	board.length == 9
	board[i].length == 9
	board[i][j] is a digit 1-9 or '.'.


### My Solution
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        - a particular cell belongs to:
            - a box
            - a row
            - a column
        - check row:
            - for i in range(9) 
                - set seen
                - row = board[i]
                - for j in range(9)
                    - if row[j] in seen return False
        - check column
            - for j in range(9)
                - set seen
                - for i in range(9)
                    - check (board[i][j])
                    - if num in seen return False
        - check box:
            - for rowStart in range(0,9,3)
                - for colStart in range(0,9,3)
                    - set seen
                    - for i in range(rowStart, rowStart+3)
                        - for j in range(colStart, colStart + 3)
        """
        # check row
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[i][j]
                if (num == "."):
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)
        
        # check col
        for j in range(9):
            seen = set()
            for i in range(9):
                num = board[i][j]
                if (num == "."):
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)
        
        # check box 
        for rowStart in range(0,9,3):
            for colStart in range(0,9,3):
                seen = set()
                for i in range(rowStart,rowStart+3):
                    for j in range(colStart,colStart+3):
                        num = board[i][j]
                        if (num == "."):
                            continue
                        if num in seen:
                            return False
                        else:
                            seen.add(num)
        
        return True
```
