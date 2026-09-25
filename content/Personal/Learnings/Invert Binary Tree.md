---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/easy
source: https://leetcode.com/problems/invert-binary-tree/
related:
author:
date: 2026-09-24
updated: 2026-09-24 15:46:31
aliases:
---
[[Leetcode]] #226

## Problem
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

### My Solution (DFS):
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        - recursion
        - at each step left, right = invertTree(left), invertTree(right)
            - temp1 temp2
            - swap left right
            - if not left and not right break
        """
        if root and (root.left or root.right):
            temp1 = root.left
            temp2 = root.right
            root.left = self.invertTree(temp2)
            root.right = self.invertTree(temp1)
        return root
```

this can actually be cleaned up with a neat little swap

### Cleaner DFS:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        # clean way to swap
        ## rhs of eqn is evaluated first
        root.left, root.right = root.right, root.left 
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
```

there actually is another solution as well.

### Iterative DFS Solution:
- uses an explicit stack instead of recursion
	- pop top node, swap children
	- push children onto stack
	- continue until empty
- simulates the recursive dfs in an iterative manner and works well when recursion depth may be too large

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        - iterative DFS
            - using stack
        """
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
        
```

