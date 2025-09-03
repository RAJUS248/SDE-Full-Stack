# 📘 Object-Oriented Programming (OOP) in Python – Food Delivery Context

## 🔍 Why OOP Came into the Industry

Before OOP, software development was mostly **procedural**, which caused:

* Difficulty modeling real-world entities (e.g., restaurants, customers).
* Repeated code and hard-to-maintain logic.
* Tight coupling between different parts of the program.

### ✅ What OOP Solves

| Problem in Procedural Programming | OOP Solution in Food Delivery                     |
| --------------------------------- | ------------------------------------------------- |
| Repetitive Code                   | Reusable classes for customers, restaurants, etc. |
| Complex Logic                     | Clean separation using encapsulation              |
| Poor Scalability                  | Modularity via objects                            |
| No Real-world Mapping             | Entities modeled as classes                       |

## 🕰️ When Was OOP Introduced?

* **1967** – Introduced in **Simula**.
* **1980s** – Gained popularity via **C++**, **Smalltalk**.
* **2000s** – Fully supported in **Python**.

---

## 📦 Core Concepts in OOP

### 🏷️ Class and Object

* **Class**: A template (e.g., `Customer`, `Restaurant`).
* **Object**: A specific entity (e.g., a particular customer or order).

### 🔾 Example

```python
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def place_order(self, item):
        return f"{self.name} placed an order for {item}"

# Creating an object
cust1 = Customer("Ravi", "MG Road, Bengaluru")
print(cust1.place_order("Paneer Biryani"))
```

---

## ❌ Preventing Arbitrary Attribute Assignment

By default, Python lets you assign any new attribute to an object dynamically because all object attributes are stored in an internal dictionary called `__dict__`.

### ✨ Under the Hood: `__dict__`

Each object in Python has a built-in `__dict__` attribute that stores instance variables:

```python
class Agent:
    def __init__(self, name):
        self.name = name

agent = Agent("Raju")
print(agent.__dict__)  # {'name': 'Raju'}

agent.rating = 4.9     # Dynamically added
print(agent.__dict__)  # {'name': 'Raju', 'rating': 4.9}
```

This makes Python flexible but also allows accidental or unintentional attribute assignment.

### 📆 Introducing `__slots__`

To restrict attribute creation and save memory, Python provides `__slots__`. When you define `__slots__`, Python doesn't create a `__dict__` for each instance. Instead, it uses a static structure (like a tuple or array) internally, which:

* Prevents the addition of new attributes.
* Saves memory for large number of objects.

### 🔾 Example

```python
class DeliveryAgent:
    __slots__ = ['name', 'location']  # Only these can be set

    def __init__(self, name, location):
        self.name = name
        self.location = location

agent = DeliveryAgent("Raj", "Koramangala")
print(agent.name)

agent.rating = 4.9  # ❌ Raises AttributeError
```

### 🧰 Summary: `__dict__` vs `__slots__`

| Feature     | `__dict__`                           | `__slots__`                      |
| ----------- | ------------------------------------ | -------------------------------- |
| Memory      | More (stores a full dictionary)      | Less (uses static memory layout) |
| Flexibility | High (add/remove attributes anytime) | Limited (attributes are fixed)   |
| Speed       | Slightly slower due to dict lookup   | Faster attribute access          |

---

## 🔐 Access Modifiers in Python

Python uses conventions for access control:

| Modifier  | Syntax     | Meaning                            |
| --------- | ---------- | ---------------------------------- |
| Public    | `self.var` | Accessible from outside            |
| Protected | `_var`     | Intended for internal/subclass use |
| Private   | `__var`    | Hidden via name mangling           |

### 🔾 Example

```python
class DeliveryAgent:
    def __init__(self):
        self.name = "Raj"            # Public
        self._location = "Koramangala"  # Protected
        self.__rating = 4.8          # Private

agent = DeliveryAgent()
print(agent.name)             # ✅ OK
print(agent._location)        # ⚠️ Accessed directly (not recommended)
# print(agent.__rating)       # ❌ Will raise AttributeError
print(agent._DeliveryAgent__rating)  # ✅ Name-mangled access
```

---

## 📀 OOP Best Practices

* Use `__init__` to initialize object state.
* Keep sensitive data protected/private.
* Use **properties** for attribute access.
* Maintain **SRP** (Single Responsibility Principle).
* Classes should reflect **real-world roles**.
* Prefer **composition** over deep inheritance.

---

## 📞 Accessing Methods and Values

```python
class Restaurant:
    def __init__(self, name):
        self.name = name

    def prepare_food(self):
        print(f"{self.name} is preparing your food.")

rest = Restaurant("SpiceHub")
rest.prepare_food()          # Method call
print(rest.name)             # Attribute access
```

---

## 🧬 Inheritance

Inheritance helps reuse logic between related classes.

### 🔾 Example

```python
class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        return f"{self.name} logged in"

class Customer(User):
    def place_order(self, item):
        return f"{self.name} ordered {item}"

c1 = Customer("Sneha")
print(c1.login())              # Inherited
print(c1.place_order("Pizza")) # Defined in subclass
```

---

## 📦 Built-in Types as Classes

Even basic types like `int`, `str`, `float` are **classes** in Python.

```python
order_id = 1234
print(type(order_id))   # <class 'int'>

delivery_note = "Delivered on time"
print(type(delivery_note))  # <class 'str'>
```

You're **creating objects** of class `int` or `str` when you assign values.

---

## 🧐 Memory Management in OOP (Python)

### When is memory allocated?

* Memory is allocated on the **heap** when an object is created (`Customer("Ravi")`).

### When is it freed?

* Python uses **automatic garbage collection** (reference counting).
* Memory is freed when no references exist.

### Memory Segments

| Segment      | Contents                          |
| ------------ | --------------------------------- |
| Stack        | References, function calls        |
| Heap         | Customer/Agent/Restaurant objects |
| Code Segment | Class definitions, methods        |

---

## 💻 How OS Handles OOP Differently than C Code

| Feature           | OOP in Python                           | Procedural C Code                      |
| ----------------- | --------------------------------------- | -------------------------------------- |
| Memory Management | Automatic via garbage collector         | Manual (`malloc`/`free`)               |
| Code Execution    | Interpreted via CPython                 | Compiled to native machine code        |
| Method Dispatch   | Handled at runtime                      | Static call, faster execution          |
| Security & Safety | Encapsulation, no direct pointer access | Vulnerable to memory leaks, corruption |

Python’s virtual machine wraps the execution with **metadata and safety layers**, unlike direct system-level access in C.

---

## 🔒 Security via OOP & OS

* **Encapsulation** hides sensitive info like payment data.
* **Inheritance and abstraction** limit access.
* OS ensures:

  * **Memory protection** (heap isolation).
  * **Sandboxed execution** (e.g., containers, VMs).
  * **Garbage collection** avoids pointer misuse bugs.

Example:

```python
class PaymentProcessor:
    def __init__(self, __secret_key):
        self.__secret_key = __secret_key  # Kept private

    def process(self, amount):
        return f"Processed ₹299 securely"

p = PaymentProcessor("xyz123")
print(p.process(299))
```

---

## 🧠 Summary

| Concept           | Explanation in Food Delivery                  |
| ----------------- | --------------------------------------------- |
| OOP Purpose       | Real-world modeling: `Customer`, `Restaurant` |
| Class             | Template for objects                          |
| Object            | Instance of class                             |
| Access Modifiers  | Control visibility of data                    |
| Inheritance       | `Customer` inherits from `User`               |
| Memory Allocation | Heap allocation at runtime                    |
| OS Behavior       | Managed execution, sandboxing, GC             |
| Built-in Classes  | All types (`int`, `str`) are classes too      |

---

## ✅ Further Practice (Food Delivery)

Implement:

* `Order` class with item, quantity, status.
* `DeliveryBusiness` class to manage orders, agents, customers.
* `Review` class with `Customer` and `Restaurant` relationship.
* Simulate delivery status update using method overriding.
