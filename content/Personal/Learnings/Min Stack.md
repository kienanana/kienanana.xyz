---
class:
tags:
  - cs/stacks
  - cs/design
  - leetcode/medium
source: https://leetcode.com/problems/min-stack/
related:
author:
date: 2026-09-09
updated: 2026-09-09 13:03:58
aliases:
---
[[Leetcode]] #155

## Problem
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
	MinStack() initializes the stack object.
	void push(int value) pushes the element value onto the stack.
	void pop() removes the element on the top of the stack.
	int top() gets the top element of the stack.
	int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
 
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
	-231 <= val <= 231 - 1
	Methods pop, top and getMin operations will always be called on non-empty stacks.
	At most 3 * 104 calls will be made to push, pop, top, and getMin.

### My Solution (2 Stacks)
```python
class MinStack:
    """
    - two stacks 
        - values
        - minimums  
    """
    def __init__(self):
        self.stack = []        
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value) 

    def pop(self) -> None:
        p = self.stack.pop()
        if p == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

The optimal solution involves a pretty cool optimisation such that only one stack is required. I don't think I would've ever thought of it.

It stores *encoded values* instead of the actual numbers. The trick is to record the *difference* between the pushed value and the current minimum. Whenever a new minimum is pushed, we store a *negative encoded value*, which signals that the minimum has changed. Later, when popping such a value, we can decode it to restore the previous minimum. 

This way, the stack internally keeps track of all minimum updates without needing a second stack - giving constant time operations with minimal space.

### Optimal Solution: One Stack
```python
class MinStack:
    """
    - two stacks 
        - values
        - minimums  
    """
    def __init__(self):
        self.stack = []        
        self.min = float('inf')

    def push(self, value: int) -> None:
        # stack stores diffs with min
        if not self.stack:
            self.min = value
            self.stack.append(0)
        else: 
            self.stack.append(value - self.min) # this has to be before resetting min 
            if value < self.min:
                self.min = value
        
    def pop(self) -> None:
        if not self.stack:
            return

        p = self.stack.pop()
        # if diff -ve, it was min
        if p < 0:
            # prevMin = self.min - -ve diff
            self.min -= p

    def top(self) -> int:
        val = self.stack[-1] 
        if val > 0: 
            return val + self.min
        else:
            # -ve diff means min
            return self.min

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
