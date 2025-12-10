Below is a **regenerated, expanded, polished set of LeetCode-style notes** for
**9. Palindrome Number**, now including **multiple algorithms** with **different time & space complexities**, plus explanations, examples, pros/cons, and code.

---

# 🔢 **LeetCode 9 — Palindrome Number (Easy)**

**Problem:**
Given an integer `x`, return `true` if it is a **palindrome**, otherwise `false`.

A number is a palindrome if it reads the same forward and backward.

---

# 📌 **Key Observations**

### 1. Negative numbers → **Never palindromes**

Because of the `-` sign.

### 2. Numbers ending with `0` (except `0` itself) → **Not palindromes**

Example: `10` → becomes `01`

### 3. We can solve this problem using:

* Arithmetic reversal
* String conversion
* Reversing only half (**optimal**)
* Digit-by-digit two-pointer math (no string, no reverse)
* Counting digits + comparing ends

---

# 🧠 **Algorithms (Multiple Time & Space Complexities)**

Below are **4 different methods**, each with **different complexity** characteristics.

---

# -------------------------------------------------------

# ✅ **Algorithm 1: Reverse Half the Number (Optimal)**

### ✔ Time: **O(log n)**

### ✔ Space: **O(1)**

### 🏆 Recommended for Interviews

### Idea:

* Build the reverse of only half the digits.
* Compare the two halves.

### Code (Python)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversedHalf = 0
        while x > reversedHalf:
            reversedHalf = reversedHalf * 10 + x % 10
            x //= 10

        return x == reversedHalf or x == reversedHalf // 10
```

---

# -------------------------------------------------------

# ✅ **Algorithm 2: Reverse the Entire Integer**

### ✔ Time: **O(log n)**

### ✔ Space: **O(1)**

### ⚠ Might overflow in languages like Java/C++

### Idea:

* Reverse the number using modulo operations.
* Compare with the original.

### Code (Python)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversedNum = 0
        
        while x > 0:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10
        
        return original == reversedNum
```

### Pros:

* Simple and easy to explain.

### Cons:

* Risk of overflow in some languages.

---

# -------------------------------------------------------

# ✅ **Algorithm 3: Use String Conversion**

### ✔ Time: **O(n)**

### ✔ Space: **O(n)**

### 👶 Easiest, but not optimal

### Idea:

* Convert to string
* Use two-pointer comparison or check reverse

### Code (Python)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
```

Or explicitly:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
```

### Pros:

* Very easy

### Cons:

* Uses extra memory
* Many interviews disallow converting to string

---

# -------------------------------------------------------

# ✅ **Algorithm 4: Compare Digits from Both Ends (Math Two-Pointer)**

### ✔ Time: **O(log n)**

### ✔ Space: **O(1)**

### 💡 No reversing, no string conversion

### Idea:

1. Count digits
2. Extract leftmost and rightmost digits
3. Compare them
4. Shrink range and repeat

### Code (Python)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Find highest place value
        div = 1
        while x // div >= 10:
            div *= 10
        
        while x > 0:
            left = x // div
            right = x % 10
            
            if left != right:
                return False
            
            # Remove leftmost and rightmost digits
            x = (x % div) // 10
            div //= 100
        
        return True
```

### Pros:

* No extra memory
* Cleaner math-based approach
* Avoids reversing numbers
* Good discussion-based solution

---

# 🧪 Example Walkthrough: x = 1221 (Half-Reversal Method)

```
x = 1221
reversedHalf = 0

Take 1 → reversedHalf = 1, x = 122
Take 2 → reversedHalf = 12, x = 12
Stop when reversedHalf >= x

Compare → 12 == 12 → palindrome
```

---

# 📊 **Complexity Summary Table**

| Algorithm                     | Description            | Time         | Space    |
| ----------------------------- | ---------------------- | ------------ | -------- |
| **1. Reverse half (optimal)** | Fastest & safest       | **O(log n)** | **O(1)** |
| **2. Reverse whole**          | Simple but risky       | O(log n)     | O(1)     |
| **3. String conversion**      | Easiest                | **O(n)**     | **O(n)** |
| **4. Math two-pointer**       | Compare ends digitally | **O(log n)** | **O(1)** |

---

# 📝 **Final Interview Notes**

* Always reject **negative** numbers
* Reject numbers ending with **0** except **0**
* Avoid unnecessary string conversion
* Reversing **half** is the optimal strategy
* Math-based digit comparison shows strong fundamentals
