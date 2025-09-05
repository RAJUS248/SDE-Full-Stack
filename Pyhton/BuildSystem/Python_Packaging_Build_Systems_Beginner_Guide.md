# Packaging Python Software — Beginner-Friendly Guide for Engineers

**Audience:** Computer Science & Engineering students who already write Python scripts and now want to understand how Python is packaged, shipped, and consumed in real-world projects.

---

## 1) Why Packaging Matters

In the **software industry**, customers rarely get raw source code. Instead, they get a **built artifact**:
- For Java: usually JARs or WARs.
- For Python: wheels (`.whl`), source distributions (`.tar.gz`), or sometimes **binary executables** built with special tools.

### The Goals of Packaging
- **Reusability**: publish a library others can `pip install`.
- **Distribution**: ship your app as a binary (no Python knowledge required).
- **Protection**: limit exposure of source code (though Python is inherently more open).

---

## 2) What Happens When You Install a Python Package

When you run:
```bash
pip install requests
```
- `pip` downloads a **wheel** (`.whl`) or **source distribution** from [PyPI](https://pypi.org/).
- A wheel is basically a **zip archive of precompiled Python bytecode (`.pyc`) + metadata**.
- Installed code usually sits in `site-packages/` inside your environment.

So, open-source Python **is usually shipped as readable source**, but it can also include **precompiled binaries** (extensions in C/C++/Rust).

---

## 3) Can Python Code Be Delivered Without Source?

Yes, but with caveats.

1. **Default (open source / PyPI)**: packages include `.py` source files → readable.  
2. **Obfuscation**: tools like `pyarmor`, `cython`, `nuitka` can turn `.py` into C extensions (`.pyd`/`.so`) or compiled binaries.  
3. **Binary-only delivery**:
   - Freeze entire app into a binary with **PyInstaller**, **cx_Freeze**, or **py2exe** (Windows).  
   - Build a self-contained executable that bundles the **Python interpreter + libraries**.  

⚠️ But note: Python is not as opaque as C++ or Java. Even binaries can often be reverse-engineered. Most companies use licensing, cloud services, or APIs for protection rather than “hiding Python code.”

---

## 4) Famous Build & Packaging Systems in Python

| Tool / Standard | What It Does | Industry Use |
|---|---|---|
| **Setuptools** (`setup.py`) | Oldest, most common | Legacy + still widely used |
| **Poetry** | Modern dependency management + build | Growing fast, beginner-friendly |
| **Flit** | Minimal packaging | Small projects |
| **Hatch** | Flexible, modern build | Advanced projects |
| **PyInstaller** | Freezes Python app into a standalone binary | Desktop apps, shipping closed-source |
| **Cython / Nuitka** | Compile Python to C/C++ → binary | Performance + protection |

> The new standard is **PEP 517/518** with `pyproject.toml`. This file declares how your package is built (setuptools, poetry, flit, etc.).

---

## 5) Simple Multi-Module Python Project

Imagine this structure:

```
python-packaging-demo/
├─ pyproject.toml
├─ README.md
├─ app/
│  ├─ __init__.py
│  ├─ main.py          # Entry point
│  └─ greeter.py       # A helper class
├─ utils/
│  ├─ __init__.py
│  └─ file_loader.py   # Uses open-source library (pathlib, or `click`)
```

### 5.1 Example Code

**`app/greeter.py`**
```python
class Greeter:
    @staticmethod
    def greet(name: str) -> str:
        return f"Hello, {name}!"
```

**`utils/file_loader.py`**
```python
from pathlib import Path

class FileLoader:
    @staticmethod
    def read_text(path: str) -> str:
        return Path(path).read_text(encoding="utf-8")
```

**`app/main.py`**
```python
from app.greeter import Greeter
from utils.file_loader import FileLoader

def main():
    print(Greeter.greet("Algorithms365"))
    content = FileLoader.read_text("data/message.txt")
    print("File content:", content)

if __name__ == "__main__":
    main()
```

---

## 6) pyproject.toml (Modern Build Config)

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "python-packaging-demo"
version = "0.1.0"
description = "Demo project showing Python packaging"
authors = [
  {name="Student Name", email="student@example.com"}
]
dependencies = []

[project.scripts]
demo-app = "app.main:main"
```

Run:
```bash
pip install build
python -m build
```

This creates:
- `dist/python_packaging_demo-0.1.0-py3-none-any.whl`  
- `dist/python_packaging_demo-0.1.0.tar.gz`  

Users can now install via:
```bash
pip install dist/python_packaging_demo-0.1.0-py3-none-any.whl
```

And run:
```bash
demo-app
```

---

## 7) Delivering Python as a Binary

To hide code or ship to non-technical end users:
```bash
pip install pyinstaller
pyinstaller --onefile app/main.py
```

Output: `dist/main` (Linux/Mac) or `dist/main.exe` (Windows).  
This binary includes Python interpreter + libs. End user doesn’t need Python installed.

> Downside: larger files, reverse-engineerable, less portable across OSes.

---

## 8) Open Source & Industry Perspective

- **Open Source**: Packages are shared as wheels/source on PyPI. Anyone can read/learn/contribute.  
- **Closed Source / Enterprise**: Companies either:
  - Deliver **binary executables** (PyInstaller).
  - Provide **APIs/Cloud services** instead of shipping code.  
- **Your Career**: Learn to package with `pyproject.toml`, publish to TestPyPI, then real PyPI. Employers value the skill of turning “scripts” into “installable packages.”

---

## 9) Practice Ideas

1. Convert a simple script into a `pyproject.toml` package.  
2. Publish it to **TestPyPI** (not public yet).  
3. Build a **PyInstaller binary** and run on a friend’s machine without Python installed.  
4. Explore `poetry` (`pip install poetry`) and create the same project with its commands.  

---

## 10) Key Takeaways

- Python packages are usually **source-based** but can also be shipped as **wheels** or **binaries**.  
- Standard build tools: `setuptools`, `flit`, `poetry`, `hatch`.  
- Binary tools: `pyinstaller`, `cx_Freeze`, `nuitka`.  
- Industry delivers Python in 2 main ways:
  - Open source (readable, reusable, PyPI).  
  - Closed source (binary executables, APIs).  

✅ With this, you can now turn your Python scripts into real packages, ship them to others, or even publish them on PyPI!  
