---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/medium
source: https://leetcode.com/problems/binary-tree-level-order-traversal/
related:
author:
date: 2026-09-29
updated: 2026-09-29 16:18:17
aliases:
---
[[Leetcode]] #102

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 
Constraints:
	The number of nodes in the tree is in the range [0, 2000].
	-1000 <= Node.val <= 1000

### My BFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        - BFS
        """
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            currLevel = []
            for _ in range(len(q)):
                node = q.popleft()
                currLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(currLevel)
        return res
```
