---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/trees
module: CS2040
lecture: L11
source:
related:
  - "[[L10 BST]]"
date:
updated:
aliases:
---

> AVL Tree is a **self-balancing extension of [[L10 BST]]**. All BST operations apply, plus rotations to maintain h = O(log N).

## Step 1: Augment

- in every vertex x, we also store its height: x.height
- during insertion and deletion, we also update height
- height update can be added in insert() before the return
    - size can be updated the same

## Step 2: Define Invariant

- a vertex x is said to be **height-balanced** if

$$
|x.left.height - x.right.height| \leq 1 
$$

- a BST is said to be **height-balanced** if *every vertex* in the tree is height-balanced

## Step 3: Maintain Height-Balance

- **bf(x) = x.left.height - x.right.height**
    - aft insertion, from insertion point, check bf of each vertex up to the root
    - once we have vertex with bf +2 or -2, have to rebalance it

## Tree Rotations

![[Screenshot_2024-11-20_at_4.42.22_PM.png]]

![[Screenshot_2024-11-20_at_4.42.42_PM.png]]

```java
Vertex rotateLeft(Vertex T) {
        Vertex w = T.right;
        w.parent = T.parent;
        T.parent = w;
        T.right = w.left;
        if (w.left != null) {
            w.left.parent = T;
        }
        w.left = T;

        // update heights and sizes
        // update height of T then W
        w.size = T.size;
        updateHeight(T);
        updateSize(T);
        updateHeight(w);

        return w;
    }

    Vertex rotateRight(Vertex T) {
        Vertex w = T.left;
        w.parent = T.parent;
        T.parent = w;
        T.left = w.right;
        if (w.right != null) {
            w.right.parent = T;
        }
        w.right = T;

        // same from here
    }
```

![[image 2.png]]

![[Screenshot_2024-11-20_at_4.50.16_PM.png]]

## Insertion / Deletion

- insert / delete key as in normal BST
- walk up the AVL tree from the insertion / deletion point to root
    - at every step, update height and check bf
    - if vertex out of balance (+2 / -2), use rotations to rebalance
    - Insertion: only trigger one of the four cases once
    - Deletion: may trigger one of the four cases several times, up to h = log N times

![[Screenshot_2024-11-20_at_4.28.06_PM.png]]

![[Screenshot_2024-11-20_at_4.36.32_PM.png]]

![[Screenshot_2024-11-20_at_4.38.08_PM.png]]

![[Screenshot_2024-11-20_at_4.38.40_PM.png]]

```java
// recursive function to insert a new key in the AVL tree
    Vertex insert(Vertex T, String v) {
        // normal BST insertion
        if (T == null) { // insertion point is found
            return new Vertex(v);          
        }
        if (T.key.compareTo(v) < 0) {       
            // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        } else if (T.key.compareTo(v) > 0) {
	        // search to the left                            
            T.left = insert(T.left, v);
            T.left.parent = T;
        } else { // duplicate 
            return T;
        }

        // update height and size of node
        updateHeight(T);                                          
        updateSize(T);

        // check balance factor and balance tree 
        int bf = balanceFactor(T);

        // possible cases
        if (bf > 1) {
            // Left Right
            if (balanceFactor(T.left) < 0) {
                T.left = rotateLeft(T.left);
            }
            // Left Left
            T = rotateRight(T);
        }

        if (bf < -1) {
            // Right Left
            if (balanceFactor(T.right) > 0) {
                T.right = rotateRight(T.right);
            }
            // Right Right
            T = rotateLeft(T);
        }
        return T;
    }

```

- starting LR / LL
    - bf(x) = -2, -1 ≤ bf(x.left) ≤ 0 (LL)
        - rightRotate(x)
    - bf(x) = +2, bf(x.left) = -1 (LR)
        - leftRotate(x.left)
    - rightRotate(x)
- starting RL / RR
    - bf(x) = -2, -1 ≤ bf(x.right) ≤ 0 (RR)
        - leftRotate(x)
    - bf(x) = +2, bf(x.right) = 1 (RL)
        - rightRotate(x.right)
    - leftRotate(x)
    
    **Rotation stuff: (AVL)**
    
    ![[IMG_12EF01221D94-1.jpeg]]
    
    ![[IMG_B9B691E217D5-1.jpeg]]
    

![[Screenshot_2024-11-20_at_4.59.49_PM.png]]
