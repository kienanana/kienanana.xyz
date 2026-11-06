---
class:
tags:
  - cs/arrays
  - cs/hashing
  - cs/greedy
  - cs/sorting
  - cs/heaps
  - cs/math
  - leetcode/medium
source: https://leetcode.com/problems/task-scheduler/
related:
author:
date: 2026-10-12
updated: 2026-10-12 16:34:32
aliases:
---
[[Leetcode]] #621

## Problem
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
 
Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
 
Constraints:
	1 <= tasks.length <= 104
	tasks[i] is an uppercase English letter.
	0 <= n <= 100

### My Max Heap Solution:
```python
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        - highest freq first 
            - track freq
                - pq: max heap 
                - (-count, task)
            - which available tasks to run first
        - track cooldowns 
            - queue (deque)
            - (execTime, -count, task)
            - tasks in cooldown
        - time = 0

        - while pq or queue:
            - check queue:
                - if execTime <= time:
                    - cooled down
                    - push to pq
            - if pq:
                - pop task from pq
                    - execute
                    - append to cooldowmn queue with freq-1 
            - time++
        """
        freq = Counter(tasks)
        pq = [(-count, task) for task, count in freq.items()]
        heapq.heapify(pq)
        queue = deque()

        time = 0
        while pq or queue:
            if queue and queue[0][0] <= time:
                _, rem, task = queue.popleft()
                heapq.heappush(pq, (rem, task))
            if pq:
                rem, task = heapq.heappop(pq)
                # rem+1 bc rem = -count
                # rem = -1: left 1 , exec and done
                if rem < -1:
                    queue.append((time+n+1, rem+1, task))
            time+=1
        return time
```

### Slight TimeSkip Max Heap Solution:
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
```

you can actually solve this with a greedy approach as well, and it's much shorter. 

### Greedy Solution:
i'll come back to this when i've done a few greedy problems.
```python

```
