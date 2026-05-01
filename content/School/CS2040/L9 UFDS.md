---
class: note
tags:
  - y2s1
  - cs/dsa
  - cs/data-structures
module: CS2040
lecture: L9
source:
related:
  - "[[L12 Graphs]]"
  - "[[L13 Graph Traversal]]"
  - "[[L14 MST]]"
date:
updated:
aliases:
---

```jsx
class UnionFind {
	public int[] p;
	public int[] rank;
	
	public UnionFind(int N) {
		p = new int[N];
		rank = new int[N];
		for (int i = 0; i < N; i++) {
			p[i] = i;
			rank[i] = 0;
		}
	}

	// find the representative item of the set that contains item i
	// by recursively visiting p[i] until p[i] = i
	// compress the path to make future find operations O(1)
	public int findSet(int i) {
		if (p[i] == i) {
			return i;
		} else {
			p[i] = findSet(p[i]);
			return p[i];
		}
	}
	
	public Boolean isSameSet(int i, int j) {
		return findSet(i) == findSet(j);
	}
	
	// if i and j belong to different disjoint sets
	// union them by setting representative item of the taller tree
	// to be the new rep of the combined set -> make result shorter
	public void unionSet(int i, int j) {
		if (!isSameSet(i, j)) {
			int x = findSet(i), y = findSet(j);
			// rank is used to keep the tree short
			if (rank[x] > rank[y]) {
				p[y] = x;
			} else {
				p[x] = y;
				if (rank[x] == rank[y]) { // rank increases
					rank[y] += 1;           // only if both trees
				}                         // initially have same rank
			}
		}
	}
	
}
```

- collection of disjoint sets
- Operations:
    - unionSet(i,j): Union two disjoint sets when needed
    - findSet(i): Find which set an item belongs to
    - isSameSet(i,j): Check if two items belong to the same set
- **Each set** is modelled as a **tree** - collection of disjoint sets forms a forest of trees
- Each set represented by a **representative item:** **root** of the corresponding tree of that set

![[Screenshot_2024-11-20_at_12.18.29_PM.png]]

## unionSet

- Union-by-Rank
- use another integer array rank, where rank[i] stores the **upper bound of the height of (sub)tree rooted at i**
    - this is just an upper bound as path compressions can make (sub)trees shorter than its upper bound

## Summary

![[Screenshot_2024-11-20_at_1.04.15_PM.png]]

## Used In
- **Kruskal's Algorithm** → [[L14 MST]] (detect whether adding an edge forms a cycle, by checking if two endpoints are in the same set)
- **Component counting** in undirected graphs → [[L13 Graph Traversal]] (alternative to BFS/DFS-based component detection)
