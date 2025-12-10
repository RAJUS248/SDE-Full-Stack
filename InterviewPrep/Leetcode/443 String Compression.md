Here are the **clean, regenerated notes** with **only Algorithm 1 (the optimal solution)** included — no Algorithm 2 or 3.

---

# 🧠 **LeetCode 443 — String Compression (Medium)**

**Pattern:** Two Pointers
**Key Concepts:** In-place modification, run-length encoding, constant space

---

# 📘 **Problem Summary**

Given an array of characters `chars`, compress it **in place** using the rules:

* For each group of **consecutive repeating** characters:

  * If count = 1 → write only the character
  * If count > 1 → write the character followed by each digit of the count
* Multi-digit counts must be split (e.g., 12 → `"1","2"`)
* Return the **new length** of the compressed array
* Characters beyond that returned length should be ignored

---

# 🔍 **Example**

### Example 1

Input:

```
["a","a","b","b","c","c","c"]
```

Output:

```
6  
["a","2","b","2","c","3"]
```

### Example 2

Input:

```
["a"]
```

Output:

```
1
["a"]
```

---

# 🎯 **Key Insight**

The solution requires two things:

1. **Scanning groups** of repeating characters
2. **Writing the compressed form back into the same array**, ensuring **O(1) extra space**

This is naturally solved using a **two-pointer technique**:

* `i` → read pointer (finds groups)
* `write` → write pointer (writes compressed output)

---

# 1️⃣ **Algorithm — Two Pointers (Optimal Solution)**

**Time:** O(n)
**Space:** O(1)

### 🚀 Approach

1. Start `i = 0` and `write = 0`
2. While scanning:

   * Let `j = i`
   * Move `j` until characters differ
   * Write the character at `chars[i]` to `chars[write]`
   * If count > 1, write each digit of the count into the array
   * Move `i = j`
3. Return `write` as the new length

---

# 🧑‍💻 **Python Code (Clean & Efficient)**

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        
        while i < len(chars):
            char = chars[i]
            j = i
            
            # Count consecutive characters
            while j < len(chars) and chars[j] == char:
                j += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            count = j - i
            
            # Write digits of count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            # Move i to the next group
            i = j
        
        return write
```

---

# 🔬 **Complexity Analysis**

| Metric               | Value                                         |
| -------------------- | --------------------------------------------- |
| **Time Complexity**  | O(n) — each character processed at most twice |
| **Space Complexity** | O(1) — constant extra space                   |

This meets the problem’s strict in-place and space requirements.

---

# 🧠 **Edge Cases to Watch**

* All characters are unique → no compression
* All characters are the same → long count (ex: `"12" → '1','2'`)
* Very long sequences
* Mixed short/long groups
* Array of length 1

---

# 🧪 **Walkthrough Example**

Input:

```
["a","a","a","b","b","c"]
```

Steps:

* `"aaa"` → write `"a","3"`
* `"bb"` → write `"b","2"`
* `"c"` → write `"c"`

Output array:

```
["a","3","b","2","c"]
```

New length: **5**

---

# 📝 **Interview Tips**

* Emphasize **two-pointer technique** from the start
* Highlight **O(1) extra space** and **why building a string is not allowed**
* Mention handling **multi-digit numbers** (common pitfall)
* Keep the implementation simple: one loop for groups, one for writing digits

