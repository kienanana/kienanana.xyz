---
class:
tags:
  - cs/two-pointers
  - cs/strings
  - leetcode/easy
source: https://leetcode.com/problems/valid-palindrome/
related:
author:
date: 2026-09-02
updated: 2026-09-02 17:50:47
aliases:
---
[[Leetcode]] #125

## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
	1 <= s.length <= 2 * 105
	s consists only of printable ASCII characters.

### My Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(char for char in s.lower() if char.isalnum())
        length = len(s2)
        for i in range(length//2):
            if (s2[i] != s2[length-1-i]):
                return False
        return True
```
