# Python Libraries for File & Network I/O — An Intro with Two Practical Examples

**Audience:** Beginner CS/CE students who want to use Python’s libraries to do real work—reading files and making network requests—without getting lost in advanced topics on day one.

---

## Why Libraries? (And Why This Matters)
Early programmers wrote everything from scratch: opening files, parsing formats, talking to servers. That meant **duplicate work**, **hidden bugs**, and **slow progress**. Modern software development relies on **libraries**:
- The **standard library** (ships with Python) gives you reliable building blocks like `pathlib` for files and `urllib` for HTTP.
- **Open‑source packages** (installed from [PyPI](https://pypi.org/)) add power and convenience (e.g., `requests` for HTTP).  
- Over time, innovations solidify into libraries and frameworks—so you get **reusable, documented, battle‑tested** code instead of reinventing it.

> Goal today: Learn to **use** a library, **find** its docs quickly, and **ship working code**. We’ll keep it simple and professional—no exception handling yet—so you can focus on the core ideas.

---

## The Two Things You’ll Do All the Time
1) **File I/O**: Open a local text file and print its contents.  
2) **Network I/O**: Call a web URL and print the response.

We’ll use:
- `pathlib.Path` (standard library) for files.
- `requests` (popular open‑source package) for HTTP. Install with: `pip install requests`.

---

## Example 1 — Read a Text File and Print It (Standard Library: `pathlib`)

```python
from __future__ import annotations

from pathlib import Path

def read_text_file(path: Path, encoding: str = "utf-8") -> str:
    """
    Return the full text content of a local file.
    This introductory example omits error handling on purpose.
    """
    return path.read_text(encoding=encoding)

def main() -> None:
    data_dir: Path = Path("data")
    file_path: Path = data_dir / "notes.txt"

    # Ensure the folder exists and create a starter file if missing.
    data_dir.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        file_path.write_text("Hello from Algorithms365!\n", encoding="utf-8")

    content: str = read_text_file(file_path)
    print(content)

if __name__ == "__main__":
    main()
```

**What to notice**
- `Path` makes file paths clear and cross‑platform.
- We explicitly set `encoding="utf-8"` for predictable text behavior.
- The example **intentionally** has no exception handling—this is an intro to the API shape and basic flow.

---

## Example 2 — Make an HTTP GET Request and Print the Response (Open‑Source: `requests`)

```python
from __future__ import annotations

import requests

def fetch_text(url: str, timeout_seconds: float = 5.0) -> str:
    """
    Perform a simple HTTP GET and return the response body as text.
    This introductory example omits error handling on purpose.
    """
    response = requests.get(url, timeout=timeout_seconds)
    return response.text

def main() -> None:
    url: str = "https://httpbin.org/get"
    body: str = fetch_text(url)
    print(body)

if __name__ == "__main__":
    main()
```

**What to notice**
- `requests` is a widely‑used open‑source HTTP client that’s more ergonomic than low‑level alternatives.
- We pass a `timeout` to avoid indefinite waits.
- Again, no exception handling yet—focus on understanding how to **call the API** and **use the response**.

---

## How to Learn (Don’t Memorize — Search Smart)
- **Standard library docs**: Browse the library index at https://docs.python.org/3/ and search terms like “pathlib read_text”.
- **Open‑source packages**: Find them on https://pypi.org/ (e.g., “requests”) and follow the link to their documentation.
- In your editor or REPL, try `help(Path)`, `help(Path.read_text)`, and `help(requests.get)` to discover arguments and return values.

---

## Mini‑Checklist for Professional Style (Even in Simple Scripts)
- Prefer **clear names** (`read_text_file`, `fetch_text`, `file_path`).
- Keep **one responsibility per function**.
- Use **type hints** (`str`, `Path`, `float`) and docstrings for self‑documenting code.
- Encode text explicitly (`utf-8`) to avoid surprises across systems.
- Add exception handling later, once you’ve understood the happy‑path flow.

---

## Practice Ideas
- Change the file path and write your own starter content; re‑run and observe the output.
- Point the network call to another URL (e.g., a public JSON API) and print the first 200 characters of the result.
- Replace `requests` with `httpx` later to explore a modern alternative (keep the structure the same).

---

**You now have two building blocks you’ll use everywhere.** Start simple, read the docs when stuck, and iterate from working code to production‑grade code step by step.
