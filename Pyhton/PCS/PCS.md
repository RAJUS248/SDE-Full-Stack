# Professional Coding Skill (Python Edition)

## Chapter Overview

This chapter is designed to guide learners from basic functional Python code to professional, production-level Python programming. The goal is to help students write code that is clean, maintainable, testable, and suitable for use in industry environments. This includes learning about exception handling, corner case management, modularity, readability, value handling, logging, and testing.

---

## 1. Introduction to Professional Coding

In academic settings, code is often written to pass a test or fulfill an assignment. In professional environments, code must be reliable, readable, and maintainable over time. It should handle unexpected inputs gracefully, be easy for other developers to understand, and be modular enough to adapt to changing requirements.

Professional code is written with the assumption that it will be read and maintained by someone else, possibly years later. It must anticipate failures, provide meaningful error messages, and be structured to facilitate testing and debugging.

---

## 2. Writing Readable and Clean Python Code

One of the hallmarks of professional code is readability. Python's syntax is already clean and concise, but there are several best practices to make your code even clearer:

Use descriptive variable and function names that convey purpose. Avoid using single-character variable names like `x` or `n` unless inside short loops.

Keep functions small and focused. A function should do one thing and do it well.

Follow the PEP8 style guide for formatting. Use consistent indentation, spacing, and naming conventions.

Document your code with docstrings. Every function should have a short description of what it does, its parameters, and what it returns.

**Example:**

```python
# Not recommended
def f(x, y): return x + y

# Recommended
def calculate_total_price(price_per_item: float, quantity: int) -> float:
    """Calculate the total price based on item price and quantity."""
    return price_per_item * quantity
```

---

## 3. Handling Edge and Corner Cases

Real-world software often breaks not during normal usage, but due to unexpected inputs. Corner cases are those scenarios that are unlikely but possible, and your code must handle them properly.

Examples of edge cases include:

* Empty input (empty lists, strings, or files)
* Null (`None`) values
* Division by zero
* Inputs that are too large or too small

Anticipating these cases and handling them appropriately is crucial in production code.

**Example:**

```python
def divide_numbers(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return numerator / denominator
```

---

## 4. Error Handling vs. Exception Handling

In Python, errors are usually catastrophic and unrecoverable (like `MemoryError`), while exceptions are conditions that can be anticipated and handled (like `FileNotFoundError`).

You should handle exceptions, not errors. Use `try...except` blocks to catch exceptions and allow your program to fail gracefully instead of crashing unexpectedly.

---

## 5. Best Practices for Exception Handling

When handling exceptions, always be as specific as possible. Catch only the exceptions you expect and can handle meaningfully.

Avoid using a bare `except:` clause, as it will catch unexpected and unrelated issues, making debugging harder.

Use `finally` blocks or context managers (`with` statement) to manage resources like files or network connections.

**Example:**

```python
def read_file_lines(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IOError as io_error:
        print(f"Failed to read file due to I/O error: {io_error}")
        return []
```

---

## 6. Writing Maintainable and Scalable Python Code

Maintainable code is code that can be changed or extended with minimal risk. To achieve this:

* Split code into small, logical functions and classes
* Avoid duplicating logic (DRY principle)
* Use clear interfaces between components
* Favor composition over inheritance when designing class structures

**Example:**

```python
class PaymentProcessor:
    def process_payment(self, amount: float, currency: str) -> None:
        """Simulate processing a payment."""
        print(f"Processing {amount} {currency}...")

def handle_order(order_id: int, amount: float):
    payment_processor = PaymentProcessor()
    payment_processor.process_payment(amount, "USD")
    print(f"Order {order_id} processed.")
```

---

## 7. Value Passing, Immutability, and Defensive Copying

Python passes references to objects, not the objects themselves. This can lead to unexpected side effects when mutable data types (like lists or dicts) are passed to functions.

To write safe, predictable code:

* Use immutable data types where possible
* Make defensive copies of input data if you need to avoid side effects
* Be clear when a function modifies its inputs

**Example:**

```python
from copy import deepcopy

def clone_customer_data(customer_data: dict) -> dict:
    """Return a deep copy of customer data to prevent accidental modifications."""
    return deepcopy(customer_data)
```

---

## 8. Logging and Debugging in Production

In production environments, avoid using `print()` statements for debugging. Use Python's built-in `logging` module, which supports different log levels (INFO, DEBUG, ERROR) and flexible output formats.

**Example:**

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_user_profile(user_id: int):
    try:
        raise ValueError("User ID is invalid")
    except ValueError as error:
        logger.error(f"Failed to fetch user profile for ID {user_id}: {error}")
```

---

## 9. Testing and Validating Production Code

Testing is an integral part of professional development. It ensures that your code works as expected and continues to work after future changes.

Types of testing include:

* **Unit Testing**: Testing individual functions in isolation
* **Integration Testing**: Testing how multiple components work together
* **Regression Testing**: Ensuring that new changes don't break existing functionality

**Example with unittest:**

```python
import unittest

def multiply(a: int, b: int) -> int:
    return a * b

class TestMathOperations(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 100), 0)

if __name__ == "__main__":
    unittest.main()
```

---
