---
class:
tags:
  - cs/arrays
  - cs/binary-search
  - cs/divide-and-conquer
  - leetcode/hard
source: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
related:
author:
date: 2026-05-09
updated: 2026-05-09 21:06:31
aliases:
---
[[Leetcode]] #4

Seeing the time complexity stated in the question prompted me to believe that a [[L4 Sorting#Merge Sort]] type of approach would be the ideal solution and I proceeded to implement that approach pretty quickly, only to be greeted with an abysmal runtime. Clearly I'm not the sharpest tool in the shed and haven't calculated time complexity in a while. 
## Problem
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 
Constraints:
	nums1.length == m
	nums2.length == n
	0 <= m <= 1000
	0 <= n <= 1000
	1 <= m + n <= 2000
	-106 <= nums1[i], nums2[i] <= 106

### My Unoptimal Solution

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /*
        - Merge sort: merge 2 sorted subarrays
        - int[] final
        - int i and j (nums1 and nums2 idx) 
        - int it (idx in final)
        - while i < m and j < n
            - compare nums1[i] and nums2[j] -> final[it++]
        - one of the arrays is done iterating:
            - if m>n add remaining from nums1
                - else (m<n) add remaining from nums2
        - int len = m+n
            - if len even (len%2 == 0)
                -  median = (final[len/2 -1] + final[len/2]) / 2
            - else (odd) 
                - median = final[len/2]
        */   
        int m = nums1.length;
        int n = nums2.length;
        int len = m+n;
        int[] fin = new int[m+n];
        int i = 0; int j = 0; int it = 0; 
    
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                fin[it++] = nums1[i++];
            } else {
                fin[it++] = nums2[j++];
            }
        }  

        // one of the arrays done iterating
        while (i < m) {
            fin[it++] = nums1[i++];
        } 
        while (j < n) {
            fin[it++] = nums2[j++];         
        }

        if (len%2 == 0) {
            return ((double)fin[len/2 -1] + (double)fin[len/2]) / 2;
        } else {
            return (double)fin[len/2]; 
        }

    }
}

// Time Complexity: O(m+n)
```

![[Screenshot 2026-05-10 at 1.03.42 AM.png]]
This was the moment I realised I'd been using the wrong sorting algorithm. 

## Optimal Solution - Binary Search

```java
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1;
        int[] B = nums2;
        int total = A.length + B.length;
        int half = (total + 1) / 2;

        if (B.length < A.length) {
            int[] temp = A;
            A = B;
            B = temp;
        }

        int l = 0;
        int r = A.length;
        while (l <= r) {
            int i = (l + r) / 2;
            int j = half - i;

            int Aleft = i > 0 ? A[i - 1] : Integer.MIN_VALUE;
            int Aright = i < A.length ? A[i] : Integer.MAX_VALUE;
            int Bleft = j > 0 ? B[j - 1] : Integer.MIN_VALUE;
            int Bright = j < B.length ? B[j] : Integer.MAX_VALUE;

            if (Aleft <= Bright && Bleft <= Aright) {
                if (total % 2 != 0) {
                    return Math.max(Aleft, Bleft);
                }
                return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2.0;
            } else if (Aleft > Bright) {
                r = i - 1;
            } else {
                l = i + 1;
            }
        }
        return -1;
    }
}
```




