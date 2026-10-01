---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/medium
source: https://leetcode.com/problems/validate-binary-search-tree/
related:
author:
date: 2026-09-30
updated: 2026-09-30 15:00:47
aliases:
---
[[Leetcode]] #98

## Problem
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
	The left subtree of a node contains only nodes with keys strictly less than the node's key.
	The right subtree of a node contains only nodes with keys strictly greater than the node's key.
	Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:
	The number of nodes in the tree is in the range [1, 104].
	-231 <= Node.val <= 231 - 1

### My DFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        - left subtree < node
        - right subtree > node
        - isValidBST(left) and isValidBST(right)

        - dfs(node, lowerBound, upperBound)
            - lower < node < upper
            - base case: 
                - no children: True
            - if left > node or right < node:
                - False
            - return dfs left (upper = node.val)
            - and dfs right (lower = node.val)
        """
        def dfs(node, lower, upper):
            if not node:
                return True 
            elif not (lower < node.val and node.val < upper):
                return False
            else:
                return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        
        return dfs(root, float("-inf"), float("inf"))
```

### My BFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        - BFS to check across level
        - (node, lower, upper)
        - same logic
            - lower < node.val < upper
            - explore left: upper = node.val 
            - explore right: lower = node.val
        """
        q = deque([(root, float("-inf"), float("inf"))])
        
        while q:
            node, lower, upper = q.popleft()
            if not (lower < node.val and node.val < upper):
                return False
            if node.left:
                q.append((node.left, lower, node.val))
            if node.right:
                q.append((node.right, node.val, upper))
        return True

```