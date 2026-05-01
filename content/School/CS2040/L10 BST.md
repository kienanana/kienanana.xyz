---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/trees
module: CS2040
lecture: L10
source:
related:
  - "[[L7 Hashing]]"
  - "[[L8 Heap]]"
  - "[[L11 AVL Tree]]"
date:
updated:
aliases:
---

![[Screenshot_2024-11-20_at_1.09.57_PM.png]]

- worst case height: h = O(N)
- left to right: ascending order
- Select(k): return the value of the k-th smallest element (1-based index)
- Rank(v): return the rank k of element with value v
- **For every node in the BST, the value of every node in its left subtree must be smaller than it, and the value of every node in its right subtree must be greater than it**

## Traversal

- **inorder**
    - a vertex is visited three times during inorder traversal (from parent and from left + right children)
    - **O(N)**

![[Screenshot_2024-11-20_at_2.22.29_PM.png]]

```jsx
inorder(N) // 4 2 5 1 3 6
	if N != null:
		inorder(N.left)
		process(N) // print
		inorder(N.right)
		
preorder(N) // 1 2 4 5 3 6
	if N != null:
		process(N) // print
		inorder(N.left)
		inorder(N.right)
		
postorder(N) // 4 5 2 6 3 1
	if N != null:
		inorder(N.left)
		inorder(N.right)
		process(N) // print
		
```

### Extra

- how many nodes in a perfect BST of height h?
    - **2^h+1 - 1**
    - height of a perfect BST with N nodes is **log N**

![[Screenshot_2024-11-20_at_2.34.57_PM.png]]

## Deletion

```java
delete(x, T)
	// case 1
	if T has no children
		if x == T.item
			return empty tree
		else return NOT FOUND
		
	// case 2
	if T has only 1 child 
		// 2A
		if left child
			if x == T.item
				return T.left
			else if x < T.item
				T.left = delete(x, T.left)
			else return NOT FOUND
		return T
		
		// 2B
		if right child 
			if x == T.item
				return T.right
			else if x > T.item
				T.right = delete(x, T.right)
			else return NOT FOUND
		return T
		
	// case 3
	if T has 2 children
		if x == T.item
			// replace T.item by 
			// min item of right subtree
			T.item = findMin(T.right)
			// delete original copy of min item 
			// from right subtree
			T.right = delete(T.item, T.right)
		else if x < T.item
			T.left = delete(x, T.left)
		else // x > T.item
			T.right = delete(x, T.right)
	return T
			
```

1. **Parent index**: parent(i) = ⌊(i-1)/2⌋

$$
\text{parent}(i) = \lfloor \frac{i - 1}{2} \rfloor
$$

(if i>0, since the root node does not have a parent).

2. **Left child index**: left(i) = 2i+1

$$
\text{left}(i) = 2i + 1
$$

(if 2i+1 is within the bounds of the array).

3. **Right child index**: right(i) = 2i+2

$$
\text{right}(i) = 2i + 2
$$

(if 2i+2 is within the bounds of the array).

```java
// rank, select
function RANK(node, v)
	if node.key = v then
		return node.left.size + 1
	else if node key > v then
		return RANK(node.left, v)
	else
		return node.left.size + 1 + RANK(node.right, v)
	end if 
end function 

function SELECT(node, k)
	q = node.left.size
	if q + 1 = k then
		return node.key
	else if q + 1 > k then
		return SELECT(node.left, k)
	else
		return SELECT(node.right, k-q-1)
	end if
end function
```

- **search(v):**
    - if v > cur, go right, if v < cur go left
    
    ```java
    // iterative solution
    while T is not empty
    	if T.item == x 
    		return T
    	else if T.item > X then
    		T = T.left
    	else 
    		T = T.right
    return null // T is empty, so X is not in T
    
    // recursive solution
    Search(x, T)
    	if T is empty
    		return null // x is not in T
    	if  x == T.item 
    		return T
    	else if x < T.item
    		return search(x, T.left)
    	else 
    		return search(x, T.right)
    ```
    
    - runs in **O(h)**
- **findMin() / findMax():**
    - traverse to leftmost / rightmost
    - **O(h)**
- **insert(v):**
    
    ![[Screenshot_2024-11-20_at_1.34.56_PM.png]]
    
    ```java
    insert(x, T)
    	if T is empty
    		return new TreeNode(x) // tree w only node x
    	else if x < T.item
    		T.left = insert(x, T.left)
    	else if x > T.item
    		T.right = insert(x, T.right)
    	else
    		return ERROR! // X already in T, x = T.item
    	return T // return the new tree T
    	// this method assumes that we don't allow
    	// duplicate key values in the BST
    ```
    
    - **O(h)**
- **successor(v):**
    - minimum in RIGHT subtree
    - else keep going up until right turn
    - **O(h)**
- **predecessor(v):**
    - maximum in LEFT subtree
    - else keep going up until left turn
    - **O(h)**

![[Screenshot_2024-11-20_at_2.26.18_PM.png]]

### Deletion Analysis

- Delete a BST vertex v, find v in O(h), then three cases:
    - v has **no children:**
        - just remove the corresponding vertex v → O(1)
    - v has **1 child:**
        - **connect** **v.left (or v.right) to v.parent** and vice versa → O(1)
        - then remove v → O(1)
    - v has **2 children:** (replace v with successor)
        - find **x = successor(v)** → O(h)
        - **replace v.key with x.key** → O(1)
        - **delete x in v.right** (otherwise have duplicate) → O(h)
    - running time: **O(h)**
    
    **Implementations:**
    
    ![[Screenshot_2024-11-20_at_2.56.29_PM.png]]
    
    ![[Screenshot_2024-11-20_at_2.56.57_PM.png]]
    
    ![[Screenshot_2024-11-20_at_2.58.16_PM.png]]
    
    height, size
    
    ```java
    height(T)
    	if T is empty
    		return -1
    	else 
    		return 1 + max(height(T.left), 
    			height(T.right))
    		
    	size(T)
    		if T is empty
    			return 0
    		else 
    			return 1 + size(T.left) + size(T.right)
    ```
    
    ![[IMG_3A6723C04A94-1.jpeg]]
    

![[image 1.png]]

**h = O(log N) for balanced BST**, **O(n) worst case for unbalanced**, N = num of nodes

> **Unbalanced BST degrades to O(N)** — fixed by [[L11 AVL Tree]] (self-balancing, guarantees h = O(log N))
> **BST vs Hashing** → [[L7 Hashing]]: BST supports ordered ops (range query, rank, select, successor); hashing is O(1) average but unordered
> **BST vs Heap** → [[L8 Heap]]: Heap only supports min/max efficiently; BST supports search, insert, delete on any key
