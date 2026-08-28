---
class:
tags:
  - cs/arrays
  - cs/hashing
  - cs/strings
  - cs/sorting
  - leetcode/medium
source: https://leetcode.com/problems/group-anagrams/
related:
author:
date: 2026-08-27
updated: 2026-08-27 14:13:04
aliases:
---
[[Leetcode]] #49

## Problem
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
> There is no string in strs that can be rearranged to form "bat". 
> The strings "nat" and "tan" are anagrams as they can be rearranged to form each other. 
> The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:
	1 <= strs.length <= 104
	0 <= strs[i].length <= 100
	strs[i] consists of lowercase English letters.

### My Solution
```java
/*
- sort each str
- HashMap<String, List<String>> map 
    - K: sorted str
    - V: indexes of words with that sorted str
*/
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        int len = strs.length;
        for (int i = 0; i < len; i++) {
            String word = strs[i];
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);

            List<String> wordList = map.getOrDefault(sortedWord, new ArrayList<>());
            wordList.add(word);
            map.put(sortedWord, wordList);
        }
        return new ArrayList<>(map.values());

    }
}
```
