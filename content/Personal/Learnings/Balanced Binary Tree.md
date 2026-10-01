---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/easy
source: https://leetcode.com/problems/balanced-binary-tree/
related:
author:
date: 2026-09-26
updated: 2026-09-26 12:34:33
aliases:
---
[[Leetcode]] #110

## Problem
Given a binary tree, determine if it is height-balanced.
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 
Constraints:
	The number of nodes in the tree is in the range [0, 5000].
	-104 <= Node.val <= 104

### My Solution (Recursive DFS):
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        - height-balanced:
            - abs(left.height - right.height) <= 1
        - recursively DFS
        """
        # return (maxHeight, isBalanced)
        def dfs(node) -> (int,bool):
            if not node:
                return (0, True)
            else:
                left = dfs(node.left)
                right = dfs(node.right)

                return (1 + max(left[0],right[0]), (abs(left[0]-right[0]) <= 1) & left[1] & right[1])
        return dfs(root)[1]
```

the iterative solution takes some brain power, because of the postorder traversal.

### Iterative DFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        - height-balanced:
            - abs(left.height - right.height) <= 1
        - iteratively DFS
            - stack = []
            - curr node
            - postorder
                - explore left 
                - if right subtree go right
                - process curr node when right done / none 
                    - last == right
                - move up 
        """
        stack = []
        curr = root
        heights = {}
        last = None

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[-1]
                if (not curr.right) or (last == curr.right):
                    # can process curr
                    stack.pop()
                    left = heights.get(curr.left, 0)
                    right = heights.get(curr.right, 0)

                    if not (abs(left - right) <= 1):
                        return False
                    
                    heights[curr] = 1 + max(left, right)
                    last = curr
                    curr = None
                else:
                    curr = curr.right
        return True
```