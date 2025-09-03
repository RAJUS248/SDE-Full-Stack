
# Binary Search Code Comparison: Bad vs Good Practices

This document demonstrates how clean, professional code improves readability and maintainability by comparing two versions of a binary search function in Python.

---

## 🔴 Poorly Written Code (Bad Practice)

```python
def f(a, t):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == t:
            return m
        elif a[m] < t:
            l = m + 1
        else:
            r = m - 1
    return -1

# Example usage
x = [1, 3, 5, 7, 9, 11]
print(f(x, 7))
```

### Problems:
- Function name `f` and variables like `a`, `t`, `l`, `r`, `m` are meaningless.
- No comments or docstrings.
- No input validation.
- Hard to debug or maintain.
- Not readable for beginners or teammates.

---

## ✅ Professionally Written Code (Clean and Understandable)

```python
def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list to find the index of the target value.

    Args:
        sorted_list (List[int]): A list of integers sorted in ascending order.
        target (int): The integer value to search for.

    Returns:
        int: The index of the target if found, else -1.
    """
    left_index = 0
    right_index = len(sorted_list) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = sorted_list[middle_index]

        if middle_value == target:
            return middle_index
        elif middle_value < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1

# Example usage
numbers = [1, 3, 5, 7, 9, 11]
search_result = binary_search(numbers, 7)
print(f"Target found at index: {search_result}" if search_result != -1 else "Target not found.")
```

### Benefits of Clean Code:
- **Readability**: Clear function and variable names show the intent.
- **Maintainability**: Easy to modify or extend in the future.
- **Debuggability**: Easier to insert logs or breakpoints.
- **Reusability**: Well-documented, modular functions are easier to reuse.
