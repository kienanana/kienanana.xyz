---
class:
tags:
  - cs/arrays
  - cs/dp
  - leetcode/easy
source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
related:
author:
date: 2026-09-04
updated: 2026-09-04 17:24:06
aliases:
---
[[Leetcode]] #121

## Problem
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
	1 <= prices.length <= 105
	0 <= prices[i] <= 104

### My Really Bad Solution (Two Pointer)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        - l,r = 0,1 
        - if profit > 0:
            - update maxProfit
            - r++
        - if profit < 0:
            - move l to r
            - new cheaper starting point  
        """
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            else:
                l=r
            r+=1
        return maxProfit
```

clearly this was not a good attempt. 

![[Screenshot 2026-09-04 at 5.25.14 PM.png|231]]

### Optimal Solution (DP)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        - DP
        - minStart
        - maxProfit
        - profit = price - minStart 
        """
        minStart = prices[0] 
        maxProfit = 0
        for price in prices:
            minStart = min(minStart, price)
            maxProfit = max(maxProfit, price - minStart)
        return maxProfit
```

there we go.