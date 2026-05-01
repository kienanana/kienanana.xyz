---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/graphs
module: CS2040
lecture: L12
source:
related:
  - "[[L9 UFDS]]"
  - "[[L13 Graph Traversal]]"
  - "[[L14 MST]]"
  - "[[L15-16 SSSP]]"
  - "[[L17 APSP]]"
date:
updated:
aliases:
---

note: a TREE is an **acyclic connected graph** (see [[L10 BST]] and [[L11 AVL Tree]] for tree-based data structures)

## Terminologies

- Sparse / Dense
    - Sparse = not so many edges
    - Dense = many edges
- Complete Graph
    - Simple graph with N vertices and NC2 edges
- In/Out Degree of a vertex
    - number of in/out edges from a vertex
- (Simple) Cycle
    - path that starts and ends with the same vertex and with no repeated vertices except start/end vertex and **no repeated edges**
    - involves 3 or more unique vertices
- (Simple) Directed Cycle
    - same but the edges in the cycle are directed and in the same direction
    - involves 2 or more unique vertices
- Component
    - maximal group of vertices in an **undirected graph** that can visit each other via some path
- Connected graph
    - **undirected** graph with 1 component
    - **NOTE:** undirected simple graph **DISCONNECTED if E ≤ V-1**
- Tree
    - connected graph - one unique path between any pair of vertices
- Bipartite graph
    - undirected graph where we can partition the vertices into two sets so that there are no edges between members of the same set
    

## Graph Data Structures

|  | **Description** | **Uses** |
| --- | --- | --- |
| **Adjacency Matrix** | - if graph is undirected, matrix will be mirrored diagonally<br>- space complexity: O(V^2)<br>- better for **dense graphs / Floyd Warshall's** → [[L17 APSP]]<br>→ if sparse, a lot of space wasted | ✅ counting number of vertices (num of rows)<br>✅ if edge(u,v) exist = O(1)<br><br>- enumerating neighbours = O(V) where v is number of vertices<br>- counting number of edges = O(V^2) (count all non-zero entries) |
| **Adjacency List** | - for each vertex i, AdjList[i] stores list of i's neighbours<br>- for weighted graphs, it stores pair(neighbour, weight)<br>- sum of list.lengths for undirected = 2E<br>- space complexity = O(V+E)<br>✅ O(V+E) to traverse each vertex and its neighbours<br>worst case = O(V^2)<br>- better for **sparse graphs / Dijkstra's** → [[L15-16 SSSP]] **/ DFS BFS** → [[L13 Graph Traversal]] **/ Prim's / Kruskal's** → [[L14 MST]] | ✅ counting number of vertices (num of rows)<br>✅ enumerating neighbours O(k) / O(deg(v)) where k is num of neighbours<br><br>- if edge(u, v) exists = O(k) / O(deg(v))<br>- counting number of edges = O(V) (sum the length of all V lists) |
| **Edge List** | - For each edge i, EdgeList[i] stores (u, v, weight)<br>- space complexity O(E) / O(V+E)?<br>- used in **Kruskal's** → [[L14 MST]] and **Bellman-Ford** → [[L15-16 SSSP]] | ✅ counting num of edges = O(1) |

### Adjacency Matrix

![[IMG_D25F0019364B-1.jpeg]]

![[Screenshot_2024-11-20_at_6.45.57_PM.png]]

```java
int v = NUM_V;
int[][] AdjMatrix = new int[V][V];
```

### Adjacency List

![[Screenshot_2024-11-20_at_6.46.23_PM.png]]

- fyi: each list of neighbours in ascending order

![[IMG_0B56D0BA839B-1.jpeg]]

```java
ArrayList<ArrayList<IntegerPair>> AdjList = 
	new ArrayList<ArrayList<IntegerPair>>();
```

### Edge List

![[IMG_CC7369FA8E3B-1.jpeg]]

![[Screenshot_2024-11-20_at_6.47.12_PM.png]]

```java
ArrayList<IntegerTriple> EdgeList = 
	new ArrayList<IntegerTriple>();
```
