# Python `for` Loop - Complete Guide

## Introduction

The `for` loop in Python is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). Python's `for` loop is more like a "for-each" loop in other languages.

## Syntax Explanation

A `for` loop in Python iterates over items of any sequence (like a list, tuple, string, or dictionary) in the order they appear.

### General Syntax

```python
for variable in iterable:
    # block of code
```

* `variable`: A name representing the current element in the iteration.
* `iterable`: Any object capable of returning its elements one at a time (e.g., list, string, tuple, dictionary, set, or range).
* The loop executes the block once for each item in the iterable.

## Basic Syntax

```python
for element in iterable:
    # Execute code block
```

## 0Understanding `range()` Function

The `range()` function is commonly used with `for` loops to generate a sequence of numbers. It can take one, two, or three arguments:

### Syntax

```python
range(stop)              # 0 to stop - 1
range(start, stop)       # start to stop - 1
range(start, stop, step) # start to stop - 1 with increment/decrement of step
```

### Returns

* An immutable sequence type (range object) that can be iterated over.
* Commonly used for looping a specific number of times.

### Example

```python
for number in range(3):
    print(number)  # Outputs 0, 1, 2
```

## 1. Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")
```

## 2. Iterating Over a String

```python
word = "hello"
for character in word:
    print(character)
```

## 3. Using `range()` Function

The `range()` function returns a sequence of numbers.

### 3.1 Simple Range

```python
for number in range(5):  # 0 to 4
    print(number)
```

### 3.2 Range with Start and Stop

```python
for number in range(1, 6):  # 1 to 5
    print(number)
```

### 3.3 Range with Step

```python
for number in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(number)
```

## 4. Iterating Over a Tuple

```python
colors = ("red", "green", "blue")
for color in colors:
    print(f"Color: {color}")
```

## 5. Iterating Over a Set

```python
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)
```

## 6. Iterating Over a Dictionary

```python
student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

# Iterating over keys
for student in student_scores:
    print(f"Student: {student}, Score: {student_scores[student]}")

# Iterating over items
for student, score in student_scores.items():
    print(f"{student} scored {score}")
```

## 7. Using `enumerate()`

`enumerate()` adds a counter to an iterable.

```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index}: {name}")
```

## 8. Nested `for` Loops

```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```

## 9. `for` Loop with `else`

The `else` block is executed when the loop finishes normally (i.e., no `break`).

```python
for number in range(5):
    print(number)
else:
    print("Loop finished without break.")
```

## 10. Breaking Out of a Loop

```python
for number in range(10):
    if number == 5:
        print("Breaking loop at 5")
        break
    print(number)
```

## 11. Skipping Iterations with `continue`

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

## 12. Using List Comprehensions (One-Liner `for` Loops)

```python
squares = [number ** 2 for number in range(6)]
print(squares)
```

## Summary

* Use `for` to iterate over any iterable object.
* Use `range()` for numeric iterations.
* `enumerate()` is useful when you need indexes.
* `for-else` is a unique Python feature.
* `break` and `continue` alter loop behavior.
* List comprehensions are a concise way to create lists.
