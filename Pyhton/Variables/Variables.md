# 🐍 Python Variables - Complete Notes

## 🎯 Why Variables Are Needed: Real-Life Analogy

Imagine your kitchen. If you want to make tea, you need to remember where the sugar, tea powder, and cups are. Instead of repeatedly going back to the grocery list, you label containers: "sugar", "tea", "cups" — now you can reuse them any time you need.

Similarly, in programming:

* A **variable** is like a labeled container.
* It stores a value (like sugar) so you can reuse it whenever needed.
* Without variables, you'd have to hard-code values every time you needed them — very inefficient and error-prone!

```python
sugar = 2  # teaspoons
water = 1  # cup
print("Making tea with", sugar, "tsp sugar and", water, "cup water")
```

---

## 📚 1. Data Types of Variables

Python has various **built-in data types**, automatically assigned when you assign a value.

### 🔢 Common Built-in Types

| Category  | Data Types                | Examples                     |
| --------- | ------------------------- | ---------------------------- |
| Numeric   | `int`, `float`, `complex` | `10`, `3.14`, `1 + 2j`       |
| Text      | `str`                     | `"hello"`                    |
| Sequence  | `list`, `tuple`, `range`  | `[1,2]`, `(3,4)`, `range(5)` |
| Mapping   | `dict`                    | `{ "name": "Alice" }`        |
| Set       | `set`, `frozenset`        | `{1,2}`, `frozenset([1,2])`  |
| Boolean   | `bool`                    | `True`, `False`              |
| Binary    | `bytes`, `bytearray`      | `b'abc'`, `bytearray(5)`     |
| None Type | `None`                    | `None`                       |

### ✅ Type Checking

```python
x = 5
print(type(x))                # <class 'int'>
print(isinstance(x, int))     # True
```

---

## 💪 2. Python is Strongly Typed

Python is **strongly typed**:

* Every variable has a **type**.
* Type mismatch causes errors.

### 🔍 Example

```python
x = "10"
y = 5
# print(x + y)  ❌ TypeError: str + int

print(int(x) + y)  # ✅ 15
```

Use `int()`, `str()`, `float()` to convert types explicitly.

---

## 🔄 3. Mutable vs Immutable Variables

### 🔁 What is Mutability?

* **Mutable**: Can be changed after creation.
* **Immutable**: Cannot be changed; any modification creates a new object.

### 📊 Mutability Table

| Data Type   | Mutable | Immutable |
| ----------- | ------- | --------- |
| `int`       | ❌       | ✅         |
| `float`     | ❌       | ✅         |
| `str`       | ❌       | ✅         |
| `list`      | ✅       | ❌         |
| `tuple`     | ❌       | ✅         |
| `dict`      | ✅       | ❌         |
| `set`       | ✅       | ❌         |
| `frozenset` | ❌       | ✅         |
| `bool`      | ❌       | ✅         |
| `bytearray` | ✅       | ❌         |
| `bytes`     | ❌       | ✅         |

### 🆔 Identity Example

```python
a = "hello"
print(id(a))
a += " world"
print(id(a))  # new id, because strings are immutable

b = [1, 2]
print(id(b))
b.append(3)
print(id(b))  # same id, because lists are mutable
```

---

## ❗ 4. Why Immutable Variables Matter

* 🧵 **Thread Safety**: Immutable objects are safer in multithreaded environments.
* 🔒 **Hashable**: Immutable types can be used as dictionary keys or in sets.
* ⚙️ **Performance**: Python can optimize memory usage for immutable objects.

### 🔑 Example: Using Immutable Keys in Dict

```python
my_dict = {(1, 2): "tuple_key"}  # ✅ tuple is immutable
# my_dict[[1, 2]] = "list_key"   ❌ TypeError: unhashable type
```

---

## 🧠 5. Scope and Lifetime of Variables

### 🔍 Variable Scope

| Scope         | Description                                                |
| ------------- | ---------------------------------------------------------- |
| **Local**     | Inside a function. Not visible outside.                    |
| **Enclosing** | In nested functions, refers to the outer function’s scope. |
| **Global**    | Declared outside all functions, accessible globally.       |
| **Built-in**  | Predefined names provided by Python itself.                |

🧠 **LEGB Rule** (Search Order):
**Local → Enclosing → Global → Built-in**

### 🔁 Example: Scope Demo

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)  # Local
    inner()
    print("Outer:", x)      # Enclosing

outer()
print("Global:", x)         # Global
```

### 🕒 Variable Lifetime

* **Local variables**: Exist only during function execution.
* **Global variables**: Exist for the entire lifetime of the program.

```python
def test():
    x = 5  # x is created
    print(x)
test()
# x no longer exists here
```

---

## 📦 6. Measuring Memory Usage of Variables

Use `sys.getsizeof()` to find out how many bytes a variable takes in memory.

```python
import sys

x = 10
print("Integer 10 takes:", sys.getsizeof(x), "bytes")

x = 10 ** 100
print("Very large integer takes:", sys.getsizeof(x), "bytes")

s = "a"
print("String 'a' takes:", sys.getsizeof(s), "bytes")

s = "a" * 100
print("String of 100 chars takes:", sys.getsizeof(s), "bytes")
```

Output will vary based on system, but you'll observe:

* Larger integers consume more memory.
* Strings grow linearly with their length.

---

## 🧠 7. Memory Segments and Variable Storage

In Python:

| Segment          | Description                                   |
| ---------------- | --------------------------------------------- |
| **Heap**         | Where objects (mutable/immutable) are stored. |
| **Stack**        | Function calls and local variable references. |
| **Code Segment** | Stores compiled Python bytecode.              |

### 👀 Internals

* Python uses **reference counting** and **garbage collection** to manage memory.
* Variables are names bound to objects in memory (via references).

### 🔍 Example

```python
x = [1, 2, 3]   # list object stored in heap, x refers to it
```

---

## ➕ 8. Math Operators with Variables

Python supports common math operations:

| Operator | Name                | Example  |
| -------- | ------------------- | -------- |
| `+`      | Addition            | `a + b`  |
| `-`      | Subtraction         | `a - b`  |
| `*`      | Multiplication      | `a * b`  |
| `/`      | Division            | `a / b`  |
| `//`     | Floor Division      | `a // b` |
| `%`      | Modulus (remainder) | `a % b`  |
| `**`     | Exponentiation      | `a ** b` |

### ⚠️ Type Mixing

```python
print(5 + 2.0)      # 7.0 (int + float = float)
print("hi" + "5")   # "hi5"
# print("hi" + 5)   ❌ TypeError
```

Use explicit type conversion to handle such cases.

```python
print("hi" + str(5))  # "hi5"
```

---

## 📌 Summary

* Python variables are **dynamically typed** but **strongly enforced**.
* Understanding **scope**, **mutability**, and **memory layout** is essential.
* Immutable types offer advantages in safety and performance.
* Use `sys.getsizeof()` to inspect memory usage.
* Variables are essential to reuse, label, and manipulate data in programs.
