---
class:
tags:
  - cs/hashing
  - cs/strings
  - cs/sorting
  - leetcode/easy
source: https://leetcode.com/problems/valid-anagram/
related:
author:
date: 2026-08-20
updated: 2026-08-20 23:10:36
aliases:
---
[[Leetcode]] #242
## Problem
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
	1 <= s.length, t.length <= 5 * 104
	s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

### My Solution:
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        // K: letter, V: count 
        HashMap<Character, Integer> mapA = new HashMap<Character, Integer>();
        HashMap<Character, Integer> mapB = new HashMap<Character, Integer>();
        if (s.length() != t.length()) {
            return false;
        }
        int len = s.length();
        for (int i = 0; i < len; i++) {
            mapA.put(s.charAt(i), mapA.getOrDefault(s.charAt(i), 0) + 1);
            mapB.put(t.charAt(i), mapB.getOrDefault(t.charAt(i), 0) + 1);
        }
        return mapA.equals(mapB);
    }
}
```

Horrendous runtime, kinda impressively bad honestly.
![[Screenshot 2026-08-20 at 11.11.38 PM.png]]

### Optimal Solution 
```java
/*
- There are 26 alphabets
- initialise Array of size 26, each val being count
- iterate through both
    - increase count for s[i]
	- decrease count for t[i]
- if any value in array not 0 at end, return false
*/

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        } 
        int[] count = new int[26];
        int len = s.length();
        for (int i = 0; i < len; i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int n : count) {
            if (n!=0) {
                return false;
            }
        }
        return true; 
    }
}
```

