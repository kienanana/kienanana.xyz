---
class:
tags:
  - cs/hashing
  - cs/strings
  - cs/sliding-window
  - leetcode/medium
source: https://leetcode.com/problems/longest-repeating-character-replacement/
related:
author:
date: 2026-09-06
updated: 2026-09-06 21:18:34
aliases:
---
[[Leetcode]] #424

## Problem
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
	1 <= s.length <= 105
	s consists of only uppercase English letters.
	0 <= k <= s.length

### My Solution:
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        - counts {}: count freq of chars
        - int res
        - sliding window:
            - l = 0
            - maxF = 0 (for optimal solution)
            - for r in range(len)
                    - add s[r] to
                    - update maxF
                    - currLen = r-l+1
                    - replacements = currLen - maxF
                    - replacements <= k 
                        - valid
                - while invalid:
                    - l++ 
                    - update counts
                - res = max(res, currLen)
        - return res
        """
        l = 0
        counts = {}
        res = 0
        for r in range(len(s)):
            c = s[r]
            counts[c] = counts.get(c, 0) + 1
            while (r-l+1) - max(counts.values()) > k:
                counts[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
```

![[Screenshot 2026-09-06 at 9.19.54 PM.png|304]]
? why everyone runtime mogging me like dat tho
anyways i watched NeetCode's video and the optimisation truly was beyond my puny brain's comprehension. it's a very simple change to the code itself, but it involves keeping track of a stale maximum, which seems really weird but it works? 

in the words of GPT:
> The important insight is: a stale `maxf` can prevent `l` from moving as much as it theoretically should, but it **cannot cause us to discover a new larger answer unless we've previously seen enough copies of some character to support a window of that size**.

> So the algorithm is effectively asking: "Given the highest frequency I've managed to achieve so far, can I maintain/grow a window whose remaining characters are at most `k`?"

### Optimal Solution:
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        maxF, res = 0, 0 # change here
        for r in range(len(s)):
            c = s[r]
            counts[c] = counts.get(c, 0) + 1
            maxF = max(maxF, counts[c]) # change here
            while (r-l+1) - maxF > k: # and here
                counts[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
```

![[Screenshot 2026-09-06 at 9.25.11 PM.png|306]]
the fuck man?
