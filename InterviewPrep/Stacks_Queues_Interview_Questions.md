# 20 Interview Questions Focused on **Stacks & Queues** (Specs + Declarations Only)

> Curated for product and services companies (Microsoft, Amazon, Google, Meta, etc.).  
> **Constraint:** Solutions must rely on **stacks and/or queues** (arrays/strings are fine as input storage). Avoid other data structures like trees/graphs/heaps/tries/maps/sets—if counting is needed, use **fixed-size arrays** (e.g., 26/128/256) instead of hash maps.  
> For each problem: implement the specified function, handle invalid inputs explicitly, and **state time & space complexity**.

**Error-handling convention**  
- **Python**: raise `ValueError` for invalid inputs.  
- **Java**: throw `IllegalArgumentException` for invalid inputs.

---

## 1) Implement a Queue Using Two Stacks
**Story**: Your embedded device firmware only exposes a stack primitive, but your API needs a FIFO queue.

**Python**
```python
class QueueUsingStacks:
    def __init__(self) -> None: ...
    def enqueue(self, value: int) -> None: ...
    def dequeue(self) -> int: ...
    def peek(self) -> int: ...
    def is_empty(self) -> bool: ...
```
**Java**
```java
public static class QueueUsingStacks {
    public QueueUsingStacks() { /* ... */ }
    public void enqueue(int value) { /* ... */ }
    public int dequeue() { /* ... */ }
    public int peek() { /* ... */ }
    public boolean isEmpty() { /* ... */ }
}
```
**Valid I/O**  
- Enqueue `[1,2,3]`, then dequeue → `1`, peek → `2`  
- Enqueue `[10]`, dequeue → `10`, isEmpty → `true`
**Invalid I/O**  
- Dequeue/peek on empty queue → Error  
- Non-integer inputs if class expects `int` → Error
**Hint**: Use two stacks: `in` and `out` (amortized O(1)).

---

## 2) Implement a Stack Using Two Queues
**Story**: A legacy service exposes only queue operations; you must provide LIFO behavior to clients.

**Python**
```python
class StackUsingQueues:
    def __init__(self) -> None: ...
    def push(self, value: int) -> None: ...
    def pop(self) -> int: ...
    def top(self) -> int: ...
    def is_empty(self) -> bool: ...
```
**Java**
```java
public static class StackUsingQueues {
    public StackUsingQueues() { /* ... */ }
    public void push(int value) { /* ... */ }
    public int pop() { /* ... */ }
    public int top() { /* ... */ }
    public boolean isEmpty() { /* ... */ }
}
```
**Valid I/O**  
- Push `[1,2,3]`, pop → `3`, top → `2`  
- Push `[5]`, pop → `5`, isEmpty → `true`
**Invalid I/O**  
- Pop/top on empty stack → Error  
- Non-integer inputs if class expects `int` → Error
**Hint**: Use two queues; make push or pop O(n).

---

## 3) Min Stack (Get Minimum in O(1))
**Story**: Trading system needs constant-time min for real-time alerts.

**Python**
```python
class MinStack:
    def __init__(self) -> None: ...
    def push(self, value: int) -> None: ...
    def pop(self) -> None: ...
    def top(self) -> int: ...
    def get_min(self) -> int: ...
```
**Java**
```java
public static class MinStack {
    public MinStack() { /* ... */ }
    public void push(int value) { /* ... */ }
    public void pop() { /* ... */ }
    public int top() { /* ... */ }
    public int getMin() { /* ... */ }
}
```
**Valid I/O**  
- Push `[2,0,3,0]`; getMin→`0`; pop(); getMin→`0`; pop(); getMin→`0`  
- Push `[1]`; top→`1`; getMin→`1`
**Invalid I/O**  
- Pop/top/getMin on empty stack → Error  
- Non-integer values if only ints allowed → Error
**Hint**: Auxiliary stack for mins or store pairs.

---

## 4) Valid Parentheses
**Story**: Input validator for code editor needs to check balanced delimiters `()[]{}`.

**Python**
```python
def is_valid_parentheses(text: str) -> bool: ...
```
**Java**
```java
public static boolean isValidParentheses(String text) { ... }
```
**Valid I/O**  
- `"()[]{}"` → `True`  
- `"{[]}"` → `True`
**Invalid I/O**  
- `"(]"` → `False` (or Error if defined)  
- `text=None` → Error
**Hint**: Stack of opening brackets; map to closing.

---

## 5) Evaluate Reverse Polish Notation (RPN)
**Story**: Calculator service processes postfix expressions with +,-,*,/ (integer division truncates toward zero).

**Python**
```python
from typing import List
def eval_rpn(tokens: List[str]) -> int: ...
```
**Java**
```java
public static int evalRPN(String[] tokens) { ... }
```
**Valid I/O**  
- `["2","1","+","3","*"]` → `9`  
- `["4","13","5","/","+"]` → `6`
**Invalid I/O**  
- Malformed tokens (insufficient operands) → Error  
- Division by zero → Error
**Hint**: Stack numbers; on operator, pop two, apply, push.

---

## 6) Simplify Unix Path
**Story**: File server normalizes paths with `.` and `..` and redundant slashes.

**Python**
```python
def simplify_unix_path(path: str) -> str: ...
```
**Java**
```java
public static String simplifyUnixPath(String path) { ... }
```
**Valid I/O**  
- `"/a/./b/../../c/"` → `"/c"`  
- `"/home//foo/"` → `"/home/foo"`
**Invalid I/O**  
- `path=None` → Error  
- Relative path rules unspecified → Error (if spec demands absolute)
**Hint**: Stack components; handle `..` popping.

---

## 7) Decode Encoded String (`k[encoded]`)
**Story**: Media metadata uses patterns like `3[a2[c]]` → expand to `accaccacc`.

**Python**
```python
def decode_encoded_string(text: str) -> str: ...
```
**Java**
```java
public static String decodeEncodedString(String text) { ... }
```
**Valid I/O**  
- `"3[a]2[bc]"` → `"aaabcbc"`  
- `"3[a2[c]]"` → `"accaccacc"`
**Invalid I/O**  
- Unbalanced brackets `"3[a2[c]"` → Error  
- Non-numeric repeat counts → Error
**Hint**: Stacks for counts and partial strings.

---

## 8) Remove Adjacent Duplicates (Repeatedly)
**Story**: Log sanitizer removes consecutive duplicates until stable.

**Python**
```python
def remove_adjacent_duplicates(text: str) -> str: ...
```
**Java**
```java
public static String removeAdjacentDuplicates(String text) { ... }
```
**Valid I/O**  
- `"abbaca"` → `"ca"`  
- `"azxxzy"` → `"ay"`
**Invalid I/O**  
- `text=None` → Error  
- Non-string types → Error
**Hint**: Use a stack; pop when same as top.

---

## 9) Next Greater Element (Circular or Linear)
**Story**: Sensor array needs for each reading the next greater value to the right (wrap-around optional).

**Python**
```python
from typing import List
def next_greater_elements(nums: List[int], circular: bool=False) -> List[int]: ...
```
**Java**
```java
public static int[] nextGreaterElements(int[] nums, boolean circular) { ... }
```
**Valid I/O**  
- `[2,1,2,4,3], circular=false` → `[4,2,4,-1,-1]`  
- `[1,2,1], circular=true` → `[2,-1,2]`
**Invalid I/O**  
- `nums=None` → Error  
- Non-integers if only ints allowed → Error
**Hint**: Monotonic decreasing stack of indices.

---

## 10) Daily Temperatures
**Story**: Forecasting: for each day, in how many days will a warmer temperature occur?

**Python**
```python
from typing import List
def daily_temperatures(temps: List[int]) -> List[int]: ...
```
**Java**
```java
public static int[] dailyTemperatures(int[] temps) { ... }
```
**Valid I/O**  
- `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`  
- `[30,40,50,60]` → `[1,1,1,0]`
**Invalid I/O**  
- `temps=None` → Error  
- Values out of expected range (if constrained) → Error
**Hint**: Monotonic stack of indices.

---

## 11) Stock Span
**Story**: For each day’s price, compute span of consecutive days with price ≤ current.

**Python**
```python
from typing import List
def stock_span(prices: List[int]) -> List[int]: ...
```
**Java**
```java
public static int[] stockSpan(int[] prices) { ... }
```
**Valid I/O**  
- `[100,80,60,70,60,75,85]` → `[1,1,1,2,1,4,6]`  
- `[10,4,5,90,120,80]` → `[1,1,2,4,5,1]`
**Invalid I/O**  
- `prices=None` → Error  
- Negative prices if forbidden → Error
**Hint**: Monotonic stack of (price,index).

---

## 12) Asteroid Collision
**Story**: Asteroids in a line move left/right; same speed. Collisions annihilate smaller ones.

**Python**
```python
from typing import List
def asteroid_collision(asteroids: List[int]) -> List[int]: ...
```
**Java**
```java
public static int[] asteroidCollision(int[] asteroids) { ... }
```
**Valid I/O**  
- `[5,10,-5]` → `[5,10]`  
- `[8,-8]` → `[]`
**Invalid I/O**  
- `asteroids=None` → Error  
- Zero-valued asteroids if forbidden → Error
**Hint**: Stack — resolve collisions when top>0 and cur<0.

---

## 13) Reverse First K Elements of a Queue
**Story**: K VIP customers need priority; reverse first K entries, keep the rest order.

**Python**
```python
from typing import List
def reverse_first_k_of_queue(queue_values: List[int], k: int) -> List[int]: ...
```
**Java**
```java
public static int[] reverseFirstKOfQueue(int[] queueValues, int k) { ... }
```
**Valid I/O**  
- `queue=[1,2,3,4,5], k=3` → `[3,2,1,4,5]`  
- `queue=[1,2], k=2` → `[2,1]`
**Invalid I/O**  
- `k<0` or `k>len(queue)` → Error  
- `queue_values=None` → Error
**Hint**: Use a stack for first K, then enqueue back.

---

## 14) Design Circular Queue (Fixed Capacity)
**Story**: Implement a bounded circular queue for I/O buffering.

**Python**
```python
class CircularQueue:
    def __init__(self, capacity: int) -> None: ...
    def enq(self, value: int) -> bool: ...
    def deq(self) -> int: ...
    def front(self) -> int: ...
    def rear(self) -> int: ...
    def is_empty(self) -> bool: ...
    def is_full(self) -> bool: ...
```
**Java**
```java
public static class CircularQueue {
    public CircularQueue(int capacity) { /* ... */ }
    public boolean enq(int value) { /* ... */ }
    public int deq() { /* ... */ }
    public int front() { /* ... */ }
    public int rear() { /* ... */ }
    public boolean isEmpty() { /* ... */ }
    public boolean isFull() { /* ... */ }
}
```
**Valid I/O**  
- Capacity=3; enq 1,2,3 → isFull `true`; deq→1; enq 4 → rear `4`  
- Capacity=1; enq 7 → deq→7 → isEmpty `true`
**Invalid I/O**  
- Capacity≤0 → Error  
- deq/front/rear on empty → Error
**Hint**: Circular indices; array-backed queue.

---

## 15) Moving Average from Data Stream
**Story**: Rolling average over the last `windowSize` measurements.

**Python**
```python
class MovingAverage:
    def __init__(self, window_size: int) -> None: ...
    def next(self, value: float) -> float: ...
```
**Java**
```java
public static class MovingAverage {
    public MovingAverage(int windowSize) { /* ... */ }
    public double next(double value) { /* ... */ }
}
```
**Valid I/O**  
- window=3; next(1)=1.0; next(10)=5.5; next(3)=4.67; next(5)=6.0  
- window=1; next(4)=4.0; next(0)=0.0
**Invalid I/O**  
- window_size≤0 → Error  
- Non-numeric values → Error
**Hint**: Queue to store last `k`; running sum.

---

## 16) Hit Counter (Last 5 Minutes)
**Story**: Count hits in the past 300 seconds.

**Python**
```python
class HitCounter:
    def __init__(self) -> None: ...
    def hit(self, timestamp: int) -> None: ...
    def get_hits(self, timestamp: int) -> int: ...
```
**Java**
```java
public static class HitCounter {
    public HitCounter() { /* ... */ }
    public void hit(int timestamp) { /* ... */ }
    public int getHits(int timestamp) { ... }
}
```
**Valid I/O**  
- hit at `[1,2,3]`, getHits(4)→`3`; getHits(301)→`2` (if hits at 1 not counted)  
- hit at `[299,300,300]`, getHits(300)→`3`
**Invalid I/O**  
- Non-monotonic timestamps (if spec demands) → Error  
- Negative timestamps → Error
**Hint**: Queue of timestamps; evict older than 300s.

---

## 17) First Unique Character in a Stream
**Story**: As characters stream in, return the first non-repeating character at each step.

**Python**
```python
class FirstUniqueCharStream:
    def __init__(self) -> None: ...
    def read(self, ch: str) -> None: ...
    def first_unique(self) -> str: ...
```
**Java**
```java
public static class FirstUniqueCharStream {
    public FirstUniqueCharStream() { /* ... */ }
    public void read(char ch) { /* ... */ }
    public char firstUnique() { /* ... */ }
}
```
**Valid I/O**  
- Read `a,b,a,c` → firstUnique→`b`, then `b`, then `c`  
- Read `x,x,y` → firstUnique→`y`
**Invalid I/O**  
- Read strings of length≠1 → Error  
- Non-ASCII if spec bounds to ASCII → Error
**Hint**: Fixed-size frequency array (size 256) + queue of candidates.

---

## 18) Browser History (Back/Forward)
**Story**: Simulate back/forward navigation.

**Python**
```python
class BrowserHistory:
    def __init__(self, homepage: str) -> None: ...
    def visit(self, url: str) -> None: ...
    def back(self, steps: int) -> str: ...
    def forward(self, steps: int) -> str: ...
```
**Java**
```java
public static class BrowserHistory {
    public BrowserHistory(String homepage) { /* ... */ }
    public void visit(String url) { /* ... */ }
    public String back(int steps) { /* ... */ }
    public String forward(int steps) { /* ... */ }
}
```
**Valid I/O**  
- Visit a→b→c; back(1)→b; back(1)→a; forward(1)→b  
- After going back, `visit(d)` clears forward stack
**Invalid I/O**  
- `homepage=None` or invalid URL format (if enforced) → Error  
- Negative steps → Error
**Hint**: Two stacks: back and forward.

---

## 19) Min Queue (Queue with O(1) Min)
**Story**: Real-time analytics need a queue supporting `enqueue`, `dequeue`, `getMin` in amortized O(1).

**Python**
```python
class MinQueue:
    def __init__(self) -> None: ...
    def enqueue(self, value: int) -> None: ...
    def dequeue(self) -> int: ...
    def get_min(self) -> int: ...
    def is_empty(self) -> bool: ...
```
**Java**
```java
public static class MinQueue {
    public MinQueue() { /* ... */ }
    public void enqueue(int value) { /* ... */ }
    public int dequeue() { /* ... */ }
    public int getMin() { /* ... */ }
    public boolean isEmpty() { /* ... */ }
}
```
**Valid I/O**  
- Enq `[3,1,2]`; getMin→`1`; deq→`3`; getMin→`1`  
- Enq `[5]`; getMin→`5`
**Invalid I/O**  
- Dequeue/getMin on empty → Error  
- Non-integer inputs → Error
**Hint**: Two MinStacks or two stacks with min tracking.

---

## 20) Longest Valid Parentheses
**Story**: Code linter finds the length of the longest well-formed parentheses substring.

**Python**
```python
def longest_valid_parentheses(text: str) -> int: ...
```
**Java**
```java
public static int longestValidParentheses(String text) { ... }
```
**Valid I/O**  
- `"(()"` → `2`  
- `")()())"` → `4`
**Invalid I/O**  
- `text=None` → Error  
- Other characters present if spec restricts to `()` → Error
**Hint**: Stack of indices; or two scans with counters.

---

## Submission Requirements (for Students)
- Implement the specified function signatures **exactly**.  
- Provide **time & space complexity** and justify amortized analyses where relevant.  
- Use only **stacks and/or queues**; any counting beyond that should rely on **fixed-size arrays** (no hash maps/sets/priority queues).

