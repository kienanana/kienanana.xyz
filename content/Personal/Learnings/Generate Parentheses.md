---
class:
tags:
  - cs/strings
  - cs/dp
  - cs/backtracking
  - cs/bracket-sequences
  - leetcode/medium
source: https://leetcode.com/problems/generate-parentheses/
related:
author:
date: 2026-09-09
updated: 2026-09-09 15:18:48
aliases:
---
[[Leetcode]] #22

## Problem
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
	1 <= n <= 8

### My Solution (Backtracking)
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        - backtracking
            - build valid strings only 
            - int open , close 
            - only ) when open > close
            - can ( until limit n 
            - recurse 
        """
        res = []
        stack = []
        def backtrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                return

            # do not use elif, need to explore both options 
            if open > close:
                # explore adding )
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()

        backtrack(0,0) 
        return res
```

I had to look up the video for this one because I'm not familiar enough with the backtracking process yet, I knew recursion had to be involved, but without backtracking, it would just be an inefficient brute force method. The stack allows me to explore the adding of an open/closed bracket, then pop and explore the other option. Pretty nifty.

There's actually a DP approach as well, but realistically I don't think I was ever getting there, especially not in an interview setting.

### Dynamic Programming Solution:
> a valid parentheses string can be built from smaller valid strings.
- general pattern: ( left ) right
	- left is a valid parentheses string with i pairs
	- right is valid parentheses string with k-i-1 pairs
	- wrapping left with () guarantees balance 
	- appending right keeps the string valid 
- every valid result for k pairs is formed by combining smaller answers

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        - DP
        - ( left ) + right : k pairs
            - left: i pairs
            - right: k-i-1 pairs
        """
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n+1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)
        return res[-1]
```