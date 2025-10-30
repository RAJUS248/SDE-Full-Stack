# Two Sum — Interviewer/Interviewee Walkthrough (Multi-Solution Master Notes)

## 1) Title Section

**Two Sum**

**Problem.** Given an integer array `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.
**Rules.**

* Exactly **one** valid pair exists.
* **Do not reuse** the same element twice.
* Return the indices in **any order**.

**Typical constraints (LeetCode-style).**

* `2 ≤ len(nums) ≤ 10^5`
* `-10^9 ≤ nums[i], target ≤ 10^9`
* One valid answer is guaranteed.

---

## 2) 👥 Roleplay: Interviewer ↔ Candidate

**Candidate:** May I confirm:

1. Are indices zero-based?
   **Interviewer:** Yes.

2. Can numbers be negative and/or repeated?
   **Interviewer:** Yes to both. There is exactly one solution.

3. If there are multiple pairs summing to target, should I return any?
   **Interviewer:** Input guarantees exactly one valid pair.

4. Do I need to preserve original order?
   **Interviewer:** No, just return valid indices.

**Candidate (thinking aloud):**

* Brute force: try all pairs `O(n^2)`.
* But we can do better: as I scan, if I know the **complement** (`target - x`), I can find it fast with a **hash map** from value → index. That gives `O(n)` on average.
* If I sort, I can two-pointer to find values in `O(n log n)` and then map back to original indices.

---

## 3) 🏷️ Important Keywords & Why They Matter

* **Hash map lookups (dictionary):** `O(1)` average to check if the complement already appeared.
* **Two pointers after sorting:** Exploits the **sorted order** to move inward and shrink the search space.
* **Binary search on sorted array:** For each element, search its complement in `O(log n)`.
* **Counting/bucketing (value → indices list):** Fast when value range is small or for duplicates handling.
* **Heap/Priority Queue:** Good for **closest pair / k-sum variants**, but not ideal for exact two-sum.
* **Streaming/Queue window:** Useful if the problem restricts to the **last k elements** (variant).
* **Stability of indices:** Sorting requires tracking **original indices**.

---

## 4) 🧠 Human (Mechanical) Approach → Brute Force

**Manual thinking:**
Look at each element and pair it with every later element; stop when a pair sums to `target`.

**Brute force logic:**

* For `i` in `[0..n-1]`

  * For `j` in `[i+1..n-1]`

    * If `nums[i] + nums[j] == target`, return `[i, j]`.

**Pseudocode**

```
for i in 0..n-1:
  for j in i+1..n-1:
    if nums[i] + nums[j] == target:
      return (i, j)
```

---

## 5) 🪓 Brute Force Implementations

**Python**

```python
from typing import List, Tuple

def two_sum_bruteforce(nums: List[int], target: int) -> Tuple[int, int]:
    n: int = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            # Check pair
            if nums[i] + nums[j] == target:
                return i, j
    # Per problem, one solution exists; fallback for completeness
    raise ValueError("No valid pair found")
```

**Time:** `O(n^2)`
**Space:** `O(1)`

**Java**

```java
public static int[] twoSumBruteForce(final int[] nums, final int target) {
    final int n = nums.length;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                return new int[] { i, j };
            }
        }
    }
    // Per problem, exactly one solution exists
    throw new IllegalArgumentException("No valid pair found");
}
```

**Time:** `O(n^2)`
**Space:** `O(1)`

---

## 6) 🧭 Mapping Brute Force → CS Concepts

* **Exhaustive search** over all pairs.
* **Signals to optimize:** repeated sum checks, no reuse of partial work, quadratic growth. We can store seen values in a hash map for instant complement tests.

---

## 7) ⚙️ Optimizations — 7 Distinct Approaches

### A) Hash Map (Two-Pass)

**Core idea:**

* Pass 1: Build `value → index`.
* Pass 2: For each `x`, check if `target - x` exists and is a different index.

**Why better:** Average `O(1)` lookups → `O(n)` total.

**When it works:** General case.
**When it doesn’t:** Pathological hash collisions (theoretical).

**Pseudocode**

```
map = {}
for i, x in enumerate(nums): map[x] = i
for i, x in enumerate(nums):
  y = target - x
  if y in map and map[y] != i: return (i, map[y])
```

**Python**

```python
from typing import List, Tuple

def two_sum_hash_two_pass(nums: List[int], target: int) -> Tuple[int, int]:
    value_to_index = {x: i for i, x in enumerate(nums)}
    for i, x in enumerate(nums):
        y = target - x
        j = value_to_index.get(y, -1)
        if j != -1 and j != i:
            return i, j
    raise ValueError("No valid pair")
```

**Java**

```java
import java.util.*;

public static int[] twoSumHashTwoPass(final int[] nums, final int target) {
    final Map<Integer, Integer> indexOf = new HashMap<>();
    for (int i = 0; i < nums.length; i++) indexOf.put(nums[i], i);
    for (int i = 0; i < nums.length; i++) {
        final int need = target - nums[i];
        final Integer j = indexOf.get(need);
        if (j != null && j != i) return new int[] { i, j };
    }
    throw new IllegalArgumentException("No valid pair");
}
```

**Complexity:** Time `O(n)` avg; Space `O(n)`
**DS rationale:** Hash map supports **constant-time** existence checks.

---

### B) Hash Map (One-Pass) — **Most Practical**

**Core idea:**
Scan once, for each `x` check if its complement already exists; otherwise store `x`.

**Why better:** Single pass, still `O(n)` average.

**When it works:** General case.

**Pseudocode**

```
map = {}
for i, x in enumerate(nums):
  y = target - x
  if y in map: return (map[y], i)
  map[x] = i
```

**Python**

```python
from typing import List, Tuple

def two_sum_hash_one_pass(nums: List[int], target: int) -> Tuple[int, int]:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    raise ValueError("No valid pair")
```

**Java**

```java
import java.util.*;

public static int[] twoSumHashOnePass(final int[] nums, final int target) {
    final Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        final int need = target - nums[i];
        final Integer j = seen.get(need);
        if (j != null) return new int[] { j, i };
        seen.put(nums[i], i);
    }
    throw new IllegalArgumentException("No valid pair");
}
```

**Complexity:** Time `O(n)` avg; Space `O(n)`
**DS rationale:** Hash map for complement lookups.

---

### C) Sorting + Two Pointers (Track Original Indices)

**Core idea:**
Sort `(value, index)` pairs by value. Use `lo`/`hi` pointers:

* If `sum < target` → `lo++`
* If `sum > target` → `hi--`
* Else return original indices.

**Why better:** `O(n log n)` due to sort; linear scan afterward.

**When it works:** Values arbitrary; need indices preserved via pairs.

**Pseudocode**

```
pairs = [(nums[i], i)]
sort pairs by value
lo, hi = 0, n-1
while lo < hi:
  s = pairs[lo].val + pairs[hi].val
  move lo/hi accordingly; if equal, return (pairs[lo].idx, pairs[hi].idx)
```

**Python**

```python
from typing import List, Tuple

def two_sum_sort_two_pointers(nums: List[int], target: int) -> Tuple[int, int]:
    pairs = sorted([(x, i) for i, x in enumerate(nums)], key=lambda t: t[0])
    lo, hi = 0, len(pairs) - 1
    while lo < hi:
        s = pairs[lo][0] + pairs[hi][0]
        if s == target:
            return pairs[lo][1], pairs[hi][1]
        if s < target:
            lo += 1
        else:
            hi -= 1
    raise ValueError("No valid pair")
```

**Java**

```java
import java.util.*;

public static int[] twoSumSortTwoPointers(final int[] nums, final int target) {
    final int n = nums.length;
    final int[][] pairs = new int[n][2]; // {value, index}
    for (int i = 0; i < n; i++) { pairs[i][0] = nums[i]; pairs[i][1] = i; }
    Arrays.sort(pairs, Comparator.comparingInt(a -> a[0]));
    int lo = 0, hi = n - 1;
    while (lo < hi) {
        final long sum = (long)pairs[lo][0] + (long)pairs[hi][0];
        if (sum == target) return new int[] { pairs[lo][1], pairs[hi][1] };
        if (sum < target) lo++; else hi--;
    }
    throw new IllegalArgumentException("No valid pair");
}
```

**Complexity:** Time `O(n log n)`; Space `O(n)`
**DS rationale:** Two pointers exploit sorted order.

---

### D) Sorting + Binary Search per Element

**Core idea:**
Sort `(value, index)` pairs. For each `i`, **binary search** for `target - value[i]` in `i+1..n-1`.

**Why better than brute force:** `O(n log n)` vs. `O(n^2)`.

**When it works:** Need to keep indices.

**Pseudocode**

```
pairs sorted by value
for i in 0..n-1:
  need = target - pairs[i].val
  j = binary_search(pairs, i+1..n-1, need)
  if found: return (pairs[i].idx, pairs[j].idx)
```

**Python**

```python
from bisect import bisect_left
from typing import List, Tuple

def two_sum_sort_binary_search(nums: List[int], target: int) -> Tuple[int, int]:
    pairs = sorted((x, i) for i, x in enumerate(nums))
    values = [v for v, _ in pairs]
    n = len(pairs)
    for i in range(n):
        need = target - pairs[i][0]
        j = bisect_left(values, need, lo=i+1)
        if j < n and values[j] == need:
            return pairs[i][1], pairs[j][1]
    raise ValueError("No valid pair")
```

**Java**

```java
import java.util.*;

public static int[] twoSumSortBinarySearch(final int[] nums, final int target) {
    final int n = nums.length;
    final int[][] pairs = new int[n][2];
    for (int i = 0; i < n; i++) { pairs[i][0] = nums[i]; pairs[i][1] = i; }
    Arrays.sort(pairs, Comparator.comparingInt(a -> a[0]));
    for (int i = 0; i < n; i++) {
        final int need = target - pairs[i][0];
        int lo = i + 1, hi = n - 1;
        while (lo <= hi) {
            final int mid = (lo + hi) >>> 1;
            if (pairs[mid][0] == need) return new int[] { pairs[i][1], pairs[mid][1] };
            if (pairs[mid][0] < need) lo = mid + 1; else hi = mid - 1;
        }
    }
    throw new IllegalArgumentException("No valid pair");
}
```

**Complexity:** Time `O(n log n)`; Space `O(n)`
**DS rationale:** Binary search on sorted array.

---

### E) Hash Map with Counts (Multiset-style)

**Core idea:**
First count frequencies `value → count`. Then scan again:

* For `x`, need `y = target - x`.
* If `y == x`, require `count[x] ≥ 2`.
* Else need `count[y] ≥ 1`.
  Return first valid pair of **distinct indices** (track an index list per value).

**Why better:** Still `O(n)` average; shows handling duplicates explicitly.

**When it works:** Helpful when duplicates are common; easy to reason about counts.

**Pseudocode**

```
count = map value->count, pos = map value->list of indices
for each x:
  y = target - x
  if y==x and count[x] >= 2: return first two indices from pos[x]
  if y!=x and count[y] >= 1: return pos[x][0], pos[y][0]
```

**Python**

```python
from typing import List, Tuple
from collections import defaultdict

def two_sum_hash_counts(nums: List[int], target: int) -> Tuple[int, int]:
    pos = defaultdict(list)
    for i, x in enumerate(nums):
        pos[x].append(i)
    for x, idxs in pos.items():
        y = target - x
        if y == x:
            if len(idxs) >= 2:
                return idxs[0], idxs[1]
        else:
            if y in pos:
                return pos[x][0], pos[y][0]
    raise ValueError("No valid pair")
```

**Java**

```java
import java.util.*;

public static int[] twoSumHashCounts(final int[] nums, final int target) {
    final Map<Integer, List<Integer>> pos = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        pos.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
    }
    for (Map.Entry<Integer, List<Integer>> e : pos.entrySet()) {
        final int x = e.getKey();
        final int y = target - x;
        if (y == x) {
            final List<Integer> idxs = e.getValue();
            if (idxs.size() >= 2) return new int[] { idxs.get(0), idxs.get(1) };
        } else if (pos.containsKey(y)) {
            return new int[] { e.getValue().get(0), pos.get(y).get(0) };
        }
    }
    throw new IllegalArgumentException("No valid pair");
}
```

**Complexity:** Time `O(n)` avg; Space `O(n)`
**DS rationale:** Hash map of **lists** to handle duplicates and return any valid pair.

---

### F) Counting Array / Bucketing (When Range is Small)

**Core idea:**
If `nums[i]` lies in a **small known range** `[L..R]`, create an array bucket `B[value-L] → first index`. Scan and check complement in O(1).

**Why better:** `O(n + range)` and low constant factors when range is tiny.

**When it works:** Only when **range is small** and known (e.g., interview variant).

**Pseudocode**

```
offset = -L
B = array of size (R-L+1) init -1
for i, x in enumerate(nums):
  need = target - x
  if L <= need <= R and B[need+offset] != -1: return (B[need+offset], i)
  if B[x+offset] == -1: B[x+offset] = i
```

**Python**

```python
from typing import List, Tuple

def two_sum_bucket(nums: List[int], target: int, L: int, R: int) -> Tuple[int, int]:
    size = R - L + 1
    buckets = [-1] * size
    for i, x in enumerate(nums):
        need = target - x
        if L <= need <= R and buckets[need - L] != -1:
            return buckets[need - L], i
        if buckets[x - L] == -1:
            buckets[x - L] = i
    raise ValueError("No valid pair")
```

**Java**

```java
public static int[] twoSumBucket(final int[] nums, final int target, final int L, final int R) {
    final int size = R - L + 1;
    final int[] bucket = new int[size];
    java.util.Arrays.fill(bucket, -1);
    for (int i = 0; i < nums.length; i++) {
        final int x = nums[i], need = target - x;
        if (need >= L && need <= R && bucket[need - L] != -1) {
            return new int[] { bucket[need - L], i };
        }
        if (bucket[x - L] == -1) bucket[x - L] = i;
    }
    throw new IllegalArgumentException("No valid pair");
}
```

**Complexity:** Time `O(n + range)`; Space `O(range)`
**DS rationale:** **Direct addressing** replaces hashing when domains are tiny.

---

### G) Streaming Window with Queue (+ Hash) — Variant

**Core idea:**
If the stream is large and you can only keep the **last `k`** elements, maintain:

* A queue of last `k` indices/values.
* A hash map `value → latest index` of the window.
  On each new element, evict old if size > `k`, then check complement.

**Why better:** Supports **online/streaming** constraints.

**When it works:** Only in streaming/windowed variants (not required here).

**Pseudocode**

```
queue, map
for each incoming (i, x):
  evict if queue size == k
  if (target-x) in map: return (map[target-x], i)
  push x, update map
```

**Python**

```python
from collections import deque
from typing import Deque, Dict, Tuple, Optional, Iterable

def two_sum_stream_window(stream: Iterable[int], target: int, k: int) -> Optional[Tuple[int, int]]:
    q: Deque[Tuple[int, int]] = deque()  # (value, index)
    idx_map: Dict[int, int] = {}
    for i, x in enumerate(stream):
        need = target - x
        if need in idx_map:
            return idx_map[need], i
        q.append((x, i))
        idx_map[x] = i
        if len(q) > k:
            old_val, old_idx = q.popleft()
            # If this index is still the latest occurrence, remove it
            if idx_map.get(old_val) == old_idx:
                idx_map.pop(old_val)
    return None
```

**Java**

```java
import java.util.*;

public static int[] twoSumStreamWindow(final int[] stream, final int target, final int k) {
    final Deque<int[]> q = new ArrayDeque<>(); // {value, index}
    final Map<Integer, Integer> idxMap = new HashMap<>();
    for (int i = 0; i < stream.length; i++) {
        final int x = stream[i], need = target - x;
        final Integer j = idxMap.get(need);
        if (j != null) return new int[] { j, i };
        q.addLast(new int[] { x, i });
        idxMap.put(x, i);
        if (q.size() > k) {
            final int[] old = q.removeFirst();
            if (Objects.equals(idxMap.get(old[0]), old[1])) idxMap.remove(old[0]);
        }
    }
    return null; // not found in windowed stream
}
```

**Complexity:** Amortized `O(n)`; Space `O(k)`
**DS rationale:** **Queue** for eviction order + hash for lookups.

---

### H) Priority Queue (Min-Heap) — Educational (Not Ideal Here)

**Core idea:**
Maintain a min-heap of values; for each `x`, search whether `target - x` is present (needs extra hash). This becomes a convoluted combo `heap + hash`.

**Why it’s worse:** Heap doesn’t speed up **equality** search; you still need a hash set/map. Complexity ends up `O(n log n)` with more overhead.

**When to use heap:** For **closest sum** or **top-k** style variants, not exact two-sum.

**Pseudocode (illustrative)**

```
heap = []
set = {}
for x in nums:
  if (target-x) in set: return ...
  push x to heap, add to set
```

**Python**

```python
import heapq
from typing import List, Tuple

def two_sum_heap_demo(nums: List[int], target: int) -> Tuple[int, int]:
    # Not recommended for exact match; uses extra hash map anyway.
    heap = []
    pos = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in pos:
            return pos[need], i
        heapq.heappush(heap, (x, i))  # heap adds no real benefit for equality search
        pos[x] = i
    raise ValueError("No valid pair")
```

**Java**

```java
import java.util.*;

public static int[] twoSumHeapDemo(final int[] nums, final int target) {
    final PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
    final Map<Integer, Integer> pos = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        final int need = target - nums[i];
        final Integer j = pos.get(need);
        if (j != null) return new int[] { j, i };
        pq.add(new int[] { nums[i], i }); // heap not helping equality search
        pos.put(nums[i], i);
    }
    throw new IllegalArgumentException("No valid pair");
}
```

**Complexity:** Time `O(n log n)`; Space `O(n)`
**DS rationale:** Heaps are for order/statistics, **not** direct equality lookup.

---

## 8) 🚫 Common Wrong/Naïve Algorithms

1. **Sort and return the indices `lo` & `hi` directly (without tracking original indices).**
   **Why plausible:** Two-pointer after sort is correct on values.
   **Counterexample:** `nums = [3, 3], target = 6`. Sorting yields `[3, 3]`, but returning `0,1` from the **sorted** array are not necessarily the original positions unless tracked.
   **Failure:** Loses original indices—**must** carry `(value, index)` pairs.

2. **Using a Set only (values, no indices).**
   **Why plausible:** You can detect existence of `need = target - x`.
   **Counterexample:** `nums = [2, 7, 11, 15], target = 9`. Set detects `7`, but you cannot recover its **index** without extra structure.
   **Failure:** Problem requires **indices**; set alone is insufficient.

---

## 9) 🧪 Edge Case Checklist

* **Two identical numbers needed:** e.g., `[3,3], target=6` → ensure distinct indices.
* **Negatives & zeros:** e.g., `[-1, 0, 1], target=0`.
* **Large values / overflow concern (Java):** sum cast to `long` when comparing after sorting.
* **Duplicates elsewhere:** multiple occurrences; ensure returning any valid pair is fine.
* **Minimal length:** `n = 2`.
* **Already sorted / reverse-sorted:** sorting approaches still OK.
* **All equal values:** `nums=[5,5,5]`, `target=10` → pick two different indices.

---

## 10) ⏱️ Complexity Summary

| Name                       | Idea                               |         Time |    Space | Notes / When to Use               |
| -------------------------- | ---------------------------------- | -----------: | -------: | --------------------------------- |
| Brute Force                | Try all pairs                      |        O(n²) |     O(1) | Easiest to reason, slow for big n |
| Hash Map (Two-Pass)        | Map value→index, then scan         |     O(n) avg |     O(n) | Simple, clear separation          |
| **Hash Map (One-Pass)**    | Check complement while scanning    | **O(n) avg** | **O(n)** | **Best practical**                |
| Sort + Two Pointers        | Sort pairs; meet in the middle     |   O(n log n) |     O(n) | Good without hashing              |
| Sort + Binary Search       | For each, binary search complement |   O(n log n) |     O(n) | Deterministic, clean              |
| Hash Map with Counts       | Value→indices list                 |     O(n) avg |     O(n) | Clear duplicate handling          |
| Bucket / Direct Addressing | Array index by value offset        | O(n + range) | O(range) | Only when range is tiny           |
| Heap Demo (Educational)    | Heap + hash (no benefit)           |   O(n log n) |     O(n) | Use heap for other variants       |

---

## 11) 🧰 Why Optimization Works (Conceptual)

* **Hashing:** Converts repeated “search for complement” from `O(n)` to **`O(1)` average**.
* **Two Pointers (sorted):** Maintains an **invariant** that moving `lo`/`hi` adjusts sum monotonically.
* **Binary Search:** Post-sort, equality search is **logarithmic**.
* **Counts/Multiset:** Makes duplicate handling explicit and simple.
* **Bucket/Direct Addressing:** Trades memory for **constant-time** lookups when domain is small.

---

## 12) 🧑‍💻 Final "Ready-to-Use" Functions (Recommended: One-Pass Hash Map)

**Python (type hints)**

```python
from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Return indices (i, j) such that nums[i] + nums[j] == target.
    Assumes exactly one solution exists and an element cannot be reused.
    """
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    # Per problem statement there is exactly one solution
    raise ValueError("No valid pair found")
```

**Java (function-only)**

```java
import java.util.*;

public static int[] twoSum(final int[] nums, final int target) {
    // Map from value -> index of its last occurrence seen so far
    final Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        final int need = target - nums[i];
        final Integer j = seen.get(need);
        if (j != null) {
            return new int[] { j, i }; // found complement earlier
        }
        seen.put(nums[i], i);
    }
    // Problem guarantees exactly one solution
    throw new IllegalArgumentException("No valid pair found");
}
```

---

## 13) 📌 Quick Practice Plan

**How to practice**

1. Implement **Brute Force** and **One-Pass Hash**.
2. Generate **random arrays**; verify both functions return identical indices (order can differ).
3. Test **edge cases**: duplicates, negatives, zeros, `[3,3]`, minimal `n=2`.
4. Add the **sorted two-pointer** version and compare outputs.
5. Time your implementations on increasing `n` to **feel** the complexity differences.

**Sample tests**

```
nums = [2,7,11,15], target=9        -> (0,1)
nums = [3,2,4], target=6            -> (1,2)
nums = [3,3], target=6              -> (0,1)
nums = [-1, -2, -3, -4, -5], target=-8 -> (2,4) or (1,3) depending on data
nums = [0,4,3,0], target=0          -> (0,3)
```

---

