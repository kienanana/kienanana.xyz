---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/medium
source: https://leetcode.com/problems/binary-tree-right-side-view/
related:
author:
date: 2026-09-29
updated: 2026-09-29 17:21:46
aliases:
---
[[Leetcode]] #199

## Problem
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
 
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []
 
Constraints:
	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

### My DFS Solution: 
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        - res = []
        - int maxDepth
        - dfs(root, depth)
            - if depth > maxDepth: 
                - add right / left if not right
                - update maxDepth
            - dfs right / left if not right
        """ 
        res = []
        maxDepth = 0
        def dfs(node, depth):
            if node:
                nonlocal maxDepth
                if depth > maxDepth:
                    maxDepth = depth
                    res.append(node.val)
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        dfs(root,1)
        return res
```

### Cleaner DFS:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
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
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        - BFS
        - go to rightmost node of each level
        """
        q = deque()
        res = []
        if root:
            q.append(root)
        while q:
            rightNode = None
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        return res

```