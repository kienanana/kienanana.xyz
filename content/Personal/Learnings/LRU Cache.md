---
class:
tags:
  - cs/hashing
  - cs/linked-lists
  - cs/design
  - cs/doubly-linked-list
  - leetcode/medium
source: https://leetcode.com/problems/lru-cache/
related:
author:
date: 2026-09-24
updated: 2026-09-24 15:16:01
aliases:
---
[[Leetcode]] #146

i actually encountered this problem in an Online Assessment, super tricky. even this second time around i took really long because of all the manual insertions and deletions i was doing, which made the code really messy. defining extra functions for insert and remove is definitely the right play here.

## Problem
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	int get(int key) Return the value of the key if the key exists, otherwise return -1.
	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
Constraints:
	1 <= capacity <= 3000
	0 <= key <= 104
	0 <= value <= 105
	At most 2 * 105 calls will be made to get and put.

### My Solution (Messy) (Double Linked List):
```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}

        # dummy nodes
        ## left: LRU, right: MRU
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            prev1 = node.prev
            next1 = node.next
            prev1.next = next1
            next1.prev = prev1

            prev2 = self.right.prev
            prev2.next = node
            node.prev = prev2
            node.next = self.right
            self.right.prev = node

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
            # remove node form original position
            oldPrev = node.prev
            oldNext = node.next
            oldPrev.next = oldNext
            oldNext.prev = oldPrev
        else:
            node = Node(key, value)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                lru = self.left.next
                newNext = lru.next
                newNext.prev = self.left
                self.left.next = newNext
                self.cache.pop(lru.key)

        # put node at MRU 
        newPrev = self.right.prev
        newPrev.next = node
        node.prev = newPrev
        node.next = self.right
        self.right.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

a lot of repeated lines in my solution, defining extra functions resolves this.

### Cleaner Solution:
```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```