---
class:
tags:
  - cs/trees
  - cs/graphs
  - cs/binary-lifting
  - cs/lowest-common-ancestor
  - leetcode/medium
source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
related:
author:
date: 2026-09-28
updated: 2026-09-28 14:30:52
aliases:
---
[[Leetcode]] #235

## Problem

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
 
Constraints:
	The number of nodes in the tree is in the range [2, 105].
	-109 <= Node.val <= 109
	All Node.val are unique.
	p != q
	p and q will exist in the BST.

### My Solution (Recursion):
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        - bst is sorted!
        - if p and q <= root:
            - search left subtree
        - elif p and q >= root:
            - search right subtree
        else:
            - return root
        """
        if p.val < root.val and q.val < root.val:
            # search left
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            # search right
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```

### My Iterative Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iteration 
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                # search left
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
```