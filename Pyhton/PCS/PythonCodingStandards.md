# Python Code Naming Conventions (PEP 8 Standard)

Python has a widely accepted style guide known as **PEP 8**. These naming conventions help make Python code more readable, maintainable, and consistent. This guide is tailored for college students aiming to write professional-level Python code.

---

## 1. Class Names

* Use **PascalCase** (a.k.a. CapitalizedWords)
* Should be **nouns**, representing data types or entities

**Example:**

```python
class StudentRecord:
    pass
```

---

## 2. Function Names

* Use **snake\_case** (lowercase with underscores)
* Should be **verbs or verb phrases**

**Example:**

```python
def calculate_salary():
    pass
```

---

## 3. Variable Names

* Use **snake\_case**
* Should be **nouns** representing values or data

**Example:**

```python
student_age = 20
employee_name = "Alice"
```

---

## 4. Constant Names

* Use **ALL\_UPPERCASE** with words separated by underscores

**Example:**

```python
MAX_LOGIN_ATTEMPTS = 3
PI = 3.14159
```

---

## 5. Module and Package Names

* Use **short, all lowercase names**
* Underscores are acceptable for readability

**Example:**

```python
# module name: student_utils.py
# package name: university
```

---

## 6. Global Variable Names

* Same as variable naming (snake\_case)
* Prefix with underscore if internal use only

**Example:**

```python
global_count = 0
_internal_flag = True
```

---

## 7. Private Variable and Function Names

* Prefix with a **single underscore** to indicate internal use
* Use **double underscore** for name mangling in classes

**Example:**

```python
class Student:
    def __init__(self):
        self._id = None
        self.__password = "secret"
```

---

## 8. Magic Methods (Dunder Methods)

* Begin and end with **double underscores**

**Example:**

```python
def __init__(self):
    pass

def __str__(self):
    return "Student"
```

---

## Complete Example

```python
MAX_STUDENTS = 30

def register_student(name):
    print(f"Registering {name}")

class CourseManager:
    def __init__(self, course_name):
        self.course_name = course_name
        self._students = []

    def add_student(self, name):
        if len(self._students) < MAX_STUDENTS:
            self._students.append(name)
            register_student(name)

    def __str__(self):
        return f"Course: {self.course_name}"
```

---

## Summary Table

| Element        | Convention     | Example                       |
| -------------- | -------------- | ----------------------------- |
| Class          | PascalCase     | `StudentRecord`               |
| Function       | snake\_case    | `calculate_salary()`          |
| Variable       | snake\_case    | `student_age`                 |
| Constant       | ALL\_UPPERCASE | `MAX_ATTEMPTS`                |
| Module/Package | lowercase      | `student_utils`, `university` |
| Private Member | \_underscore   | `_id`, `__password`           |
| Magic Method   | **dunder**     | `__init__`, `__str__`         |

---

## Tips for Students

* Follow PEP 8: Use tools like `flake8`, `pylint`, or `black` to enforce it.
* Write descriptive, meaningful names.
* Be consistent with naming across files and projects.
* Avoid single-character names except for loop indices (`i`, `j`).
* Use underscores to improve readability (`student_name` not `studentname`).
