# Recursion Advanced Notes

## 1. Introduction: What is Recursion?
Recursion is a **programming technique** where a function calls itself to solve smaller parts of a problem until it reaches a **base condition** that stops the recursion.  

Every recursive problem has two parts:
1. **Base Case** – The stopping condition (prevents infinite loop).
2. **Recursive Case** – Function calls itself with a smaller or simpler input.

---

## 2. Walkthrough Example (with 5 steps)

Let’s start with a simple recursion example: **print numbers from 1 to 5**.

### Python
```python
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)
```

### Java
```java
public class RecursionDemo {
    static void printNumbers(int n) {
        if (n == 0) return;
        printNumbers(n - 1);
        System.out.println(n);
    }

    public static void main(String[] args) {
        printNumbers(5);
    }
}
```

### Step-by-step Execution (for `print_numbers(5)`):
1. Call stack builds:
   - `print_numbers(5)` → calls `print_numbers(4)`
   - `print_numbers(4)` → calls `print_numbers(3)`
   - `print_numbers(3)` → calls `print_numbers(2)`
   - `print_numbers(2)` → calls `print_numbers(1)`
   - `print_numbers(1)` → calls `print_numbers(0)`
2. Base case reached at `n == 0` → returns without printing.
3. Now stack unwinds:
   - `print_numbers(1)` prints 1
   - `print_numbers(2)` prints 2
   - `print_numbers(3)` prints 3
   - `print_numbers(4)` prints 4
   - `print_numbers(5)` prints 5

**Output:**  
```
1
2
3
4
5
```

---

## 3. Recursive Patterns

### Pattern 1: Work **before** the recursive call
```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

```java
static void countdown(int n) {
    if (n == 0) return;
    System.out.println(n);
    countdown(n - 1);
}
```

**Output:**  
```
5
4
3
2
1
```

---

### Pattern 2: Work **after** the recursive call
```python
def countup(n):
    if n == 0:
        return
    countup(n - 1)
    print(n)

countup(5)
```

```java
static void countup(int n) {
    if (n == 0) return;
    countup(n - 1);
    System.out.println(n);
}
```

**Output:**  
```
1
2
3
4
5
```

---

### Pattern 3: Multiple recursive calls
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

```java
static int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
```

- `fibonacci(5)` calls `fibonacci(4)` and `fibonacci(3)` → each of them calls further, forming a **tree of calls**.

---

### Pattern 4: Recursive call inside an expression
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

```java
static int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n-1);
}
```

- The result of recursion is directly used in a mathematical expression.  

---

## 4. Visualizing Recursion (Stack)

Example: factorial(4)

```
factorial(4)
= 4 * factorial(3)
= 4 * (3 * factorial(2))
= 4 * (3 * (2 * factorial(1)))
= 4 * (3 * (2 * (1 * factorial(0))))
= 4 * 3 * 2 * 1 * 1
= 24
```

---

## 5. Tips, Tricks & Pitfalls

### ✅ Tips to Master Recursion
- Always define the **base case first**.
- Think of the function as a **black box**: assume it works for smaller input.
- Dry run with **small values** to see stack.
- Use **recursion trees** for multiple calls.

### ⚠️ Common Mistakes
- **Missing base case** → infinite recursion → stack overflow.
- **Wrong base condition** gives wrong results.
- **Overlapping subproblems** → exponential calls (e.g., Fibonacci). Use memoization or DP.

---

## 6. Advanced Applications of Recursion
- **Tree Traversals** (preorder, inorder, postorder).
- **Backtracking** (N-Queens, maze solving).
- **Divide and Conquer** (merge sort, quick sort).
- **Dynamic Programming** (top-down memoization).
- **Mathematical series** (factorial, Fibonacci, power).

---

## 7. Summary
- Recursion = function calling itself until base case.  
- Patterns:
  - Work before recursion
  - Work after recursion
  - Multiple recursive calls
  - Recursive call in expression  
- Practical walkthrough shows how stack builds & unwinds.  
- Avoid mistakes by ensuring base cases and understanding stack flow.  
- Recursion is powerful for **trees, graphs, backtracking, and DP**.
