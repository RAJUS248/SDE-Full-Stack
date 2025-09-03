# Loops in Python - Complete Detailed Notes

## 📌 Introduction to Loops

Loops are control flow structures used to execute a block of code repeatedly. They are essential for tasks such as iterating over collections, automating repetitive tasks, and processing large datasets.

---

## 🔁 Types of Loops in Python

Python supports two main types of loops:

### 1. `for` Loop

Used for iterating over a sequence (like a list, tuple, dictionary, string, or range).

**Syntax:**

```python
for item in sequence:
    # do something with item
```

**Example:**

```python
skills = ["coding", "problem-solving", "communication"]
for skill in skills:
    print(f"Candidate has skill: {skill}")
```

### 2. `while` Loop

Executes a block of code as long as a condition is `True`.

**Syntax:**

```python
while condition:
    # do something
```

**Example:**

```python
attempt = 0
while attempt < 3:
    print("Trying to connect to server...")
    attempt += 1
```

### 3. Simulating a `do-while` Loop

Python doesn't have a native `do-while` loop but it can be simulated:

```python
while True:
    # block of code
    if not condition:
        break
```

**Example:**

```python
while True:
    user_input = input("Enter a number (type 'exit' to stop): ")
    if user_input == 'exit':
        break
    print("You entered:", user_input)
```

---

## 🥮 The `range()` Function

Often used with `for` loops to repeat an action a specific number of times.

**Syntax:**

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

**Examples:**

```python
for number in range(1, 6):
    print(f"Number: {number}")

for i in range(10, 0, -2):
    print(i)
```

---

## 🚀 Looping Over Collections

Python lets you iterate through any iterable collection.

### List:

```python
for name in ["Alice", "Bob", "Charlie"]:
    print(name)
```

### Set:

```python
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

### Dictionary:

```python
user_scores = {"Alice": 90, "Bob": 85}
for name, score in user_scores.items():
    print(f"{name} scored {score}")
```

### Under the Hood:

Python uses **iterators** through the `__iter__()` and `__next__()` methods.

---

## 🔎 Nested `for` Loop Example (Real-Life)

### Example: Student Grades for Each Subject

```python
students = ["Alice", "Bob"]
subjects = ["Math", "Science"]

for student in students:
    for subject in subjects:
        print(f"{student} is studying {subject}")
```

#### Output:

```
Alice is studying Math
Alice is studying Science
Bob is studying Math
Bob is studying Science
```

---

## 🤡 Famous Loop Bugs in the Industry

1. **Amazon Pricing Glitch (2014)**:

   * A bug in a loop caused all book prices to drop to £0.01.
   * Lesson: Always validate loop exit conditions and boundary cases.

2. **NASA Mars Orbiter (1999)**:

   * A loop processed distance in imperial units instead of metric.
   * Lesson: Loop logic must use consistent units and data formats.

---

## ✅ Best Practices for Using Loops

* Use **meaningful variable names**.
* Avoid deeply nested loops — extract logic into functions.
* Ensure **termination conditions** are solid.
* Use `enumerate()` when index is needed.
* Use **comprehensions** for clean, readable code.

**Example with `enumerate()`:**

```python
for index, name in enumerate(["Alice", "Bob"]):
    print(f"{index + 1}. {name}")
```

**Example with `zip()`:**

```python
names = ["Alice", "Bob"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

---

## ✂ `break` and `continue` Statements

### `break` — Exit loop early

```python
for attempt in range(5):
    print("Trying to connect...")
    if attempt == 2:
        print("Connected!")
        break
```

*Real-life analogy: Stopping interview rounds after finding the perfect candidate.*

### `continue` — Skip to next iteration

```python
for candidate in ["Alice", "", "Bob"]:
    if not candidate:
        continue
    print(f"Interviewing {candidate}")
```

*Real-life analogy: Skipping empty resumes.*

---

## 📈 Loop Usage in Industry

Loops make up about **25–40%** of typical application logic in:

* Data pipelines
* Backend services
* ETL scripts
* Monitoring/logging
* Automation tasks

---

## 🧠 Summary Table

| Loop Type  | Use Case                        | When to Use                   |
| ---------- | ------------------------------- | ----------------------------- |
| `for`      | Known-length iteration          | Lists, strings, dicts, ranges |
| `while`    | Unknown-length repetition       | User input, retry logic       |
| `break`    | Exit early from loop            | Found desired result          |
| `continue` | Skip to next without processing | Invalid or skipped input      |

---

## 📝 Final Notes

* Loops are powerful but must be handled responsibly.
* Prefer readability and clarity over cleverness.
* Always test edge cases and inputs.
* Think of loops like a process — keep them clean and predictable.

---
