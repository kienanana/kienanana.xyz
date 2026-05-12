---
class:
tags:
  - cs/hashing
  - cs/strings
  - cs/sliding-window
  - leetcode/medium
source: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
related:
author:
date: 2026-05-05
updated: 2026-05-05 23:01:12
aliases:
---
[[Leetcode]] #3

This one took me wayyy longer than it should've, and while I know fully well that the beginning of this process of getting back into regular Leetcoding was always going to be painful and slow, I'm kinda appalled at how slow and how rusty I've become. 
- my first attempt did use a Hashmap, but calculated the substring length wrongly by using the current index and subtracting the previous index of the current character 
- took a while to brainstorm but I did have the right thought process that led me to a [[misc#Sliding Window | Sliding Window]] approach 
- I had to resolve two edge cases which involved Blank (" ") / Empty ("") Strings, turns out it was just a reordering of some logic: inserting the val into the hash only after updating left 

## Problem
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.

### My Solution: 

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
        HashMap: char, latest idx
        int left = left boundary of current window 

        Sliding Window: 
        - iterate index i 
        - substring is s[left, i]    
        - char c = s[i]    
        - if c is in substring, left = hash.get(c)+1
        - hash.replace(c, i)
        - ans = max(ans, i-left+1)
        */

        int ans = 0;
        int left = 0;
        HashMap<Character, Integer> chars = new HashMap<>();
        int len = s.length();

        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);

            if (chars.containsKey(c) && chars.get(c) >= left) {
                left = chars.get(c)+1;
            }
            
			chars.put(c, i);
            ans = Math.max(ans, i-left+1);
        }

        return ans;
    }
}
```

