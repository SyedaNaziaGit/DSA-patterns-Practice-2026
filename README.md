# DSA Patterns Practice 2026

Data structures and algorithms practice organised by **pattern** rather than by topic. Most interview problems are variations of a small set of patterns, so learning to recognise the pattern matters more than memorising solutions.

All solutions are in Python.

## Patterns covered

| Pattern | Folder | Use it when you see... |
|---------|--------|------------------------|
| [Two Pointers](#1-two-pointers) | `two_pointers/` | Sorted array or string, pairs, palindromes |
| [Sliding Window](#2-sliding-window) | `sliding_window_pattern/` | Longest/shortest/best contiguous subarray or substring |
| [Fast and Slow Pointers](#3-fast-and-slow-pointers-floyds-algorithm) | `fast_and_slow_floyds_algo/` | Linked list cycles, middle of a list |
| [Merge Intervals](#4-merge-intervals) | `merge_intervals_pattern/` | Overlapping ranges, scheduling |
| [Nearest Distance](#5-nearest-distance-multi-source-bfs)  | `closest_distance_pattern_or_nearest_distance/` | Shortest distance from every cell to the nearest target |
| [Sorting](#6-sorting-as-a-first-step) | `sort/` | Order makes the problem simple |
| [Greedy](#7-greedy) | `greedy/` | Locally best choice leads to a global best |
| [Backtracking](#8-backtracking) | `backtracking/` | All combinations, permutations, subsets |
| [Dynamic Programming](#9-dynamic-programming) | `dynamic_programming/` | Overlapping subproblems, optimise a count or value |
| [Trees](#10-trees-dfs-and-bfs) | `trees/` | Hierarchical data, traversals, depth |
| [Graphs](#11-graphs-bfs-and-dfs) | `graphs/` | Connections, grids, components, paths |

## Quick pattern recogniser

| If the problem says... | Think... |
|------------------------|----------|
| "sorted array", "find a pair that sums to..." | Two pointers |
| "longest substring/subarray with..." | Sliding window |
| "cycle in a linked list", "middle node" | Fast and slow pointers |
| "merge overlapping", "meeting rooms" | Merge intervals (sort first) |
| "distance to the nearest 0/1/gate" | Multi-source BFS |
| "minimum number of...", "maximum profit" with choices | Greedy or DP |
| "generate all subsets/permutations/combinations" | Backtracking |
| "number of ways to...", "can you reach..." with overlapping subproblems | Dynamic programming |
| "binary tree", "path", "depth" | Tree DFS or BFS |
| "islands", "connected components", "prerequisites" | Graph BFS, DFS, or topological sort |

---

## 1. Two Pointers

**Idea:** Use two indexes that move through the data, usually from opposite ends or in the same direction, to avoid a nested loop.

**Signals:** sorted input, pair or triplet sums, reversing, palindromes, removing duplicates in place.

**Complexity:** typically O(n) time and O(1) space, versus O(n²) for brute force.

```python
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        if s < target:
            l += 1          # need a bigger sum
        else:
            r -= 1          # need a smaller sum
    return []
```

**Classic problems:** Two Sum II, 3Sum, Valid Palindrome, Container With Most Water 

## 2. Sliding Window

**Idea:** Keep a window over a contiguous range and slide it, expanding on the right and shrinking from the left, updating the answer as you go instead of recomputing each window.

**Signals:** "longest", "shortest", or "maximum" over a contiguous subarray or substring, often with a constraint like "at most k" or "no repeats".

**Complexity:** O(n) time, since each element enters and leaves the window at most once.

```python
def longest_unique_substring(s):
    seen = {}               # char -> last index
    left = best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1     # shrink past the repeat
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

**Classic problems:** Longest Substring Without Repeating Characters, Maximum Sum Subarray of Size K, Minimum Window Substring 

## 3. Fast and Slow Pointers (Floyd's Algorithm)

**Idea:** Move one pointer one step at a time and another two steps. In a cycle, the fast pointer eventually catches the slow one. Otherwise the fast pointer reaches the end when the slow one is at the middle.

**Signals:** linked list cycles, cycle start, middle of a list, happy number.

**Complexity:** O(n) time, O(1) space, with no extra set needed.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

**Classic problems:** Linked List Cycle, Middle of the Linked List, Find the Duplicate Number 

## 4. Merge Intervals

**Idea:** Sort intervals by start time, then sweep once. If the next interval starts before the current one ends, they overlap, so merge them.

**Signals:** ranges, overlaps, meeting schedules, inserting an interval.

**Complexity:** O(n log n) because of the sort, then O(n).

```python
def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:                      # overlap
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

**Classic problems:** Merge Intervals, Insert Interval, Meeting Rooms 

## 5. Nearest Distance (Multi-Source BFS) 

**Idea:** Instead of searching from every cell, start a BFS from **all targets at once**. Each cell is reached first by its nearest target, so the BFS level is the shortest distance.

**Signals:** "distance of each cell to the nearest 0, gate, or rotten orange".

**Complexity:** O(rows × cols).

```python
from collections import deque

def nearest_zero(grid):
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                dist[r][c] = 0
                q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist
```

**Classic problems:** 01 Matrix, Rotting Oranges, Walls and Gates 


## 6. Sorting as a First Step

**Idea:** Sorting often turns a hard problem into a simple scan, because neighbours in sorted order are the ones that matter.

**Signals:** "overlap", "closest pair", "group", "rank", or when order is free to choose.

**Complexity:** O(n log n) for the sort, plus the scan.

```python
def can_attend_all(intervals):
    intervals.sort()
    return all(intervals[i][0] >= intervals[i - 1][1]
               for i in range(1, len(intervals)))
```

**Classic problems:** Meeting Rooms, Sort Colors, Kth Largest Element 

## 7. Greedy

**Idea:** At each step, take the choice that looks best right now. This only works when local choices provably lead to a global best, so check with a small counterexample first.

**Signals:** "minimum number of...", scheduling, jump or reach problems, and cases where sorting plus a rule gives the answer.

**Complexity:** usually O(n log n) (sorting) or O(n).

```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])      # earliest finish first
    count, end = 0, float("-inf")
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count
```

**Classic problems:** Jump Game, Non-overlapping Intervals, Gas Station 

## 8. Backtracking

**Idea:** Build a solution step by step. At each step choose, explore, then undo the choice (backtrack) and try the next one. It is brute force with early pruning.

**Signals:** "all subsets", "all permutations", "all combinations", N-Queens, Sudoku, word search.

**Complexity:** exponential (for example O(2ⁿ) for subsets), so pruning matters.

```python
def subsets(nums):
    res, path = [], []

    def backtrack(i):
        if i == len(nums):
            res.append(path[:])
            return
        path.append(nums[i])        # choose
        backtrack(i + 1)            # explore
        path.pop()                  # undo
        backtrack(i + 1)            # skip

    backtrack(0)
    return res
```

**Classic problems:** Subsets, Permutations, Combination Sum, N-Queens 

## 9. Dynamic Programming

**Idea:** Break the problem into overlapping subproblems, solve each once, and reuse the result (memoization or tabulation). First define the **state**, then the **transition**, then the **base case**.

**Signals:** "number of ways", "minimum cost", "maximum profit", "can you reach", and a brute-force recursion that repeats work.

**Complexity:** number of states × work per state, often O(n) or O(n²).

```python
def rob(nums):                       # House Robber
    prev, curr = 0, 0
    for n in nums:
        prev, curr = curr, max(curr, prev + n)   # skip house, or rob it
    return curr
```

**Classic problems:** Climbing Stairs, House Robber, Coin Change, Longest Common Subsequence 

## 10. Trees (DFS and BFS)

**Idea:** Trees are recursive, so most problems solve naturally with recursion (DFS: pre/in/post-order) or a queue (BFS: level order).

**Signals:** depth, paths, ancestors, level-by-level output, validating a BST.

**Complexity:** O(n) time, O(h) space for recursion, where h is the tree height.

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Classic problems:** Maximum Depth, Level Order Traversal, Validate BST, Lowest Common Ancestor 

## 11. Graphs (BFS and DFS)

**Idea:** Model items as nodes and relationships as edges. Use **BFS** for shortest paths in unweighted graphs, **DFS** for exploring components or detecting cycles, and **topological sort** for ordering with dependencies.

**Signals:** grids ("islands"), connected components, prerequisites, word ladders, "is there a path".

**Complexity:** O(V + E).

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
            return
        grid[r][c] = "0"                     # mark visited
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count
```

**Classic problems:** Number of Islands, Course Schedule, Clone Graph, Word Ladder 

---

## Repository structure

```
DSA-patterns-Practice-2026/
├── two_pointers/
├── sliding_window_pattern/
├── fast_and_slow_floyds_algo/
├── merge_intervals_pattern/
├── closest_distance_pattern_or_nearest_distance/
├── sort/
├── greedy/
├── backtracking/
├── dynamic_programming/
├── trees/
├── graphs/
└── README.md
```

Each folder holds my Python solutions for that pattern. 


## Author

**Syeda Nazia** · [GitHub](https://github.com/SyedaNaziaGit) · [LinkedIn](https://www.linkedin.com/in/syeda-nazia) · [Portfolio](https://syedanaziagit.github.io/nazia_portfolio_website/)
