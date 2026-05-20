---
class: note
tags:
  - cs/dp
source:
related:
author:
date: 2026-05-17
updated: 2026-05-17 01:01:28
aliases:
  - DP
---
I've been coming across a bunch of DP questions on [[Leetcode]], so I think it's about time I self-learn it properly once and for all. 

Dynamic Programming (DP) is a method used to solve complex problems by breaking them into smaller or overlapping subproblems and storing their results to avoid recomputation. It is an optimisation technique that transforms recursive solutions with exponential time into efficient ones with polynomial time. 
- the core idea is to store solutions to subproblems so that each is solved only once
- we first write a recursive solution in a way that there are overlapping subproblems in the recursion tree (the recursive function is called with the same parameters multiple times) 
- to make sure that a recursive value is computed only once, we store the results of the recursive calls 
- there are **2 ways** to store the results, one is *top down (memoization)* and the other is *bottom up (tabulation)*. 

## When to Use DP? 
### 1. Optimal Substructure 
This means that we use the optimal results of subproblems to achieve the optimal result of the bigger problem. 

Example: 
> Consider the problem of finding the minimum cost path in a weighted graph from a source node to a destination node. We can break this problem down into smaller subproblems:
> - Find the minimum cost path from the source node to each intermediate node.
> - Find the minimum cost path from each intermediate node to the destination node.
> The solution to the larger problem (finding the minimum cost path from the source node to the destination node) can be constructed from the solutions to these smaller subproblems.

### 2. Overlapping Subproblems
This means that solutions to the same subproblems are needed again and again. Store these computed solutions to subproblems in a table so that they don't have to be recomputed. 

Example:
> Consider the problem of computing the [Fibonacci series](https://www.geeksforgeeks.org/dsa/program-for-nth-fibonacci-number/). To compute the Fibonacci number at index ***n***, we need to compute the Fibonacci numbers at indices ***n-1*** and ***n-2***. This means that the subproblem of computing the Fibonacci number at index ***n-2*** is used twice (note that the call for n - 1 will make two calls, one for ***n-2*** and other for ***n-3***) in the solution to the larger problem of computing the Fibonacci number at index ***n***.
> 
> You may notice overlapping subproblems highlighted in the second recursion tree for Nth Fibonacci diagram shown below.


## Approaches of DP
### 1. Top-Down Approach (Memoization) 
We keep the solution recursive and add a memoization table to avoid repeated calls of same subproblems. 
- Before making a recursive call, we first check if the memoization table already has a solution for it
- After the recursive call is over, we store the solution in the memoization table 

### 2. Bottom-Up Approach (Tabulation) 
We start with the **smallest subproblems** and gradually build up to the final solution. 
- write an iterative solution (avoid recursive overhead) and build the solution in bottom-up manner 
- use a dp table where we first fill the solution for base cases and then fill the remaining entries of the table using recursive formula 
- only use recursive formula on table entries and do not make recursive calls 

|                        | Memoization                                                                                                                                                                   | Tabulation                                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **State**              | State transition relation is easy to think                                                                                                                                    | State transition relation is difficult to think                                                                                                                      |
| **Code**               | Code is easy to write by modifying the underlying recursive solution.                                                                                                         | Code gets complicated when a lot of conditions are required                                                                                                          |
| **Speed**              | Slow due to a lot of recursive calls.                                                                                                                                         | Fast, as we do not have recursion call overhead.                                                                                                                     |
| **Subproblem solving** | If some subproblems in the subproblem space need not be solved at all, the memoized solution has the advantage of solving only those subproblems that are definitely required | If all subproblems must be solved at least once, a bottom-up dynamic programming algorithm definitely outperforms a top-down memoized algorithm by a constant factor |
| **Table entries**      | Unlike the tabulated version, all entries of the lookup table are not necessarily filled in memoized version. The table is filled on demand.                                  | In the tabulated version, starting from the first entry, all entries are filled one by one                                                                           |


## Example of DP 
### Example 1: Fibonacci Sequence 
> *Fibonacci sequence:* 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

![[Pasted image 20260517011913.png]]

#### Using Memoization Approach - O(n) Time and O(n) Space
- take a memo array initialised to -1 
- as we make a recursive call, we first check if value stored in memo array corresponding to that position is -1 
	- -1 indicates we haven't calculated it yet, have to recursively compute it 
- output must be stored in the memo array so that, next time, if the same value is encountered, it can be directly used from the memo array

```java
import java.util.Arrays;

class GFG {
	static int fibRec(int n, int[] memo) {
		// base case 
		if (n <= 1) {
			return n;	
		}	
		
		// to check if output already exists 
		if (memo[n] != -1) {
			return memo[n];	
		}
		
		// calculate and save output for future use 
		memo[n] = fibRec(n-1, memo) + fibRec(n-2, memo); 
		
		return memo[n];
	}
	
	static int fib(int n) {
		int[] memo = new int[n+1];
		Arrays.fill(memo, -1);
		return fibRec(n, memo);	
	}
	
	public static void main(String[] args) {
		int n = 5;
		System.out.println(fib(n));
	}
}
```


### Using Tabulation Approach - O(n) Time and O(n) Space
- use an array of *size (n+1)*, often called *dp[]*, to store Fibonacci numbers 
- array is initialised with base values at the appropriate indices 
	- such as dp[0] = 0 and dp[1] = 1 
- then iteratively calculate FIbonacci values from dp[2] to dp[n] by using dp[i] = dp[i-1] + dp[i-2]
- allows us to efficiently compute Fibonacci numbers in a loop 
- the value at dp[n] gives the Fibonacci number for the input n 

```java
import java.util.Arrays;

// function for calculating the n-th fibonacci number 
class GfG {
	static int fibo(n) {
		int[] dp = new int[n+1];
		
		// storing the independent values in dp 
		dp[0] = 0;
		dp[1] = 1;
		
		// using the bottom-up approach 
		for (int i = 2; i <= n; i++) {
			dp[i] = dp[i-1] + dp[i-2];	
		}	
		
		return dp[n];
	}
	
	public static void main(String[] args) {
		int n = 5;
		System.out.println(fibo(n));	
	}
}
```


## Common Algorithms that Use DP: 
- Longest Common Subsequence (LCS) 
- Longest Increasing Subsequence 
- [[L15-16 SSSP#Bellman-Ford]] Shortest Path 
- [[L17 APSP#Floyd-Warshall]] 
- Matrix Chain Multiplication 
- Fibonacci Sequence



