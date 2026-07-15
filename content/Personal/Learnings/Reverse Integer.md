---
class:
tags:
  - cs/math
  - leetcode/medium
source: https://leetcode.com/problems/reverse-integer/
related:
author:
date: 2026-05-25
updated: 2026-05-25 03:11:25
aliases:
---
[[Leetcode]] #7

Not much to be said here, just a Math problem. The only struggle here was passing some overflow cases, because i was updating ans before doing the overflow checks. Another thing I had to swap was:
> `int MAX = (int)Math.pow(2,31) - 1;`  
> `int MIN = -(int)Math.pow(2,31);` 

in my original solution to:
> `int MAX = 2147483647;`
> `int MIN = -2147483648;`

The reason is that Math.pow returns a double value, but that value is too large for an int, and java clamps 2147483648 to 2147483647 and MAX becomes off by 1. I actually could've also just used `Integer.MAX_VALUE` and `Integer.MIN_VALUE` apparently.

## Problem
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
	-231 <= x <= 231 - 1

## My Solution:
```java
class Solution {
    public int reverse(int x) {
        /*
        int num = x or -x if x<0
        int ans = 0
        int MAX = 2**31 - 1
        int MIN = -2**31
        - while num != 0:
            - rem = num%10
            - num = num/10
            - ans = ans*10 + rem
            - if ans > MAX or < MIN return 0 
        */
        int num = x;
        int ans = 0;
        int MAX = 2147483647;
        int MIN = -2147483648;

        while (num != 0) {
            int rem = num%10;
            num = num/10;
            if (ans > MAX/10 || (ans == MAX/10 && rem > MAX%10)) {
                return 0;
            }
            
            if (ans < MIN/10 || (ans == MAX/10 && rem > MAX%10)) {
                return 0;
            }
            ans = ans*10 + rem;
        }
        return ans;
    }
}
```
