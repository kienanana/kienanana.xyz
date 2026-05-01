---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/graphs
module: CS2040
lecture: L13
source:
related:
  - "[[L6 Stacks & Queues]]"
  - "[[L9 UFDS]]"
  - "[[L12 Graphs]]"
  - "[[L14 MST]]"
  - "[[L15-16 SSSP]]"
date:
updated:
aliases:
---

## Summary

- **DFS:** by using a **stack** / **recursion** → see [[L6 Stacks & Queues]]
- **BFS:** by using a **queue** → see [[L6 Stacks & Queues]]
- both algorithms run in **O(V+E)** if graph stored in an **adj list** → see [[L12 Graphs]]
- both algorithms run in **O(V^2)** if graph is stored as an **adj matrix** → see [[L12 Graphs]]

## Breadth First Search (BFS)

- Ripple-like manner
- **Queue Q // visited[]** (0 initially, 1 when visited) **// p[v]** parent array to memorise path
- Time Complexity: O(V + E)

```java
// initialisation phase - **O(V)**
for all v in V
	visited[v] = 0
	p[v] = -1
Q = {S} // start from S
visited[s] = 1

// main loop - **O(E)**
while Q is not empty
	u = Q.dequeue()
	for all v adjacent to u // order of neighbour
		if visited[v] = 0     // influences BFS
			visited[v] = 1      // visitation sequence
			p[v] = u
			Q.enqueue(v)
```

- initialisation is O(V)
- for the while loop:
    - Case 1: disconnected graph E = 0, takes O(E)
    - Case 2: connected graph
        - each vertex is in the queue once (visited will be flagged to avoid cycle)
        - when a vertex is dequeued, all its neighbours are scanned (for loop); when queue is empty, all E edges are examined ~ O(E) → if we use Adj List!

```java
// Reachability test
BFS(u) // or DFSrec(u)
if viisted[v] == 1
	Output "yes"
else Output "no"

// identifying / counting components
CC = 0 // component count
for all v in V 
	visited[v] = 0 // initialisation
for all v in V // O(V)
	if visited[v] == 0
		CC++
		DFSrec(v) // O(V+E)
// BFS from v is also OK
```

## Kahn's Algorithm

```java
// initialisation - **O(V+E)**
for all v in V
	indef[v] = 0
	p[v] = -1
for each edge (u,v) // get indegree of vertices
	indef[v] = indeg[v] + 1
for all v' where indeg[v'] = 0
	Q = {v'} // enqueue V
	
// main loop - **O(V+E)**
while Q is not empty
	u = Q.dequeue()
	append u to back of toposort
	for all v adjacent to u // order of neighbour
		indeg[v] = indeg[v] - 1
		if indeg[v] = 0 // add to queue
			p[v] = u
			Q.enqueue(v)
output toposort as the topological order
```

## Counting SCC

```java
// taken from bots THA
// second pass DFS on the transposed graph to identify SCCs
visited = new boolean[N]; // reset visited for second           DFS pass
int sccCount = 0; 
while (!stack.isEmpty()) {
    int node = stack.pop();
    if (!visited[node]) {
        ArrayList<Integer> scc = new ArrayList<>();
        dfsRev(node, scc, sccCount);
        botnets.add(scc);
        sccCount++;
    }
}

// from lec notes 
SCC = 0
for all v in V 
	visited[v] = 0
for all v in K from last to first vertex 
	if visited[v] == 0
		SCC += 1
		DFSrec(v)
```

*Idea: If a vertex v is reachable from s, then all neighbours of v will also be reachable from s (recursive definition)*

## Depth First Search (DFS)

- maze-like manner
- **Stack S // visited[] // p[v]**
- Time Complexity: O(V + E)

```java
// initialisation phase, in the main method
for all v in V
	visited[v] = 0
	p[v] = -1
DFSrec(s) // start the recursive call from s

DFSrec(u)
	visited[u] = 1 // to avoid cycle
	for all v adjacent to u // order of neighbour
		if visited[v] = 0 // influences DFS
			p[v] = u // visitation sequence 
			DFSrec(v) // recursive (implicit stack)
```

- initialisation is O(V)
- for the while loop:
    - Case 1: disconnected graph E = 0, takes O(E)
    - Case 2: connected graph
        - each vertex is visited (ie. call DFSrec on it) once (visited will be flagged to avoid cycle)
        - when a vertex is visited, all its neighbours are scanned (for loop); when queue is empty, all E edges are examined ~ O(E) → if we use Adj List!

## Applications of BFS and DFS

| **Reachability** | check whether vertex u can reach vertex v<br>**idea: BFS / DFS** from u, if **visited[v] = 1 after end**, v is reachable |
| --- | --- |
| **Find Shortest Path** | unweighted graphs<br>**BFS, Time Complexity = O(V+E)**<br>→ for weighted SSSP see [[L15-16 SSSP]] |
| **Identifying / Counting Components** | use **BFS / DFS** to identify components by labelling / counting them<br>**Time Complexity = O(V+E)**<br>Alternative: [[L9 UFDS]] (Union-Find) |
| **Topological Sort** | **Kahn's Algorithm**<br>- modified version of **BFS**<br>- replace **visited[]** with **indeg[]** - keep track of in-degree of each vertex in the DAG<br>- use an ArrayList toposort to record the vertices<br>**- O(V+E)**<br><br>**Modified DFS (better)**<br>post order processing<br>- visit all neighbours, toposort.add(u)<br>- all vertices reachable by any vertex v will be placed before v in toposort<br>**- O(V+E)** |
| **Identifying / Counting SCC's** | **SCC:** a maximal group (subgraph) of vertices (≥ 1) in a directed graph where every vertex is reachable from every other vertex<br><br>**Kosaraju's Algorithm**<br>1. DFS topological sort (post-order) (no reversal)<br>→ store vertices into array / stack (compute finish times)<br>2. create transposed graph where direction of edges reversed<br>→ for each vertex v in adj list of G and for each neighbour u of v, add edge u → v to G'<br>3. perform counting of SCC (call DFS(G') on vertices in decreasing order of their finish times)<br>- Time complexity:<br>**Adj List O(V+E)**<br>Adj Matrix: for bigger problems, matrix size larger, more traversals |

## Modified DFS - Topological Sort

![[Screenshot_2024-11-21_at_1.59.22_AM.png]]

```java
DFSrec(u) // **O(V+E)**
	visited[u] = 1 // to avoid cycle
	for all v adjacent to u // order of neighbour
		if visited[v] = 0 // influences DFS
			p[v] = u // visitation sequence
			DFSrec(v) // recursive (implicit stack)
	append u to the back of toposort // "post-order"
	
// in the main method
for all v in V
	visited[v] = 0
	p[v] = -1
	
for all v in V
	if visited[v] == 0
		DFSrec(v) // start the recursive call 
**reverse toposort and output it**

// 1. normal DFS
// 2. once backtrack, append to toposort
// 3. reverse once done
```
