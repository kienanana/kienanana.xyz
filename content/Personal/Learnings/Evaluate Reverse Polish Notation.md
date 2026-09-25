---
class:
tags:
  - cs/arrays
  - cs/math
  - cs/stacks
  - leetcode/medium
source: https://leetcode.com/problems/evaluate-reverse-polish-notation/
related:
author:
date: 2026-09-09
updated: 2026-09-09 14:24:08
aliases:
---
[[Leetcode]] #150

## Problem
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

	The valid operators are '+', '-', '*', and '/'.
	Each operand may be an integer or another expression.
	The division between two integers always truncates toward zero.
	There will not be any division by zero.
	The input represents a valid arithmetic expression in a reverse polish notation.
	The answer and all the intermediate calculations can be represented in a 32-bit integer.

 
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

 
Constraints:

	1 <= tokens.length <= 104
	tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

### My Solution:
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        - stack [] : store nums 
        - for c in tokens
            - if num, stack.append
            - if operator
                - b = pop(), a = pop() 
                - a operator b 
        """        
        stack = []
        operators = {"+": lambda a,b : a+b,
                    "-": lambda a,b : a-b,
                    "*": lambda a,b : a*b,
                    "/": lambda a,b : int(a/b)}
        for c in tokens:
            if c in operators:
                b = stack.pop()
                a = stack.pop()
                
                res = operators[c](a,b)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack.pop()
```

i was trying to save some time and avoid having to write out every if else case, but that actually made my solution way slower and less memory-efficient. sucks to be me. 

### Optimal Solution:
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
```

