---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/data-structures
module: CS2040
lecture: L8
source:
related:
  - "[[L4 Sorting]]"
  - "[[L10 BST]]"
  - "[[L14 MST]]"
  - "[[L15-16 SSSP]]"
date:
updated:
aliases:
---

## Complete Binary Tree

- every level, except possibly the last is completely filled, all nodes as far left as possible
- every level including last is filled → Perfect binary tree
- N items → **height O(logN)**

```jsx
Insert(v)
	heapsize = heapsize + 1; // extend, O(1)
	A[heapsize] = v // insert at back, O(1)
	ShiftUp(heapsize) // fix the heap property, **O(log n)**
	
Shiftup(i) // **O(log n)**
	// while not root and violates max heap property
	while i > 1 and A[parent(i) < A[i]: 
		swap(A[i], A[parent(i))
		i = parent(i)
		
ExtractMax()
	maxV = A[1] 
	A[1] = A[heapsize] // replace root with last element
	heapsize -= 1
	ShiftDown(1) // **O(log n)**
	return maxV
	
ShiftDown(i) // or heapify
	while i <= heapsize: // **O(log n) (height)**
		maxV = A[i]; max_id = i;
		// check both directions, find larger
		if left(i) <= heapsize and maxV < A[left(i)]:
			maxV = A[left(i)]; max_id = left(i)
		if right(i) <= heapsize and maxV < A[right(i)]:
			maxV = A[right(i)]; max_id = right(i)
		if (max_id != i):
			swap(A[i], A[max_id])
			i = max_id;
		else:
			break
			
CreateHeap(arr) // **O(N) version**
	N = size(arr)
	A[0] = 0 // dummy entry
	for i = 1 to N:
		A[i] = arr[i-1] // copy content O(N)
	// from parent of last element to root
	for i = parent(N) down to 1: // O(N/2)
		ShiftDown(i) // O(log N), shiftdown all internal nodes
								 // including root
```

![[Screenshot_2024-11-20_at_12.05.14_PM.png]]

```jsx
HeapSort(arr) // **O(NlogN)**
	CreateHeap(arr) // O(N)
	N = size(arr)
	for i from 1 to N: // O(N)
		A[N-i+1] = ExtractMax() // O(log N)
	return A
```

![[image.png]]

![[Screenshot_2024-11-20_at_11.38.02_AM.png]]

![[Screenshot_2024-11-20_at_11.53.33_AM.png]]

- **UpdateKey(i, new)** → **O(log N)**
- **Delete(i)** → make value 1 more than root (O(1)), ShiftUp (O(log n)), ExtractMax (O(log n)) → **O(log N)**

### CreateHeap (O(N) Version)

![[Screenshot_2024-11-20_at_12.00.02_PM.png]]

- parent(i) = floor(i/2) → somewhere in the middle
- NOT O(N log N) because this is not tight bound
    - height floor(log N), cost to shiftdown(i): O(log N), no. of nodes at level h of perfect binary tree: ceiling(N / 2^h+1)

![[Screenshot_2024-09-24_at_2.22.07_PM.png]]

### HeapSort (O(n log n))

- with a binary (max) heap, call ExtractMax() N times
- do not need extra array like merge sort, more memory friendly
- in-place sorting, but not cache friendly
- → see [[L4 Sorting]] for comparison with other O(n log n) algorithms (Merge Sort, Quick Sort)

## Priority Queue (min-heap)
- **Prim's Algorithm** → [[L14 MST]] (process lowest-weight edge first)
- **Dijkstra's Algorithm** → [[L15-16 SSSP]] (process nearest unvisited vertex first)
- BST can also implement PQ but heap is simpler → [[L10 BST]]

extra: heap rank example

![[Screenshot_2024-11-20_at_3.22.02_PM.png]]
