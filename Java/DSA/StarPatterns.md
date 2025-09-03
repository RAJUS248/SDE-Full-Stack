# Star Pattern Printing — Interview-Ready Notes (Python + Java)

> Beginner-friendly, production-quality solutions.
> You’ll first learn **how to think** about star patterns in plain English, then practice the **most asked patterns** with a visual, a short logic explanation, **Python code**, and **Java code with line-by-line comments**.

---

## 1) How to think about star-pattern questions (plain English)

1. **Decide the grid**
   You almost always print **row by row**. The number of rows is typically `n`.

2. **Work out what each row contains**
   Every row is a mix of **spaces** and **stars**. For each row:

   * How many **leading spaces**?
   * How many **stars**?
   * For hollow shapes, where are the **edges** (print `*`) and where are the **insides** (print space)?

3. **Translate counts into loops**

   * One **outer loop** over rows.
   * One or more **inner loops** (commonly two): one for spaces, one for stars.
   * Hollow shapes need a bit of **conditional logic** inside the star loop to decide `*` vs space.

4. **Verify with tiny inputs**
   Try `n = 1, 2, 3` mentally. Check centering, symmetry, and whether first/last rows look right.

5. **Complexity**
   All these patterns take **O(n²)** time (you print \~n characters for n rows) and **O(1)** extra space (besides the output).

---

## 2) Patterns

> Visuals use `n = 5`. Replace `n` with any positive integer in code.

### 2.1 Solid Square (n × n)

**Visual**

```
*****
*****
*****
*****
*****
```

**Logic (plain English)**
We print `n` rows. Each row is exactly `n` stars and zero spaces.

**Python**

```python
def solid_square(n: int) -> None:
    for _ in range(n):
        print('*' * n)
```

**Java (commented)**

```java
public static void solidSquare(int n) {
    // Loop through each row from 1 to n
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        // Build a line that contains exactly n stars
        StringBuilder line = new StringBuilder();
        for (int count = 1; count <= n; count++) {
            line.append('*'); // Append one star
        }
        System.out.println(line); // Print the completed row
    }
}
```

---

### 2.2 Hollow Square

**Visual**

```
*****
*   *
*   *
*   *
*****
```

**Logic (plain English)**
First and last rows are all stars. The middle rows print star at the **first** and **last** column; everything in between is space.

**Python**

```python
def hollow_square(n: int) -> None:
    for r in range(1, n + 1):
        if r == 1 or r == n:
            print('*' * n)
        else:
            if n >= 2:
                print('*' + ' ' * (n - 2) + '*')
            else:
                print('*')  # handles n = 1 edge case
```

**Java (commented)**

```java
public static void hollowSquare(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        for (int currentCol = 1; currentCol <= n; currentCol++) {
            // Border cells: top row, bottom row, first column, last column
            boolean isBorder = currentRow == 1 || currentRow == n || currentCol == 1 || currentCol == n;
            line.append(isBorder ? '*' : ' ');
        }
        System.out.println(line);
    }
}
```

---

### 2.3 Left-Aligned Half Pyramid (Increasing)

**Visual**

```
*
**
***
****
*****
```

**Logic (plain English)**
Row `r` prints exactly `r` stars. No spaces needed.

**Python**

```python
def left_half_pyramid(n: int) -> None:
    for r in range(1, n + 1):
        print('*' * r)
```

**Java (commented)**

```java
public static void leftHalfPyramid(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        // Number of stars equals the row number
        for (int k = 1; k <= currentRow; k++) {
            line.append('*');
        }
        System.out.println(line);
    }
}
```

---

### 2.4 Right-Aligned Half Pyramid (Increasing)

**Visual**

```
    *
   **
  ***
 ****
*****
```

**Logic (plain English)**
To right-align, prepend spaces. Row `r` uses `(n - r)` spaces and `r` stars.

**Python**

```python
def right_half_pyramid(n: int) -> None:
    for r in range(1, n + 1):
        print(' ' * (n - r) + '*' * r)
```

**Java (commented)**

```java
public static void rightHalfPyramid(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        // Leading spaces to push stars to the right
        for (int s = 1; s <= n - currentRow; s++) {
            line.append(' ');
        }
        // Stars equal to the row number
        for (int k = 1; k <= currentRow; k++) {
            line.append('*');
        }
        System.out.println(line);
    }
}
```

---

### 2.5 Inverted Left-Aligned Half Pyramid

**Visual**

```
*****
****
***
**
*
```

**Logic (plain English)**
Row `r` prints `n - r + 1` stars. No spaces needed.

**Python**

```python
def inverted_left_half_pyramid(n: int) -> None:
    for r in range(1, n + 1):
        print('*' * (n - r + 1))
```

**Java (commented)**

```java
public static void invertedLeftHalfPyramid(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        // Stars decrease each row
        for (int k = 1; k <= n - currentRow + 1; k++) {
            line.append('*');
        }
        System.out.println(line);
    }
}
```

---

### 2.6 Inverted Right-Aligned Half Pyramid

**Visual**

```
*****
 ****
  ***
   **
    *
```

**Logic (plain English)**
Row `r` has `(r - 1)` spaces and `(n - r + 1)` stars.

**Python**

```python
def inverted_right_half_pyramid(n: int) -> None:
    for r in range(1, n + 1):
        print(' ' * (r - 1) + '*' * (n - r + 1))
```

**Java (commented)**

```java
public static void invertedRightHalfPyramid(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        // Left spaces increase each row
        for (int s = 1; s <= currentRow - 1; s++) {
            line.append(' ');
        }
        // Stars decrease each row
        for (int k = 1; k <= n - currentRow + 1; k++) {
            line.append('*');
        }
        System.out.println(line);
    }
}
```

---

### 2.7 Full (Centered) Pyramid

**Visual**

```
    *
   ***
  *****
 *******
*********
```

**Logic (plain English)**
To center the pyramid, put `(n - r)` spaces then `(2*r - 1)` stars. The number of stars is odd and grows by 2 each row.

**Python**

```python
def full_pyramid(n: int) -> None:
    for r in range(1, n + 1):
        print(' ' * (n - r) + '*' * (2 * r - 1))
```

**Java (commented)**

```java
public static void fullPyramid(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        // Spaces to center align
        for (int s = 1; s <= n - currentRow; s++) {
            line.append(' ');
        }
        // Odd number of stars in each row
        for (int k = 1; k <= 2 * currentRow - 1; k++) {
            line.append('*');
        }
        System.out.println(line);
    }
}
```

---

### 2.8 Inverted Full (Centered) Pyramid

**Visual**

```
*********
 *******
  *****
   ***
    *
```

**Logic (plain English)**
Start wide and shrink. Row `r` uses `(r - 1)` spaces and `2*(n - r) + 1` stars.

**Python**

```python
def inverted_full_pyramid(n: int) -> None:
    for r in range(1, n + 1):
        print(' ' * (r - 1) + '*' * (2 * (n - r) + 1))
```

**Java (commented)**

```java
public static void invertedFullPyramid(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        // Spaces increase as the pyramid narrows
        for (int s = 1; s <= currentRow - 1; s++) {
            line.append(' ');
        }
        // Star count shrinks by 2 per row
        for (int k = 1; k <= 2 * (n - currentRow) + 1; k++) {
            line.append('*');
        }
        System.out.println(line);
    }
}
```

---

### 2.9 Solid Diamond

**Visual**

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

**Logic (plain English)**
It’s a full pyramid followed by an inverted full pyramid, but the bottom half starts from `n-1` rows to avoid duplicating the middle line.

**Python**

```python
def solid_diamond(n: int) -> None:
    for r in range(1, n + 1):
        print(' ' * (n - r) + '*' * (2 * r - 1))
    for r in range(n - 1, 0, -1):
        print(' ' * (n - r) + '*' * (2 * r - 1))
```

**Java (commented)**

```java
public static void solidDiamond(int n) {
    // Top half
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        for (int s = 1; s <= n - currentRow; s++) line.append(' ');
        for (int k = 1; k <= 2 * currentRow - 1; k++) line.append('*');
        System.out.println(line);
    }
    // Bottom half (start at n-1 so we don't repeat the center row)
    for (int currentRow = n - 1; currentRow >= 1; currentRow--) {
        StringBuilder line = new StringBuilder();
        for (int s = 1; s <= n - currentRow; s++) line.append(' ');
        for (int k = 1; k <= 2 * currentRow - 1; k++) line.append('*');
        System.out.println(line);
    }
}
```

---

### 2.10 Hollow Diamond

**Visual**

```
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

**Logic (plain English)**
Same spacing as the solid diamond, but inside each row we only print `*` at the first and last position of the width; everything in between is space.

**Python**

```python
def hollow_diamond(n: int) -> None:
    for r in range(1, n + 1):
        width = 2 * r - 1
        inner = ''.join('*' if c in (1, width) else ' ' for c in range(1, width + 1))
        print(' ' * (n - r) + inner)
    for r in range(n - 1, 0, -1):
        width = 2 * r - 1
        inner = ''.join('*' if c in (1, width) else ' ' for c in range(1, width + 1))
        print(' ' * (n - r) + inner)
```

**Java (commented)**

```java
public static void hollowDiamond(int n) {
    // Top half
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        int width = 2 * currentRow - 1;
        StringBuilder line = new StringBuilder();
        for (int s = 1; s <= n - currentRow; s++) line.append(' ');
        for (int c = 1; c <= width; c++) {
            boolean isEdge = (c == 1 || c == width);
            line.append(isEdge ? '*' : ' ');
        }
        System.out.println(line);
    }
    // Bottom half
    for (int currentRow = n - 1; currentRow >= 1; currentRow--) {
        int width = 2 * currentRow - 1;
        StringBuilder line = new StringBuilder();
        for (int s = 1; s <= n - currentRow; s++) line.append(' ');
        for (int c = 1; c <= width; c++) {
            boolean isEdge = (c == 1 || c == width);
            line.append(isEdge ? '*' : ' ');
        }
        System.out.println(line);
    }
}
```

---

### 2.11 Sandglass (Hourglass) — Solid

**Visual**

```
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```

**Logic (plain English)**
An inverted full pyramid followed by a full pyramid, but the bottom starts from the **second** row to avoid duplicating the narrowest line.

**Python**

```python
def sandglass(n: int) -> None:
    for r in range(1, n + 1):
        print(' ' * (r - 1) + '*' * (2 * (n - r) + 1))
    for r in range(2, n + 1):
        print(' ' * (n - r) + '*' * (2 * r - 1))
```

**Java (commented)**

```java
public static void sandglass(int n) {
    // Top inverted pyramid
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        for (int s = 1; s <= currentRow - 1; s++) line.append(' ');
        for (int k = 1; k <= 2 * (n - currentRow) + 1; k++) line.append('*');
        System.out.println(line);
    }
    // Bottom pyramid (start from 2 to avoid repeating the center line)
    for (int currentRow = 2; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        for (int s = 1; s <= n - currentRow; s++) line.append(' ');
        for (int k = 1; k <= 2 * currentRow - 1; k++) line.append('*');
        System.out.println(line);
    }
}
```

---

### 2.12 Butterfly (Solid)

**Visual**

```
*       *
**     **
***   ***
**** ****
*********
**** ****
***   ***
**     **
*       *
```

**Logic (plain English)**
For row `r`, print `r` stars, then `2*(n - r)` spaces, then `r` stars again. Mirror the top for the bottom.

**Python**

```python
def butterfly(n: int) -> None:
    for r in range(1, n + 1):
        print('*' * r + ' ' * (2 * (n - r)) + '*' * r)
    for r in range(n - 1, 0, -1):
        print('*' * r + ' ' * (2 * (n - r)) + '*' * r)
```

**Java (commented)**

```java
public static void butterfly(int n) {
    // Top half
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        for (int k = 1; k <= currentRow; k++) line.append('*');           // Left wing
        for (int s = 1; s <= 2 * (n - currentRow); s++) line.append(' '); // Gap between wings
        for (int k = 1; k <= currentRow; k++) line.append('*');           // Right wing
        System.out.println(line);
    }
    // Bottom half
    for (int currentRow = n - 1; currentRow >= 1; currentRow--) {
        StringBuilder line = new StringBuilder();
        for (int k = 1; k <= currentRow; k++) line.append('*');
        for (int s = 1; s <= 2 * (n - currentRow); s++) line.append(' ');
        for (int k = 1; k <= currentRow; k++) line.append('*');
        System.out.println(line);
    }
}
```

---

### 2.13 X Pattern (Diagonals)

**Visual**

```
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
```

**Logic (plain English)**
In an `n × n` grid, print `*` at the two diagonals: when column equals row, and when column equals `n - row + 1`. All other cells are spaces.

**Python**

```python
def x_pattern(n: int) -> None:
    for r in range(1, n + 1):
        row_chars = []
        for c in range(1, n + 1):
            row_chars.append('*' if (c == r or c == n - r + 1) else ' ')
        print(''.join(row_chars))
```

**Java (commented)**

```java
public static void xPattern(int n) {
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        for (int currentCol = 1; currentCol <= n; currentCol++) {
            boolean onDiagonal = currentCol == currentRow || currentCol == (n - currentRow + 1);
            line.append(onDiagonal ? '*' : ' ');
        }
        System.out.println(line);
    }
}
```

---

### 2.14 Plus (+) Pattern (odd `n`)

**Visual (n = 5)**

```
  *
  *
*****
  *
  *
```

**Logic (plain English)**
Find the middle index `mid = (n + 1) // 2`. Print `*` along the middle row and the middle column; spaces elsewhere.

**Python**

```python
def plus_pattern(n: int) -> None:
    if n % 2 == 0:
        raise ValueError("Use an odd n for a symmetric plus pattern.")
    mid = (n + 1) // 2
    for r in range(1, n + 1):
        row_chars = []
        for c in range(1, n + 1):
            row_chars.append('*' if (r == mid or c == mid) else ' ')
        print(''.join(row_chars))
```

**Java (commented)**

```java
public static void plusPattern(int n) {
    if (n % 2 == 0) {
        throw new IllegalArgumentException("Use an odd n for a symmetric plus pattern.");
    }
    int mid = (n + 1) / 2;
    for (int currentRow = 1; currentRow <= n; currentRow++) {
        StringBuilder line = new StringBuilder();
        for (int currentCol = 1; currentCol <= n; currentCol++) {
            boolean onPlus = currentRow == mid || currentCol == mid;
            line.append(onPlus ? '*' : ' ');
        }
        System.out.println(line);
    }
}
```

---

### 2.15 Hollow Centered Pyramid

**Visual**

```
    *
   * *
  *   *
 *     *
*********
```

**Logic (plain English)**
For the first `n-1` rows, center the “frame” using `(n - r)` leading spaces and width `2*r - 1`; print `*` at the first and last positions inside that width and spaces inside. The last row is the solid base of `2*n - 1` stars.

**Python**

```python
def hollow_pyramid(n: int) -> None:
    if n == 1:
        print('*')
        return
    for r in range(1, n):
        width = 2 * r - 1
        inner = ''.join('*' if c in (1, width) else ' ' for c in range(1, width + 1))
        print(' ' * (n - r) + inner)
    print('*' * (2 * n - 1))
```

**Java (commented)**

```java
public static void hollowPyramid(int n) {
    if (n == 1) {
        System.out.println('*');
        return;
    }
    // Upper hollow frame
    for (int currentRow = 1; currentRow <= n - 1; currentRow++) {
        int width = 2 * currentRow - 1;
        StringBuilder line = new StringBuilder();
        // Center alignment
        for (int s = 1; s <= n - currentRow; s++) line.append(' ');
        // First and last columns are stars; inside is space
        for (int c = 1; c <= width; c++) {
            boolean isEdge = (c == 1 || c == width);
            line.append(isEdge ? '*' : ' ');
        }
        System.out.println(line);
    }
    // Solid base
    StringBuilder base = new StringBuilder();
    for (int k = 1; k <= 2 * n - 1; k++) base.append('*');
    System.out.println(base);
}
```

---

## 3) Minimal, reusable templates

**Python**

```python
def centered(width_spaces: int, star_count: int) -> str:
    return ' ' * width_spaces + '*' * star_count

def edge_line(width: int) -> str:
    # Returns a string of given width where only edges are '*'
    if width <= 0:
        return ''
    if width == 1:
        return '*'
    return '*' + ' ' * (width - 2) + '*'
```

**Java (commented)**

```java
public static String centeredLine(int spaces, int stars) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < spaces; i++) sb.append(' ');
    for (int i = 0; i < stars; i++) sb.append('*');
    return sb.toString();
}

public static String edgeLine(int width) {
    StringBuilder sb = new StringBuilder();
    if (width <= 0) return "";
    if (width == 1) return "*";
    sb.append('*');
    for (int i = 0; i < width - 2; i++) sb.append(' ');
    sb.append('*');
    return sb.toString();
}
```

---

## 4) Quick checklist for interviews

* Decide **spaces** and **stars** per row first; then code.
* Confirm whether you need **solid** or **hollow**.
* For diamonds and sandglass, ensure you **don’t duplicate the center line**.
* For `+` and `X`, prefer **odd `n`** to keep symmetry.
* Test with **tiny `n`** mentally (1–3) to catch off-by-one errors fast.

---

## 5) Example driver (optional)

**Python**

```python
def demo(n: int) -> None:
    print("\nSolid Square"); solid_square(n)
    print("\nHollow Square"); hollow_square(n)
    print("\nLeft Half Pyramid"); left_half_pyramid(n)
    print("\nRight Half Pyramid"); right_half_pyramid(n)
    print("\nInverted Left Half Pyramid"); inverted_left_half_pyramid(n)
    print("\nInverted Right Half Pyramid"); inverted_right_half_pyramid(n)
    print("\nFull Pyramid"); full_pyramid(n)
    print("\nInverted Full Pyramid"); inverted_full_pyramid(n)
    print("\nSolid Diamond"); solid_diamond(n)
    print("\nHollow Diamond"); hollow_diamond(n)
    print("\nSandglass"); sandglass(n)
    print("\nButterfly"); butterfly(n)
    print("\nX Pattern"); x_pattern(n)
    print("\nPlus Pattern"); plus_pattern(n if n % 2 == 1 else n + 1)
    print("\nHollow Pyramid"); hollow_pyramid(n)

# demo(5)
```

**Java**

```java
public static void demo(int n) {
    System.out.println("\nSolid Square");        solidSquare(n);
    System.out.println("\nHollow Square");       hollowSquare(n);
    System.out.println("\nLeft Half Pyramid");   leftHalfPyramid(n);
    System.out.println("\nRight Half Pyramid");  rightHalfPyramid(n);
    System.out.println("\nInv Left Half Pyramid"); invertedLeftHalfPyramid(n);
    System.out.println("\nInv Right Half Pyramid"); invertedRightHalfPyramid(n);
    System.out.println("\nFull Pyramid");        fullPyramid(n);
    System.out.println("\nInverted Full Pyramid"); invertedFullPyramid(n);
    System.out.println("\nSolid Diamond");       solidDiamond(n);
    System.out.println("\nHollow Diamond");      hollowDiamond(n);
    System.out.println("\nSandglass");           sandglass(n);
    System.out.println("\nButterfly");           butterfly(n);
    System.out.println("\nX Pattern");           xPattern(n);
    System.out.println("\nPlus Pattern");        plusPattern(n % 2 == 1 ? n : n + 1);
    System.out.println("\nHollow Pyramid");      hollowPyramid(n);
}
```

---

### Final note

All solutions are **O(n²)** time and **O(1)** extra space. Practice recognizing the **counts per row** (spaces, stars) and these questions will feel mechanical. If you want this as a printable `.md` or class handout PDF/Word, say the word and I’ll package it neatly.
