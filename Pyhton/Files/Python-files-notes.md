# Using Libraries in Python
---

## 📌 Introduction

In Python, **libraries (modules and packages)** are reusable sets of code that simplify development by providing pre-built solutions for common tasks like **file handling, networking, data processing, and machine learning**.

This note will cover:

* What libraries are and why they exist
* File operations (`create`, `read`, `write`, `append`, `delete`)
* Who implements library functions
* How to view and debug library source code
* Shipping software: bundling dependencies
* Why Python is called **“batteries included”**
* Best practices for managing libraries

---

## 📚 What is a Library in Python?

* A **module** is a single `.py` file with reusable functions and classes.
* A **package** is a directory containing multiple modules with an `__init__.py`.

### Examples:

* **Standard Library**: `os`, `sys`, `math`, `datetime`, `json`
* **File Handling Libraries**: `os`, `shutil`, built-in `open()`
* **Third-Party Libraries**: NumPy, Pandas, Requests

✅ Python’s **standard library** is one of its biggest strengths: it is very large, covering almost every common use case.

---

## 🖼️ Diagram — How Libraries Fit Into Python Execution

```
+--------------------------------------------------+
|                Your Python Script                |
|  (Functions, Classes, Code you write)            |
+--------------------------------------------------+
                |   imports
                v
+--------------------------------------------------+
|         Python Libraries (Standard + External)   |
|   e.g., os, sys, open(), pandas, requests, etc.  |
+--------------------------------------------------+
                |   executed by
                v
+--------------------------------------------------+
|           Python Interpreter (CPython)           |
|   - Imports and compiles .py to .pyc (bytecode)  |
|   - Handles execution, memory, exceptions        |
+--------------------------------------------------+
                |   system calls
                v
+--------------------------------------------------+
|          Operating System (Windows/Linux/Mac)    |
|   - File System APIs (create, read, write files) |
|   - Network APIs, Process Management, Threads    |
+--------------------------------------------------+
```

---

## 📁 File Handling in Python

Python makes file handling **simple and concise** with the built-in `open()` function and the `os` module.

### Common Operations

1. **Open/Create a File** → `open("file.txt", "w")`
2. **Read File** → `open("file.txt", "r")`
3. **Write File** → `open("file.txt", "w")`
4. **Append to File** → `open("file.txt", "a")`
5. **Delete File** → `os.remove("file.txt")`

---

### Examples

#### 1. Creating/Writing to a File

```python
# Write mode ('w') creates the file if it doesn't exist
with open("example.txt", "w") as f:
    f.write("Hello, Python File Handling!\n")
    f.write("This is a new line of text.")
```

#### 2. Reading a File

```python
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```

#### 3. Appending to a File

```python
with open("example.txt", "a") as f:
    f.write("\nAppended line of text.")
```

#### 4. Deleting a File

```python
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted.")
else:
    print("File not found.")
```

---

## 👩‍💻 Who Implements These Library Functions?

* **Standard Libraries** → Maintained by the Python core team (CPython contributors).
* **Third-Party Libraries** → Open-source communities (e.g., NumPy by Travis Oliphant, Pandas by Wes McKinney).
* **Custom Libraries** → You can create your own `.py` modules or packages and reuse them.

📌 Like Java, these functions are not “magic” — they are written in **Python and C**, tested, and shared.

---

## 🔍 Finding Library Source Code

1. **Python Standard Library**:

   * Found in the `Lib/` directory of your Python installation.
   * Example path: `/usr/lib/python3.10/`

2. **Third-Party Libraries**:

   * Installed via `pip`, usually inside `site-packages/`.
   * Open source → available on GitHub.

👉 You can even use Python’s `inspect` module to see the source:

```python
import inspect, os
print(inspect.getsource(os.remove))
```

---

## 🐞 Debugging into Library Code

Yes ✅

* IDEs like **PyCharm, VSCode** let you step into library functions.
* You can attach the library source (or use `pip install <pkg> --editable`).
* If C extensions are used (e.g., NumPy internals), you may only see wrappers.

---

## 📦 Shipping Software — Do We Ship Libraries Too?

| Library Type                | Ship It?                                                           |
| --------------------------- | ------------------------------------------------------------------ |
| **Python Standard Library** | ❌ No — included with Python.                                       |
| **Third-Party Libraries**   | ✅ Yes — must bundle via `requirements.txt` or virtual environment. |
| **Custom Libraries**        | ✅ Yes — include your `.py` or package.                             |

### Bundling Options

* **requirements.txt** → for `pip install -r requirements.txt`
* **Virtual Environment / venv** → ship with dependencies installed
* **Wheel (`.whl`) / Package** → distribute via PyPI
* **Standalone (PyInstaller, cx\_Freeze)** → bundle everything into an `.exe`

---

## 🔋 Why “Batteries Included”?

Python philosophy: **batteries included**.

* Standard library covers:

  * File handling
  * Networking (`socket`, `http`)
  * OS interaction (`os`, `sys`)
  * Data processing (`json`, `csv`)
  * Threading, multiprocessing
  * Testing (`unittest`)

This means you can do a lot without third-party dependencies.

---

## 👨‍💻 Who Writes Library Source Code?

* **Python Core Developers** (PSF & CPython maintainers).
* **Open-Source Communities** (NumPy, Flask, Django).
* **You** — anyone can publish packages on **PyPI** (Python Package Index).

📍 Explore:

* [CPython GitHub Repository](https://github.com/python/cpython)
* [PyPI Repository](https://pypi.org/)

---

## 🔄 Comparison with Other Languages

| Operation | Python (`open`, `os`)   | Java (`java.io`)           | C (`stdio.h`)           |
| --------- | ----------------------- | -------------------------- | ----------------------- |
| Create    | `open("file.txt", "w")` | `File.createNewFile()`     | `fopen("file.txt","w")` |
| Read      | `open("file.txt", "r")` | `Scanner` / `FileReader`   | `fopen("file.txt","r")` |
| Write     | `open("file.txt", "w")` | `FileWriter`               | `fprintf()`             |
| Append    | `open("file.txt", "a")` | `FileWriter("file", true)` | `fopen("file.txt","a")` |
| Delete    | `os.remove("file.txt")` | `file.delete()`            | `remove("file.txt")`    |

---

## ✅ Summary (Skill-Oriented Takeaways)

* **Libraries** are reusable code collections (modules/packages).
* Python has a very rich **standard library** (batteries included).
* Source code is open — you can read and debug into it.
* When shipping:

  * Standard library → already included.
  * Third-party/custom → bundle via `requirements.txt`, `venv`, or `.whl`.
* Learn how to trace into library code — helps in **debugging & mastery**.
* Dependency managers (`pip`, `venv`, `poetry`) make library management professional.
