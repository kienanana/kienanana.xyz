---
class:
tags:
  - cs/strings
  - cs/stacks
  - cs/bracket-sequences
  - leetcode/easy
source: https://leetcode.com/problems/valid-parentheses/
related:
author:
date: 2026-09-06
updated: 2026-09-06 21:52:18
aliases:
---
[[Leetcode]] #20

## Problem
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

### My Solution:
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in mappings:
                if stack and stack[-1] == mappings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
```
