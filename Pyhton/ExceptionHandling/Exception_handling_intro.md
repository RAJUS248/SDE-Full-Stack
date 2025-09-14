
# Exception Handling in Clean Code (Python & Java, File I/O Examples)

---

## 1️⃣ Why `try–catch–finally` Exists?

* In **early programming languages** (like C), error handling was done by:

  * Returning **error codes** (e.g., `-1`, `NULL`).
  * Setting **global flags** (`errno` in C).
* **Problems with this:**

  * Easy to **forget to check** the return code.
  * Mixed **happy path logic** with **error checking**, making code noisy.
  * Resource leaks (files, memory) when a function failed but cleanup was skipped.
* **Solution → Structured Exception Handling**:

  * Introduced in the **1980s–1990s**:

    * Ada (1983), C++ (1990), Java (1995 with checked exceptions).
    * Python adopted it from its **first release (1991)**.
  * `try–catch–finally` separated:

    * **Happy path logic** → in the `try`.
    * **Error recovery** → in `catch` (Python: `except`).
    * **Cleanup always** → in `finally`.

💡 **Impact:** Programs became **cleaner, safer, and more reliable**.

---

## 2️⃣ Basic Syntax

### In **Python**

```python
try:
    # risky code
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File does not exist!")
finally:
    # always runs
    print("Cleaning up...")
    file.close()
```

---

### In **Java**

```java
try {
    // risky code
    FileReader reader = new FileReader("data.txt");
    BufferedReader br = new BufferedReader(reader);
    String content = br.readLine();
} catch (FileNotFoundException e) {
    System.out.println("File does not exist!");
} finally {
    // always runs
    System.out.println("Cleaning up...");
    // must close resources manually here
}
```

---

## 3️⃣ Simple Example for Beginners (Step by Step)

Imagine: **Read a file that might not exist.**

### Pseudocode

```
TRY to open the file
    read contents
CATCH file-not-found
    tell user "file missing"
FINALLY
    close file if it was opened
```

---

### Python Example

```python
def read_file(path: str) -> None:
    try:
        f = open(path, "r", encoding="utf-8")
        print("File contents:", f.read())
    except FileNotFoundError:
        print("⚠️ Error: File not found at", path)
    finally:
        print("Closing file (if opened)")
        try:
            f.close()
        except Exception:
            pass  # ignore if file never opened

# Demo
read_file("ok.txt")      # prints contents
read_file("missing.txt") # shows error, still cleans up
```

---

### Java Example

```java
import java.io.*;

public class TryCatchDemo {
    public static void readFile(String path) {
        FileReader reader = null;
        try {
            reader = new FileReader(path);
            BufferedReader br = new BufferedReader(reader);
            System.out.println("File contents: " + br.readLine());
        } catch (FileNotFoundException e) {
            System.out.println("⚠️ Error: File not found at " + path);
        } catch (IOException e) {
            System.out.println("⚠️ Error reading file: " + e.getMessage());
        } finally {
            System.out.println("Closing file (if opened)");
            try {
                if (reader != null) reader.close();
            } catch (IOException ignored) {}
        }
    }

    public static void main(String[] args) {
        readFile("ok.txt");     // normal case
        readFile("missing.txt");// error case
    }
}
```

---

# 🚀 Throwing Exceptions in Java and Python

##  Why Do We "Throw" Exceptions?

* Sometimes, your code **detects a problem** (like invalid input, missing file, or division by zero).
* Instead of handling it immediately, you may want to **signal (throw) an error** to the caller.
* This allows **cleaner error handling** and avoids messy `if-else` checks everywhere.

---

##  Throwing Exceptions in **Java**

### Syntax:

```java
throw new ExceptionType("Message");
```

* `throw` → keyword to raise an exception.
* `new ExceptionType()` → creates an exception object.

### Example:

```java
class AgeChecker {
    public static void checkAge(int age) throws Exception {
        if (age < 18) {
            throw new Exception("Age must be 18 or above!");
        }
        System.out.println("Valid age: " + age);
    }

    public static void main(String[] args) {
        try {
            checkAge(15);  // ❌ This will throw exception
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

👉 Output:

```
Error: Age must be 18 or above!
```

---

### Throwing Exceptions in **Python**

### Syntax:

```python
raise ExceptionType("Message")
```

* `raise` → keyword to raise an exception.
* `ExceptionType()` → creates an exception object.

### Example:

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above!")
    print("Valid age:", age)

try:
    check_age(15)  # ❌ This will raise exception
except ValueError as e:
    print("Error:", e)
```

👉 Output:

```
Error: Age must be 18 or above!
```

---

## 🔑 Key Difference

* **Java** uses `throw new ExceptionType(...)`
* **Python** uses `raise ExceptionType(...)`

Both mean: **"Stop here and pass the error to the caller!"** 🚦


---

✅ **Beginner Takeaway**

* `try` = where we put risky code.
* `catch`/`except` = handle the error.
* `finally` = cleanup always runs, success or failure.

👉 Later, we’ll see how **Clean Code best practices** refine this pattern: keep `try` blocks small, translate exceptions, log once, and use modern constructs (`with` in Python, try-with-resources in Java).

