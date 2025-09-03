# 📘 Analysis of Algorithms: Time and Space Complexity

## 🧠 What is Algorithm Analysis?

Algorithm analysis is the process of evaluating the **efficiency** of an algorithm in terms of:
- **Time Complexity**: How long it takes to run.
- **Space Complexity**: How much memory it uses.

This helps developers **choose the most efficient algorithm** for solving a problem, especially when the input size becomes large.

---

## ⏱️ Time Complexity (Big O Notation)

### 🔍 What is Big O Notation?

Big O Notation describes **how an algorithm scales** with input size `n`. It represents the **worst-case time** required for execution.

| Big O | Name                | Description                                | Example                  |
|-------|---------------------|--------------------------------------------|--------------------------|
| O(1)  | Constant Time        | Executes in the same time regardless of input | Accessing an array item |
| O(log n) | Logarithmic Time | Halves input each time                     | Binary Search            |
| O(n)  | Linear Time         | Grows directly with input size              | Simple loop over array   |
| O(n log n) | Linearithmic   | Log factor added to linear                 | Merge Sort, Heap Sort    |
| O(n²) | Quadratic Time      | Nested loops                              | Bubble Sort              |
| O(2ⁿ) | Exponential Time    | Doubles each time                         | Solving subsets          |
| O(n!) | Factorial Time      | All permutations                         | Travelling Salesman (Brute Force) |

---

## 🛠️ How is Time Complexity Measured?

1. **Count the most frequent operation** (e.g., comparison, assignment).
2. Focus on the **input size `n`**.
3. Identify how the number of operations grows with `n`.

> Example: In a loop `for i in range(n):`, the loop runs `n` times → **O(n)**.

---

## 📌 Why is Time Complexity Important?

- Helps **predict performance** before running the code.
- Essential for **scaling systems**.
- Lets us **compare algorithms** efficiently.
- Saves **cost, time, and computing resources**.

---

## 🔍 Real-life Algorithm Examples

| Algorithm               | Description                         | Time Complexity |
|------------------------|-------------------------------------|-----------------|
| Binary Search          | Search in sorted list               | O(log n)        |
| Linear Search          | Check each item                     | O(n)            |
| Bubble Sort            | Compare all pairs                   | O(n²)           |
| Merge Sort             | Divide and merge                    | O(n log n)      |
| Recursive Fibonacci    | Exponential growth                  | O(2ⁿ)           |
| Traveling Salesman (Brute Force) | All possible paths       | O(n!)           |

---

## 📦 Data Structures vs Time Complexity

### 🔍 Search/Find Time Complexity

| Data Structure        | Search / Find Time     | Notes                                 |
|----------------------|------------------------|---------------------------------------|
| Array (Unsorted)     | O(n)                   | Need to check each element            |
| Array (Sorted)       | O(log n) with binary search | Must be sorted                     |
| Linked List          | O(n)                   | Traverse node-by-node                |
| Hash Table (Dict)    | O(1) average, O(n) worst | Best for quick lookup                |
| Binary Search Tree   | O(log n) avg, O(n) worst | Depends on tree balance             |
| Heap                 | O(n)                   | No direct search                     |
| Trie (Prefix Tree)   | O(k) where k = key length | Efficient for text search         |

---

## ⚠️ Exponential Complexity Growth

### Time taken grows rapidly with input size:

| Input Size (n) | O(2ⁿ) Steps     |
|----------------|-----------------|
| 5              | 32              |
| 10             | 1024            |
| 15             | 32,768          |
| 20             | 1,048,576       |
| 25             | 33,554,432      |
| 30             | 1,073,741,824   |

> 🔺 Clearly shows that exponential time is **not practical** for large inputs.

---

## 🧑‍🔬 Who Invented Algorithm Analysis?

- **Donald Knuth**, a computer scientist, played a major role in formalizing algorithm analysis in the **1960s and 1970s**.
- The term “Big O” was introduced by **Paul Bachmann** in the 1890s, but **popularized** in computer science by Knuth.

---

## 🧮 Space Complexity

### 📘 What is Space Complexity?

It is the amount of **memory** an algorithm uses relative to input size.

**Includes:**
- Input storage
- Temporary variables
- Function call stack (for recursion)

### 📌 Common Examples

| Algorithm            | Space Complexity |
|---------------------|------------------|
| Iterative Loop      | O(1)             |
| Recursive Factorial | O(n) (stack space) |
| Merge Sort          | O(n)             |
| Quick Sort (in-place) | O(log n)       |

---

## 🧠 Why is Space Complexity Important?

- Crucial in **embedded systems** or **mobile apps** where memory is limited.
- Determines **whether large datasets can fit in memory**.
- Optimizing memory improves **speed and energy usage**.

---

## ✅ Summary

| Concept          | Definition                                       |
|------------------|--------------------------------------------------|
| Time Complexity  | Execution time growth with input size            |
| Space Complexity | Memory used growth with input size               |
| Big O Notation   | Describes upper bound (worst-case performance)   |
| Efficient Algo   | Uses less time and/or space                      |
| Key Inventor     | Donald Knuth (Formalized it in 1970s)            |

---

## 🎓 Real-Life Analogy

- **Time Complexity**: How long it takes to find a book in a library.
- **Space Complexity**: How much shelf space is needed to store books.

> A good algorithm finds the book fast (low time) without needing a warehouse (low space).

---

## ✍️ Tips for Students

- Always analyze algorithms before coding.
- Use `O(1)` or `O(log n)` solutions when possible.
- Be cautious with `O(n²)` or worse in large input cases.
- Practice with real problems to understand the impact!

---
