---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/medium
source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
related:
author:
date: 2026-10-01
updated: 2026-10-01 19:58:46
aliases:
---
[[Leetcode]] #230

## Problem
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
 
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:
	The number of nodes in the tree is n.
	1 <= k <= n <= 104
	0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

### My Solution (Recursive DFS):
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        - inorder traversal
        - if not node
            - return nothing
        - inorder(left)
        - # now this node is traversed
        - count++ 
        - # so now traverse curr
        - if count == k: return node.val
        - # right child
        - inorder(right) 

        ! propagate answer back up through the levels
        """
        count = 0
        def inorder(node):
            nonlocal count
            if node:
                leftResult = inorder(node.left)
                # must eval to not None
                ## if result is 0, evals to False
                if leftResult is not None: 
                    return leftResult
                # add count only when traversing CURRENT 
                count += 1
                if count == k:
                    return node.val
                rightResult = inorder(node.right)
                if rightResult is not None:
                    return rightResult
        return inorder(root)
```

my solution actually ended up resembling the optimal recursive dfs, but differs in how the answer is propagated up.

### Cleaner Recursive DFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # dfs inorder traversal
        count = 0
        res = root.val

        def dfs(node):
            nonlocal count
            nonlocal res
            if not node:
                return 
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return res
            dfs(node.right)
        
        dfs(root)
        return res
```

### Optimal Iterative DFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # dfs inorder traversal
        curr = root
        stack = []

        while stack or curr:
            # all the way left 
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            # traverse right
            curr = curr.right
```

### My Inorder Traversal Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # dfs inorder traversal
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node)
            dfs(node.right)
        dfs(root)
        return arr[k-1].val

                
```