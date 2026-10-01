---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/easy
source: https://leetcode.com/problems/same-tree/
related:
author:
date: 2026-09-27
updated: 2026-09-27 19:22:41
aliases:
---
[[Leetcode]] #100

## Problem
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
 
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

 
Constraints:
	The number of nodes in both trees is in the range [0, 100].
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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        - recursive dfs
            - base case:
                - p, p.left, p.right == q, q.left, q.right
        """
        def dfs(a, b):
            if not a and not b:
                return True
            elif not (a and b):
                return False
            else:
                return (a.val == b.val) and dfs(a.left, b.left) and dfs(a.right, b.right)
        return dfs(p,q)
```

### Cleaner-Written Recursive DFS:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
```

### My Iterative DFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        - iterative dfs
            - stack [(p,q)]
            - both none: continue
            - check same val, append children
        """
        stack = [(p,q)]
        while stack:
            a, b = stack.pop()
            if not a and not b:
                continue
            else:
                if a and b and a.val == b.val:
                    stack.append((a.left, b.left))
                    stack.append((a.right, b.right))
                else:
                    return False
        return True
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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        - BFS
        - queue 1, 2
            - nodes: q1.popleft, q2.popleft
        """
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            a = q1.popleft()
            b = q2.popleft()
            if not a and not b:
                continue 
            elif not a or not b or a.val != b.val:
                return False
            else:
                q1.append(a.left)
                q1.append(a.right)
                q2.append(b.left)
                q2.append(b.right)
        return True
```