# 📘 Python Functions - Complete Notes

## 📌 What are Functions?

Functions in Python are reusable blocks of code designed to perform a specific task. They help break down complex problems into smaller, manageable parts.

---

## 🧠 Why Use Functions? (Real-life Analogy)

Imagine a coffee machine:

* You press a button (call the function)
* It makes coffee (executes code)
* You enjoy the result (return value)

Instead of making coffee manually every time (writing the same code repeatedly), you define a process (function) once and reuse it.

---

## 🧾 Basic Function Syntax

```python
def function_name(parameters) -> return_type:
    """Optional docstring"""
    # Code block
    return value
```

### Example

```python
def greet_user(name: str) -> None:
    print(f"Hello, {name}!")

greet_user("Alice")
```

---

## 🧰 Types of Functions

### 🔹 Without Parameters and Return

```python
def say_hello() -> None:
    print("Hello there!")

say_hello()
```

### 🔹 With Parameters

```python
def greet_person(person_name: str) -> None:
    print(f"Welcome, {person_name}!")

greet_person("Mahesh")
```

### 🔹 With Return Values

```python
def square(number: int) -> int:
    return number * number

result = square(5)
print("Square is:", result)
```

### 🔹 Multiple Return Values

```python
def get_user_info() -> tuple:
    name = "John"
    age = 30
    return name, age

name, age = get_user_info()
print(name, age)
```

---

## 🧮 Return Types Examples

### Returning List

```python
def get_numbers() -> list:
    return [1, 2, 3]
```

### Returning Dictionary

```python
def get_user() -> dict:
    return {"name": "Alice", "age": 25}
```

---

## 🌀 Infinite Function Call Loop (Caution)

```python
def infinite_loop():
    print("Calling itself...")
    infinite_loop()

# infinite_loop()  # Uncomment to run - Causes RecursionError
```

### 🔥 Stack Overflow (Recursive Calls without Base Case)

```python
def explode():
    print("Stack level deep")
    explode()

# explode()  # Uncomment to simulate stack overflow
```

---

## 🧱 Call Stack Example (4 Levels Deep)

```python
def level_one():
    print("Entered Level 1")
    level_two()
    print("Exiting Level 1")

def level_two():
    print("Entered Level 2")
    level_three()
    print("Exiting Level 2")

def level_three():
    print("Entered Level 3")
    level_four()
    print("Exiting Level 3")

def level_four():
    print("Entered Level 4")
    print("Deepest level reached")
    print("Exiting Level 4")

level_one()
```

---

## 📚 Function Overloading in Python (Simulated)

Python doesn't support traditional overloading, but it can be simulated using default arguments or `*args` and `**kwargs`.

### Using Default Parameters

```python
def greet(name: str = "Guest") -> None:
    print(f"Hello, {name}!")

greet("Alice")
greet()
```

### Using \*args

```python
def add_numbers(*numbers: int) -> None:
    total = sum(numbers)
    print(f"Sum is: {total}")

add_numbers(1, 2)
add_numbers(1, 2, 3, 4)
```

---

## 📏 Naming Conventions (PEP 8)

* Function names: `snake_case`
* Variable names: `snake_case`
* Constants: `UPPER_CASE`

### Example

```python
def calculate_area(length: float, width: float) -> float:
    return length * width
```

---

## ✅ Best Practices

* 🔄 **DRY Principle**: Don’t Repeat Yourself
* 🧪 **Use meaningful names**: Describe what the function does
* 🪜 **Keep functions small**: One function = one responsibility
* 📑 **Use docstrings**: Explain parameters and return values
* ✅ **Use return instead of print for results**
* 🧪 **Write testable functions**: Avoid hardcoded values

### Docstring Example

```python
def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b
```

---

## 🖥️ Passing Parameters to Python File via Command Prompt

### Python File: `greet_user.py`

```python
import sys

def greet(name: str) -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        greet(sys.argv[1])
    else:
        print("Please provide a name as a command-line argument.")
```

### Running via Command Prompt

```bash
python greet_user.py Alice
```

#### Output

```
Hello, Alice!
```

---

## 🧩 Understanding `if __name__ == "__main__"`

### 🧐 What is it?

`__name__` is a special built-in variable in Python. It holds the name of the module. If a Python script is being run directly, `__name__` is set to `'__main__'`. If it is being imported into another script, `__name__` will be the module's name.

### ✅ Why Use It?

To prevent certain code from being run when the module is imported elsewhere.

### Example

```python
def greet(name: str) -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")
```

### Explanation

* If you run this file directly: ✅ `greet("Alice")` runs
* If you import this file in another Python script: ❌ `greet("Alice")` will not run automatically

This is especially useful for keeping **test or driver code** separate from **reusable function definitions**.

---

## 🧾 Summary

* Functions help in modular code and reuse
* Use parameters and return values effectively
* Understand the call stack and recursion
* Follow naming conventions and best practices
* Pass parameters via command line for flexible scripting
* Use `if __name__ == "__main__"` to protect script entry point

---

> ✅ Practicing small examples regularly builds confidence in writing production-level Python code!
