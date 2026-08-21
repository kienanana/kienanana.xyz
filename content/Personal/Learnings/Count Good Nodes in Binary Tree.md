---
class:
tags:
  - cs/trees
  - cs/graphs
  - leetcode/medium
source: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
related:
author:
date: 2026-08-05
updated: 2026-08-05 16:36:27
aliases:
---
[[Leetcode]] #1448

I'm super rusty with graph traversal, so I spent reallyyyyy long staring at this and overcomplicating it in my head. This turned out to be much easier than I expected. 

## Problem
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
 
Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
	The number of nodes in the binary tree is in the range [1, 10^5].
	Each node's value is between [-10^4, 10^4].

### My Solution: 
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

/*
DFS helper:
- input treenode and max`
- if node.val >= max, count++
- update max
- returns number of good nodes 
    + dfs(left, newMax) + dfs(right, newMax)

- begin with dfs(root, root.val)
*/

class Solution {
    public int goodNodes(TreeNode root) {
       return DFS(root, root.val); 
    }

    private int DFS(TreeNode node, int max) {
        if (node == null) {
            return 0;
        }
        
        int count = (node.val >= max) ? 1 : 0;
        int newMax = Math.max(max, node.val);

        return count + DFS(node.left, newMax) + DFS(node.right, newMax); 
    }
}
```
