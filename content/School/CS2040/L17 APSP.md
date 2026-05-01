---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/graphs
module: CS2040
lecture: L17
source:
related:
  - "[[L12 Graphs]]"
  - "[[L13 Graph Traversal]]"
  - "[[L15-16 SSSP]]"
date:
updated:
aliases:
---

- **diameter** of a graph: **greatest** shortest path distance between any pair of vertices

> APSP extends [[L15-16 SSSP]] to all pairs. Floyd-Warshall uses **adjacency matrix** → [[L12 Graphs]]. For DAG special case, uses topological sort → [[L13 Graph Traversal]].

## Floyd-Warshall

### Key Idea

- Uses **2D Matrix** for SP cost: D[V][V]
- initialisation: D[i][i] = 0, D[i][j] = **weight of edge(i,j)**, if there is edge i → j, otherwise INF
- 3 nested loops
- after algo stops, D[i][j] contains the SP cost from i → j

![[Screenshot_2024-11-21_at_9.51.34_PM.png]]

```java
for (int k = 0; k < V; k++) // remember, k first
	for (int i = 0; i < V; i++) // i first
		for (int j = 0; j < V; j++) // then j
			D[i][j] = Math.min(D[i][j], D[i][k] + D[k][j])
			// relaxation of D[i][j]
```

- **preprocessing (once): O(V^3)**
    - answering query: O(1)
    - can only solve APSP for **small graphs**
        - if **E = O(V^2)** and **time is short**
    - uses **adjacency matrix** representation → [[L12 Graphs]]
    - for sparse graphs, run Dijkstra's V times instead → [[L15-16 SSSP]]

Assume that the vertices are labelled as [0 … V – 1]

- Now let **sp(i, j, k)** denotes the shortest path between vertex i and vertex j with
the restriction that the vertices on the shortest path (excluding i and j) can
only consist of **vertices from [0 … k]**
- eg. sp(1,10,3) → sp from vertex 1 → 10 using only vertices (1,2,3)
- initially **k = -1,** then iteratively **k++ until  k = V-1**

## Applications (FW Variants)

| **Print Actual SP** | - use 2D predecessor array **p**<br>- **p[i][j]** is the predecessor of j on a shortest path from i to j<br><br>**Key Idea:**<br>- initially, p[i][j] = i for all pairs of i and j (regardless of if edge(i,j) exists)<br>- in the loop: → |
| --- | --- |
| **Transitive Closure** | - determine if i is connected to j either directly or indirectly<br>- modify matrix D to only contain 0 & 1 |
| **Minimax / Maximin** | minimax: min ST<br>maximin: max ST<br>- finding the path that minimises / *maximises* the max / *min* edge from vertex i to j<br>**Key idea: (minimax)**<br>- for a single path from i to j, pick the **max edge weight** along this path<br>- then for all possible paths i → j, pick the max edge weight that is the **smallest**<br>- D[i][j] wil store the smallest max-edge-weight |
| **Detecting positive / negative Cycle** | 1. set the main diagonal of D to INF<br>2. run Floyd Warshall's<br>3. Recheck the main diagonal<br>- 0 ≤ x < inf = **positive cycle**<br>- x < 0 = **negative cycle** |

## Special Case: DAG Graph → [[L13 Graph Traversal]] (topological sort) + [[L15-16 SSSP]] (one-pass Bellman-Ford)

- When the graph is a DAG, simply call one-pass bellman ford for all the vertices according to its topological
order.
- Toposort is O(V+E), calling one-pass Bellman Ford's one time is O(E) time, so calling it for V number
of times (because we call it for all vertices in the topological order is O(VE) time.
- Thus, the overall time
complexity is O(VE + V + E), which in general is faster than Floyd Warshall's O(V3) time.

```java
// print actual SP, in the loop:
if D[i][k] + D[k][j] < D[i][j]
    D[i][j] = D[i][k] + D[k][j] // relax
    **p[i][j] = p[k][j]** // update predecessor
```

```java
// transitive closure, modified FW
// initially: D[i][j] = 0
// D[i][j] = 1 if edge(i,j) exists; 0 otherwise
// the 3 nested loops as per normal
D[i][j] = D[i][j] | (D[i][k] & D[k][j]); 
       // direct         indirect
```

```java
// minimax / maximin
// same 3 comments as above
D[i][j] = Math.min(D[i][j], 
						Math.max(D[i][k], D[k][j]));
```
