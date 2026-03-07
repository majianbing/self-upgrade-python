# Brain Muscle: Algorithmic Patterns Landscape (Enhanced)
**With Python Implementations & LeetCode Problem Matching**

---

## 💻 The Hardware Reality: Why These Patterns Work

Algorithms are strategies to optimize how we feed data from **RAM** to the **CPU**. The goal is to minimize **Latency** (waiting for data) and maximize **Throughput** (doing work).

```mermaid
flowchart LR
    subgraph CPU [CPU Core]
        ALU[ALU: Math/Logic]
        Reg[Registers: Immediate Data]
    end

    subgraph Memory [Memory Hierarchy]
        L1[L1 Cache: Super Fast]
        L2[L2 Cache: Fast]
        RAM[RAM: Slow Bottleneck]
    end

    ALU <-->|1 Cycle| Reg
    Reg <-->|~4 Cycles| L1
    L1 <-->|~10 Cycles| L2
    L2 <-->|~100+ Cycles| RAM

    %% Pattern Mappings
    RAM -.->|Sequential Access| Sliding[Sliding Window / Arrays]
    RAM -.->|Random Access| Hash[HashMap / Trees]
    
    Sliding -->|High Cache Hit Rate| L1
    Hash -->|Cache Misses| L1
```

| Algo Pattern | Hardware/OS Concept | Why it's fast |
| :--- | :--- | :--- |
| **Arrays / Sliding Window** | **Spatial Locality** | CPU Cache pre-fetches neighbors. Sequential access is king. |
| **DP (Tabulation)** | **Spatial Locality + Reuse** | Sequential writes to an array; never re-compute (saves CPU cycles). |
| **Recursion / DFS** | **Stack Memory** | Uses the Call Stack (LIFO). Can be slow due to context switching/overhead. |
| **HashMap** | **Random Access (RAM)** | Trades memory space to avoid CPU scanning cycles (O(1) vs O(N)). |
| **Bitwise** | **ALU (Arithmetic Logic Unit)** | Uses the simplest, fastest CPU circuits (AND, OR, XOR). |

---

## 🧠 The Mindset Diagram (ENHANCED)

```mermaid
flowchart TD
    Start([Read Problem]) --> Input{Input Type?}

    %% 1. Array / String
    Input -->|Array / String| Sorted{Sorted or Range?}
    Sorted -->|Yes, Sorted| BS["Binary Search"]
    Sorted -->|Range Query| Prefix["Prefix Sum"]
    Sorted -->|No| Sub{Subarray / Substring?}
    Sub -->|Yes| Window{Window Condition?}
    Window -->|Fixed/Dynamic Size| Slide["Sliding Window"]
    Sub -->|No| Next{Next Greater/Smaller?}
    Next -->|Yes| Stack["Monotonic Stack"]
    Next -->|No| Pattern{Duplicates / Pairs?}
    Pattern -->|Yes| Hash["HashMap / HashSet"]
    Pattern -->|No| Twoptr["Two Pointers"]

    %% 2. Linked List
    Input -->|Linked List| ListType{Cycle / Middle / Merge?}
    ListType -->|Cycle / Middle| FastSlow["Fast & Slow Pointers"]
    ListType -->|Reverse / Reorder| InPlace["In-Place Reversal"]
    ListType -->|Merge Sorted| Merge["Merge Two Lists"]

    %% 3. Tree / Graph / BFS/DFS
    Input -->|Tree / Graph| TreeType{Tree/Graph Type?}
    TreeType -->|BST| BSTNode["BST Validation"]
    TreeType -->|General Graph| Path{Path Finding?}
    Path -->|Shortest Path| Weighted{Weighted?}
    Weighted -->|No| BFS["BFS"]
    Weighted -->|Yes| Dijkstra["Dijkstra / A*"]
    Path -->|Dependencies| Topo["Topological Sort"]
    Path -->|Explore All| DFS["DFS / Backtracking"]

    %% 4. Optimization / Combinatorial
    Input -->|Combinatorial / Optimization| OptType{Optimization Type?}
    OptType -->|All Combos / Perms| Backtrack["Backtracking"]
    OptType -->|Top K Elements| Heap["Heap / Priority Queue"]
    OptType -->|Min/Max Value| Subproblem{Overlapping Subproblems?}
    Subproblem -->|Yes| DP["Dynamic Programming"]
    Subproblem -->|No| Greedy["Greedy Algorithm"]
    OptType -->|Intervals| Interval["Interval Scheduling"]
    OptType -->|Bit Tricks| Bits["Bitwise Operations"]
    OptType -->|Word/Prefix| Trie["Trie (Prefix Tree)"]
    OptType -->|Union/Group| UF["Union Find"]
```

---

## 🧠 The Mindset: Trigger -> Template

When reading a problem, look for keywords (**Triggers**) to identify the underlying pattern.



## 🛠️ The Global Built-in Mapping: Java vs. Python

| **Data Structure / Pattern** | **Java (Standard)**                            | **Python (Standard/Built-in)**  | **Python "Cheat Code"**            |
| ---------------------------- | ---------------------------------------------- | ------------------------------- | ---------------------------------- |
| **Dynamic Array**            | `ArrayList<T>`                                 | `list`                          | `list.append()`, `list.pop()`      |
| **Hash Map**                 | `HashMap<K, V>`                                | `dict`                          | `{}` or `collections.defaultdict`  |
| **Hash Set**                 | `HashSet<T>`                                   | `set`                           | `set()` with $O(1)$ `in` checks    |
| **Double-Ended Queue**       | `ArrayDeque<T>`                                | `collections.deque`             | `popleft()`, `appendleft()`        |
| **Min-Priority Queue**       | `PriorityQueue<T>`                             | `heapq` (functions)             | `heappush(list, val)`              |
| **Max-Priority Queue**       | `PriorityQueue<T>(Collections.reverseOrder())` | `heapq` (negate values)         | `heappush(list, -val)`             |
| **Ordered Map**              | `LinkedHashMap<K, V>`                          | `collections.OrderedDict`       | Remembers insertion order.         |
| **Sorted Map**               | `TreeMap<K, V>`                                | `bisect` or `sortedcontainers`* | `bisect.insort()`                  |
| **Frequency Counter**        | `Map<K, Integer>` + loop                       | `collections.Counter`           | `Counter(iterable).most_common(k)` |
