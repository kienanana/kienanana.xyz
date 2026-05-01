---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/graphs
module: CS2040
lecture: L14
source:
related:
  - "[[L8 Heap]]"
  - "[[L9 UFDS]]"
  - "[[L12 Graphs]]"
  - "[[L13 Graph Traversal]]"
date:
updated:
aliases:
---

- **Connected, undirected, weighted** graph with lowest weight of spanning tree
- remove largest edge from a cycle
- **Cycle Property:** if a cycle is formed after adding an edge, it must be the edge with the greatest weight in the cycle, as all the other edges in the cycle have been added earlier

## Algorithms

*greedy: select best possible choice at each step*

- **Jarnik's / Prim's (PQ)** → 1 subtree that grows — uses Priority Queue (min-heap) → [[L8 Heap]]
- **Kruskal's (UF)** → 1 or more subtrees that join together — uses UFDS to detect cycles → [[L9 UFDS]]

## Kruskal's Algorithm

- **To sort edges:** EdgeList<w,u,v> → [[L12 Graphs]]
- **To test for cycles:** UFDS → [[L9 UFDS]]
- **Time Complexity: O(E logV)**

```java
1. sort set of E edges by incr weight 
		// Collections.sort O(E log E)
2. T = {}
3. while there are unprocessed edges left // O(E)
		 // O(1)
		 pick an unprocessed edge e with min cost
		 // O(α(V)) = O(1) if V <= 1 mill 
		 // (grows slowly)
		 if adding e to T does not form a cycle
			 add e to T // O(1)	 
```

## Prim's Algorithm

- **Require:** PQ and boolean array taken
- **Time Complexity: O(E logV)** using adj list
    - process each edge only once = O(E)
    - enqueue / dequeue from pq = O(log E)
        - = O(log V) as E = O(V^2) [dense graph V^2 edges, sparse graph v-1 edges]

```java
1. add starting vertex s to tree
T = {S} // usually vertex 0

2. enqueue edges connected to s into PQ ordered 
based on increasing weight

3. while there are edges left in PQ
			take out the front most edge e (smallest w)
			if neighbour not yet in T
				T = T ∪ V // including this edge e
				enqueue each edge and adjacent neighbour
				into PQ if not already in T
```

### Cut Property

- for any cut of the graph, if the weight of an edge e in the cut-set is strictly smaller than the weights of other edges of the cut set, then e belongs to all MSTs of G

![[Screenshot_2024-11-21_at_1.00.16_PM.png]]

### Prim's Variant for Dense Graphs

- use **simple array A of size V**
- Time complexity = **O(V^2)**

```java

1. Initialise A[v] = <∞,v> for all v
2. A[s] = <0,s> // source vertex
3. while not all vertices are in T // O(V)
			Scan A to get v where A[v].first is min
			in A // O(V)
			Add to T
			A[v] = <∞, A[v].second> // so we won't 
															// choose again
			// find new smallest edge 
			for all neighbours u of v // O(V)
				if (u is not in T && A[u].first > w(v,u))
					A[u] = <w(v,u), v> 
```
