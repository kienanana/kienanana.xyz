---
class:
tags:
  - cs/two-pointers
  - cs/strings
  - cs/dp
  - leetcode/medium
source: https://leetcode.com/problems/longest-palindromic-substring/description/
related:
author:
date: 2026-05-15
updated: 2026-05-15 12:49:54
aliases:
---
[[Leetcode]] #5

This one took way too long for some reason. My solution is a two pointer approach, but the ideal solution actually utilises [Manacher's Algorithm](https://www.geeksforgeeks.org/dsa/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/) , which is used specifically for this problem - to find all palindromic substrings of a string in O(n) time. 

I also took an incredible picture while working on this problem yesterday evening. 

![[Pasted image 20260515143837.png | 400]]

## Problem
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
	1 <= s.length <= 1000
	s consist of only digits and English letters.

## My Two Pointer Solution:

```java
class Solution {
    public String longestPalindrome(String s) {
        /*
        - iterate through each char c in s
            - odd length palindrome:
                - set this as middle 
                - left and right idx -1 +1 respectively 
                - if left == right: continue 

            - if s.charAt(i) == s.charAt(i+1) -> even length
                - expand left and right from around this pair 
        */
        
        int len = s.length();
        if (len == 1) {
            return s;
        }

        int bestLeft = 0;
        int bestLen = 1;

        for (int i=0; i<len; i++) {
            // odd length palindrome  
            int left = i-1;
            int right = i+1;

            while (left>=0 && right<len && s.charAt(left) == s.charAt(right)) {
                int curLen = right-left+1;
                if (curLen > bestLen) {
                    bestLen = curLen;
                    bestLeft = left;
                }            
                left--;
                right++;
            }

            // even length palindrome  
            left = i;
            right = i+1;

            while (left>=0 && right<len && s.charAt(left) == s.charAt(right)) {
                int curLen = right-left+1;
                if (curLen > bestLen) {
                    bestLen = curLen;
                    bestLeft = left;
                }            
                left--;
                right++;
            }

        }

        return s.substring(bestLeft,bestLeft+bestLen);
    }
}
```


## Manacher's Algorithm Solution 

```java
public class Solution {
    public int[] manacher(String s) {
        StringBuilder t = new StringBuilder("#");
        for (char c : s.toCharArray()) {
            t.append(c).append("#");
        }
        int n = t.length();
        int[] p = new int[n];
        int l = 0, r = 0;
        for (int i = 0; i < n; i++) {
            p[i] = (i < r) ? Math.min(r - i, p[l + (r - i)]) : 0;
            while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 &&
                   t.charAt(i + p[i] + 1) == t.charAt(i - p[i] - 1)) {
                p[i]++;
            }
            if (i + p[i] > r) {
                l = i - p[i];
                r = i + p[i];
            }
        }
        return p;
    }

    public String longestPalindrome(String s) {
        int[] p = manacher(s);
        int resLen = 0, center_idx = 0;
        for (int i = 0; i < p.length; i++) {
            if (p[i] > resLen) {
                resLen = p[i];
                center_idx = i;
            }
        }
        int resIdx = (center_idx - resLen) / 2;
        return s.substring(resIdx, resIdx + resLen);
    }
}
```


