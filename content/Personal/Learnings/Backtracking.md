---
class: note
tags:
  - cs/backtracking
source: https://www.geeksforgeeks.org/dsa/backtracking-algorithms/
related:
author:
date: 2026-10-14
updated: 2026-10-14 16:29:08
aliases:
---
Backtracking algorithms are like problem-solving strategies that help explore different options to find the solution. 
- work by trying out different paths and if one doesn't work, then backtrack and try another until the right one is found
- useful for problems where you must generate all valid combinations, permutations or subsets under constraints

Backtracking is not for optimisation problems like [[Dynamic Programming|DP]] , rather it is for when there are multiple solutions and you want all the solutions.
- Brute Force Approach
	- for any given problem, you should try all possible solutions and pick up desired solutions
- build state space tree with DFS

![[Pasted image 20261014165430.png]]

## General Outline of Backtracking Algorithm:
1. choose an initial solution
2. explore all possible extensions of the current solution
3. if an extension leads to a solution, return that solution
4. if an extension does not lead to a solution, backtrack to the previous solution and try a different extension
5. repeat steps 2-4 until all possible solutions have been explored




