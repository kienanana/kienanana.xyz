---
class:
tags:
  - cs/trees
  - cs/graphs
  - cs/string-matching
  - cs/hash-function
  - leetcode/easy
source: https://leetcode.com/problems/subtree-of-another-tree/
related:
author:
date: 2026-09-28
updated: 2026-09-28 00:18:30
aliases:
---
[[Leetcode]] #572

need to know how to solve [[Same Tree]] before solving this.

## Problem
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
	The number of nodes in the root tree is in the range [1, 2000].
	The number of nodes in the subRoot tree is in the range [1, 1000].
	-104 <= root.val <= 104
	-104 <= subRoot.val <= 104

### My Solution (BFS):
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        """
        - bfs for starting point (curr == subRoot)
            - BFS from starting point and subRoot
                - isSameTree
        """
        nodes = deque([root])
        while nodes:
            curr = nodes.popleft()
            if curr.val == subRoot.val:
                q1 = deque([curr])
                q2 = deque([subRoot])
                same = True
                while q1 and q2:
                    a = q1.popleft()
                    b = q2.popleft()
                    if not a and not b:
                        continue
                    elif not a or not b or a.val != b.val:
                        same = False
                        break
                    else:
                        q1.append(a.left)
                        q1.append(a.right)
                        q2.append(b.left)
                        q2.append(b.right)
                if same: return True
            if curr.left: nodes.append(curr.left)
            if curr.right: nodes.append(curr.right)
        return False
```

DFS actually is the cleaner fit and much simpler to implement here. this is because subtree equality depends on matching the entire structure below a node. i mean in the end the time complexity is about the same for both: O(n * m). 

### My Recursive DFS Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        """
        - recursive dfs
            - def isSameTree
            - traverse to starting point curr == subRoot
                - isSameTree
        """
        if not subRoot:
            return True
        if not root:
            return False 

        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self,a,b):
        if not a and not b:
            return True
        elif a and b and a.val == b.val:
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
        else:
            return False
```



