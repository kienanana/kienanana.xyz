---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/sorting
module: CS2040
lecture: L4
source:
related:
  - "[[L5 Lists]]"
  - "[[L8 Heap]]"
date:
updated:
aliases:
---

![[Screenshot_2024-09-04_at_2.17.33_AM.png]]

## Selection Sort

![[Screenshot_2024-09-04_at_2.20.30_AM.png]]

![[Screenshot_2024-09-04_at_2.23.12_AM.png]]

## Bubble Sort

![[Screenshot_2024-09-04_at_2.22.36_AM.png]]

![[Screenshot_2024-09-04_at_2.24.09_AM.png]]

![[Screenshot_2024-09-04_at_2.25.07_AM.png]]

## Insertion Sort

![[Screenshot_2024-09-04_at_2.27.03_AM.png]]

![[Screenshot_2024-09-04_at_2.28.40_AM.png]]

## Merge Sort

![[Screenshot_2024-09-04_at_2.30.10_AM.png]]

![[Screenshot_2024-09-04_at_2.30.31_AM.png]]

![[Screenshot_2024-09-04_at_2.30.49_AM.png]]

![[Screenshot_2024-09-04_at_2.31.06_AM.png]]

![[Screenshot_2024-09-04_at_2.31.36_AM.png]]

![[Screenshot_2024-09-04_at_2.32.18_AM.png]]

![[Screenshot_2024-09-04_at_2.32.45_AM.png]]

![[Screenshot_2024-09-04_at_2.33.43_AM.png]]

![[Screenshot_2024-09-04_at_2.34.50_AM.png]]

## Quick Sort

![[Screenshot_2024-09-04_at_2.35.14_AM.png]]

![[Screenshot_2024-09-04_at_2.35.45_AM.png]]

![[Screenshot_2024-09-04_at_2.36.24_AM.png]]

![[Screenshot_2024-09-04_at_2.37.39_AM.png]]

![[Screenshot_2024-09-04_at_2.38.08_AM.png]]

![[Screenshot_2024-09-04_at_2.38.44_AM.png]]

![[Screenshot_2024-09-04_at_2.39.10_AM.png]]

![[Screenshot_2024-09-04_at_2.39.57_AM.png]]

## Radix Sort

![[Screenshot_2024-09-04_at_2.41.31_AM.png]]

![[Screenshot_2024-09-04_at_2.41.42_AM.png]]

## HeapSort

→ see [[L8 Heap]] for full implementation — uses a max-heap, O(N log N), in-place but not cache friendly.

## Comparison of Sorting Algorithms

![[Screenshot_2024-09-04_at_2.44.57_AM.png]]

![[Screenshot_2024-09-04_at_2.45.31_AM.png]]

![[Screenshot_2024-09-04_at_2.45.49_AM.png]]

---

![[Screenshot_2024-09-04_at_2.46.51_AM.png]]

---

| ***Algorithm***    | ***Approach***                                                                                                                                                                                                                                                                                                           | ***No. of Comparisons***                              | ***Best / Worst Case***                                                                                                                                                                                                                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Selection Sort** | each iteration, find minimum, move to front<br>or<br>Every iteration, find largest element in unsorted region, swap with last element in unsorted region.                                                                                                                                                                | (n-1) + (n-2) + … + 1<br>TAKE NOTE OF WHO U SWAP WITH | **Best:**<br>- input already in ascending order<br>- algorithm returns after a single iteration in the outer loop<br>- O(n)<br><br>**Worst:**<br>- input in descending order<br>- n-1 outer loops required<br>- running time same, O(n^2)                                                                                     |
| **Insertion Sort** | for each element, pull out, move downwards and insert at correct spot<br>ie.<br>Starting with the second element, shift it to its left until it encounters an element <= it. Repeat for the following elements.                                                                                                          | depends where u stop                                  | **Best:**<br>- array already sorted, hence a[j] > next is always false<br>- no shifting of data necessary, inner loop not executed at all<br>- O(n)<br><br>**Worst:**<br>- array reversely sorted, hence a[j] > next is always true<br>- need i shifts for i = 1 to n-1<br>- insertion always occurs at the front<br>- O(n^2) |
| **Bubble Sort**    | comparisons between A[i] and A[i+1] up to last 2 unsorted                                                                                                                                                                                                                                                                | (n-1) + (n-2) + … + 1                                 | [improved version]<br>**Best:**<br>- input already in ascending order<br>- algorithm returns after single iteration in the outer loop<br>- O(n)<br><br>**Worst:**<br>- input in descending order<br>- n-1 iterations in the outer loop needed<br>- O(n^2) running time same                                                   |
| **Merge Sort**     | keep halving until individual elements, sort and merge into subarray of 2, then 4, until n/2 and n                                                                                                                                                                                                                       |                                                       | O(nlogn) — divide-and-conquer, uses auxiliary array (compare with [[L8 Heap\|HeapSort]] which is in-place)                                                                                                                                                                                                                    |
| **Radix Sort**     | Treat each element as a character string. Starting with the least significant digit (character), group each element based on that digit. Repeat for the remaining digits.                                                                                                                                                |                                                       | O(d*n)<br>- d = max number of digits of the n numeric strings in the array<br>- if d is fixed or bounded: **O(n)**                                                                                                                                                                                                            |
| **Quick Sort**     | select a pivot, partition the array into two subarrays (elements smaller than the pivot go to the left, larger to the right), and recursively apply the same logic to the subarrays.<br>ie.<br>Choose pivot (first element in this course), divide array into two parts (<p and >=p), quick sort on each of those parts. |                                                       | **Best:**<br>- partition always splits array into 2 equal halves<br>- depth of recursion is logn<br>- each level takes n or fewer comparisons<br>- O(n log n)<br><br>**Worst:**<br>- worst case is rare, and on average, we get some good splits and bad splits<br><br>**Average:**<br>- O(n log n)                           |

