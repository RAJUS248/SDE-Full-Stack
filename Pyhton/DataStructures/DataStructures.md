
# Python Data Structures - Complete Guide

Python provides several built-in and standard library data structures to store, manage, and manipulate data efficiently. This lesson covers them in detail with syntax, examples, comparisons, and use-cases.

---

## 📌 List of Data Structures in Python

| Data Structure | Type          | Mutable | Built-in | Typical Use                      |
|----------------|---------------|---------|----------|----------------------------------|
| `list`         | Sequence      | Yes     | Yes      | Ordered collection               |
| `tuple`        | Sequence      | No      | Yes      | Immutable ordered collection     |
| `set`          | Set           | Yes     | Yes      | Unordered unique items           |
| `frozenset`    | Set           | No      | Yes      | Immutable set                    |
| `dict`         | Mapping       | Yes     | Yes      | Key-value pairs                  |
| `str`          | Sequence      | No      | Yes      | Textual data                     |
| `array.array`  | Sequence      | Yes     | No       | Typed numeric values             |
| `collections.deque` | Sequence | Yes     | No       | Fast appends/pops from both ends|
| `heapq`        | Heap Queue    | Yes     | No       | Priority queue                   |
| `queue.Queue`  | Queue         | Yes     | No       | Thread-safe queue                |
| `collections.Counter` | Mapping | Yes    | No       | Frequency counting               |
| `collections.defaultdict` | Mapping | Yes| No       | Default values for missing keys |

---

## 🛠 Syntax and Creation

```python
# List
fruits = ["apple", "banana", "mango"]

# Tuple
dimensions = (1920, 1080)

# Set
unique_ids = {101, 102, 103}

# Frozenset
frozen = frozenset([1, 2, 3])

# Dictionary
student = {"name": "John", "age": 21}

# String
message = "Hello World"

# Array (typed array)
import array
arr = array.array('i', [1, 2, 3])

# Deque
from collections import deque
dq = deque([1, 2, 3])

# Heap
import heapq
heap = [3, 1, 4]
heapq.heapify(heap)

# Queue
from queue import Queue
q = Queue()
q.put(1)
q.get()

# Counter
from collections import Counter
c = Counter("banana")

# DefaultDict
from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
```

---

## 📊 Comparison Table

| Data Structure | Memory Efficient | Mutable | Heap/Stack | Advantages                               | Disadvantages                          | When to Use                             |
|----------------|------------------|---------|-------------|------------------------------------------|----------------------------------------|------------------------------------------|
| List           | Moderate         | ✅ Yes  | Heap        | Flexible, many methods                   | Slower insert/delete in middle         | Ordered data, indexing, iterating       |
| Tuple          | High             | ❌ No   | Heap        | Faster, hashable, lightweight            | Cannot modify after creation           | Constant, grouped data                  |
| Set            | High             | ✅ Yes  | Heap        | Fast lookup, remove duplicates           | Unordered, no indexing                 | Unique items only                        |
| Frozenset      | High             | ❌ No   | Heap        | Hashable, can be dictionary key          | Cannot modify                          | Immutable unique collections             |
| Dict           | High             | ✅ Yes  | Heap        | Fast key lookup, versatile               | Memory heavy, unordered < py3.7        | Mapping data, lookups                    |
| String         | Moderate         | ❌ No   | Heap        | Optimized storage, unicode support       | Costly string concatenation            | Text handling                            |
| Array          | High             | ✅ Yes  | Heap        | Fixed type, less memory than list        | Type-restricted                        | Numeric data, performance critical code  |
| Deque          | Moderate         | ✅ Yes  | Heap        | Fast appends/pops on both ends           | Slower random access                   | Queues, stacks                           |
| Heap (heapq)   | High             | ✅ Yes  | Heap        | Efficient min-heap operations            | Not thread-safe                        | Priority queues                          |
| Queue          | Moderate         | ✅ Yes  | Heap        | Thread-safe, FIFO                        | Slower than deque                      | Multithreaded producer-consumer problems |
| Counter        | High             | ✅ Yes  | Heap        | Count frequencies easily                 | Limited operations                     | Counting items in list, string, etc.     |
| DefaultDict    | Moderate         | ✅ Yes  | Heap        | Avoids key errors                        | Slight overhead                        | Grouping, default values                 |

---

## 📘 Detailed Explanation & Code Examples

### 1. `list`
```python
fruits = ['apple', 'banana', 'mango']
fruits.append('orange')
fruits.remove('banana')
print(fruits[0])  # Accessing
```

**Important Methods**: `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `sort()`, `reverse()`

---

### 2. `tuple`
```python
dimensions = (1920, 1080)
print(dimensions[0])
```

**Advantages**: Immutable, hashable, used as dictionary keys

---

### 3. `set`
```python
ids = {101, 102, 103}
ids.add(104)
ids.discard(101)
print(102 in ids)  # Fast lookup
```

**Important Methods**: `add()`, `remove()`, `union()`, `intersection()`, `difference()`

---

### 4. `frozenset`
```python
fset = frozenset([1, 2, 3])
# fset.add(4)  # ❌ Will raise error
```

---

### 5. `dict`
```python
student = {"name": "Alice", "grade": "A"}
student["age"] = 20
del student["grade"]
print(student.get("name"))
```

**Important Methods**: `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`

---

### 6. `str`
```python
s = "Python"
print(s.upper())
print(s.replace("P", "J"))
```

---

### 7. `array.array`
```python
import array
a = array.array('i', [10, 20, 30])
a.append(40)
print(a[1])
```

---

### 8. `collections.deque`
```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
```

---

### 9. `heapq`
```python
import heapq
h = [4, 1, 3]
heapq.heapify(h)
heapq.heappush(h, 2)
print(heapq.heappop(h))
```

---

### 10. `queue.Queue`
```python
from queue import Queue
q = Queue()
q.put("task1")
print(q.get())
```

---

### 11. `collections.Counter`
```python
from collections import Counter
c = Counter("banana")
print(c)  # {'a': 3, 'b': 1, 'n': 2}
```

---

### 12. `collections.defaultdict`
```python
from collections import defaultdict
d = defaultdict(int)
d['x'] += 1
print(d['x'])  # 1
```

---

## 📍 Memory Usage Insights

You can measure memory usage using `sys.getsizeof()`:

```python
import sys
print(sys.getsizeof([]))        # Empty list
print(sys.getsizeof(()))        # Empty tuple
print(sys.getsizeof(set()))     # Empty set
print(sys.getsizeof({}))        # Empty dict
print(sys.getsizeof("Python"))  # String
```

---

## 🧠 Tips to Choose the Right Data Structure

- Use **list** for ordered data and frequent indexing
- Use **tuple** when data should not change
- Use **set/frozenset** for uniqueness and fast membership checks
- Use **dict** for fast lookup by keys
- Use **deque** for queue/stack behavior
- Use **heapq** for priority queues
- Use **defaultdict** and **Counter** for data aggregation tasks

---

## 🧪 Real-Life Analogy

| Real-life Item     | Python Data Structure |
|--------------------|------------------------|
| Shopping List      | `list`                |
| Fixed GPS Coordinates | `tuple`            |
| Class Roll Numbers | `set`                 |
| Contact Book       | `dict`                |
| Word Counter       | `Counter`             |
| Inbox Queue        | `queue.Queue`         |

---

## 🧮 Heap vs Stack Allocation

- Python uses **heap memory** for all object allocations
- Local variables (references) live in **stack**
- Data structures are stored in heap and accessed via reference

---

## 📌 Summary

- Python has diverse built-in and library-supported data structures
- Choose based on **mutability**, **order**, **uniqueness**, and **performance**
- Understanding internal working helps in writing optimized code

---
