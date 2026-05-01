---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/graphs
module: CS2040
lecture: L15-16
source:
related:
  - "[[L8 Heap]]"
  - "[[L12 Graphs]]"
  - "[[L13 Graph Traversal]]"
  - "[[L17 APSP]]"
date:
updated:
aliases:
---

![[Screenshot_2024-11-21_at_1.22.36_PM.png]]

- **Shortest path weight** from Vertex a to b: **δ**(a,b)
    - infinity if b is unreachable from a, else min(PW(p))

![[Screenshot_2024-11-21_at_1.25.13_PM.png]]

## Algorithms

```java
initSSSP(s) // initialisation
	for each v in V 
		D[v] = infinity // or 1B
		p[v] = -1 // NULL
	D[s] = 0 // what we know so far
	
relax(u, v, w(u,v)) //relaxation operation
	if D[v] > D[u] + w(u,v) // SP can be shortened
		D[v] = D[u] + w(u,v) // relax this edge
		p[v] = u // rmb/update the predecessor
		// if necessary update some data structure
```

## SSSP - Terminating Condition

- algo has solved SSSP when **for all edges (u,v), D[v] ≤ D[u] + w(u,v)** [no edge can be relaxed further]

```java
initSSSP(s) 

repeat // main loop
	select edge (u,v) in E **in arbitrary manner**
	relax(u, v, w(u,v)) 
until all edges have D[v] <= D[u] + w(u,v)
// can be very slow... BF algo does relaxations 
// in a better order!
```

> **Graph representations:** choose Adj List for BFS/Bellman-Ford/Dijkstra's, Adj Matrix for dense graphs → [[L12 Graphs]]
> **For All-Pairs Shortest Paths:** → [[L17 APSP]]

| **Algorithm** | **Usefulness** | **Description** |
| --- | --- | --- |
| **Modified BFS**<br>O(V+E) | **Unweighted** graph / constant weight edges<br>→ find least number of edges traversed from s to others<br><br>will not consider a longer path with shorter weights | - graph can be directed / undirected<br>- data structure: **adj list**<br>- replace **visited** array with **distance** array **D**<br>- increase distance by 1 when moving to next vertex |
| **Bellman Ford's**<br>O(VE) | 1. general weighted graph<br>2. detect negative weight cycle | - graph can be directed / undirected<br>- data structure: **adj list / edge list**<br>- to detect -ve weight cycle, run the algo **an extra time** aft executing it for V-1 times<br>→ if any edge relaxes, -ve weight cycle exists<br>**Key idea:**<br>1. initialise<br>2. perform next step V-1 times:<br>- for every edge, if edge can be relaxed, relax and set p[v] = u |

## Bellman-Ford

- worst case complete graph: E = V^2 → O(V^3)

![[Screenshot_2024-11-21_at_3.32.49_PM.png]]

## Modified BFS

```java
// initialisation 
for all v in V
	D[v] = INF
	p[v] = -1
Q = {s} // start from s
D[s] = 0

while Q is not empty // main
	u = Q.dequeue()
	// order of neighbour
	for all v adjacent to u
		// influences BFS
		if D[v] = INF
			// visitation sequence
			D[v] = D[u] + 1
			p[v] = u
			Q.enqueue(v)
```

- **Optimise**
    - stop when no more relaxation after a pass (can flag out)
- performance on small graphs:
    - without -ve weight cycle = OK, in O(VE)
    - with -ve weight cycle = terminates in O(VE)
    - some -ve edges, no -ve cycle = OK

## Special Cases

| **Tree**<br>O(V) | **- BFS / DFS** → [[L13 Graph Traversal]]<br>- every path in tree is a shortest path, just traverse all nodes → spanning tree<br>- if neighbour is predecessor, don't visit it<br>- since O(V+E) = O(V + V-1) = O(V) |
| --- | --- |
| **Unweighted**<br>O(V+E) | **BFS only** |
| **DAG**<br>O(V+E) + O(E) | **- Toposort** → [[L13 Graph Traversal]] **, One pass Bellman Ford's**<br>   - can do an ordering of the vertices - topological sort (kahn's algo)<br>   - modify BF by replacing outermost V-1 loop to just one pass<br>   → only run the relaxation across all edges once in topological order |
| No negative weight **edge**<br>O((V+E)logV) | **Dijkstra's**<br>- can use Bellman Ford's but runs in O(VE)<br>→ for a reasonably sized weighted graph with V~1000, E~100000<br>→ E=O(V^2) in a complete simple graph, BF is really slow: O(V^3) |
| No negative weight **cycle**<br>O((V+E)logV) =<br>O(E log E) | ***Modified Dijkstra's***<br>Formal assumption: the graph has no negative weight cycle (but can have negative weight edges) |
| General case: **weighted** graph<br>O(VE) | **Bellman Ford's** |
| **Shortest path cost** of multiple sources to **same destination T** | - Flip all edges in the graphs (if it is directed) & perform SSSP algorithm from T<br>- the shortest path from vertex v to T D[v→T] is D[T→v] in our transformed graph<br><br>undirected connected weighted graph, non-negative edge weights:<br>- run dijkstra's from T to get the SPs from T to all other vertices<br>- since the graph is undirected, reversing these paths will give the SPs from other vertices to T<br>- **O((V+E)*logV) time** |

## More Algorithms

| **Algorithm** | **Usefulness** | **Description** |
| --- | --- | --- |
| **Dijkstra's**<br>O((V+E)logV) | Graphs with **no negative** **edge weight**<br>Uses min-heap (Priority Queue) → [[L8 Heap]] | *- Each vertex is only processed once*<br>**Key Ideas:**<br>- maintain a set **Solved** of vertices whose final shortest path weights have been determined, initially **Solved = {s},** source vertex s only<br>- repeatedly select vertex u in **{V - Solved}** with the **min shortest path estimate D[u]**, add **u to Solved**, **relax all edges** out of u<br>- greedy algorithm → select best so far<br>- Vertices added to Solved in non-decreasing SP costs<br><br>* can detect if graph contains -ve edge weight:<br>→ reports true when it tries to update shortest dist of a vertex in PQ but is unable to find (vertex alr in solved)<br>→ cannot be used to differentiate between -ve edge weight and cycle |
| **Modified Dijkstra's**<br>"lazy data structure" strat<br><br>O(E log E) =<br>O((V+E)logV)<br><br>except **faster** when E<O(V) **(disconnected)** then O(E log E) <<br>O(V log V) | Graphs with no **negative weight cycle** | *- Each vertex can be processed multiple times (due to presence of negative edge weight)*<br>- runs faster than Bellman Ford's<br>- can be trapped if there is -ve weight cycle<br>→ use BF instead if high probability of -ve weight cycle<br>**Key idea:**<br>- Enqueue (0,s) into a normal PQ<br>- Remove vertex u with **minimum d** from PQ<br>[min shortest path estimate so far]<br>- **if D[u] == d**, relax all edges out of u.<br>if an edge (u,v) is relaxed, update D[v] & enqueue new (d,v) into PQ<br>- **else if d > D[u],** discard this inferior (d,u) pair |

## Dijkstra's

*relax outgoing edges from nodes close to source then relax from nodes further away*

1. **Min PQ: store the shortest path estimate** for a vertex v as **IntegerPair(d,v)** in the PQ, d = D[v] (current shortest path estimate)
2. Enqueue all vertices as Pair(INF, v), except source (0,s) into PQ
3. Main loop: keep removing vertex u with **minimum d** from PQ, **add u into Solved**, **relax all outgoing** edges
    1. update D[v] and (d,v) in PQ once edge(u,v) is relaxed
    2. use bBST to implement PQ

## Modified Dijkstra's

```java
initSSSP(s)

// store pair of (dist[u], u)
PQ.enqueue((0,s))
// order: increasing dist[u]
while PQ is not empty 
	(d,u) = PQ.dequeue()
	if d == D[u] // impt check, lazy
		for each vertex v adjacent to u
			// can relax
			if D[v] > D[u] + w(u,v)
				D[v] = D[u] + w(u,v) // rlx
				PQ.enqueue(D[v], v)
				// re-enqueue this
```
