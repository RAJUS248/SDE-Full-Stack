# Advanced Loop Lesson — Mastering Python Loops with Star Patterns

> This is a **hands-on, advanced loop lesson** in Python. We’ll build mastery through small, focused examples and grow into complex patterns.
>
> Design rules we’ll follow throughout:
> - Index from **1** up to **`<= max`** (using `range(1, max_value + 1)`).
> - Use **descriptive variable names**: `row`, `row_max`, `column`, `column_max`, `width_max`, `height_max`, `depth_max`.
> - For each printed line, **build a string, then print once** (fewer bugs, easier to debug).
> - Add **clear comments** above tricky loops and conditions.

---

## How to Derive Loop Logic (Recipe)

1. **Sketch small cases** (try `row_max = 3` or `4`).  
2. Decide **for each row**: how many **spaces** and how many **stars**?  
3. Turn those counts into **two loops** (spaces first, then stars).  
4. Keep **outer loop = rows**, **inner loops = counts**.  
5. Use **`range(1, count + 1)`** to preserve the 1..`<= max` mental model.  
6. **Build, then print** each line to avoid partial outputs and to simplify debugging.

---

## Debugging Off-by-One & Alignment

- If the shape is **shifted**, re-check **space** counts.  
- If the shape is **too wide or narrow**, re-check **star** formulas (e.g., `2*row - 1`).  
- Always test **tiny heights** (`row_max = 1, 2, 3, 4`) to spot mistakes early.

---

## 1) Example: Print 100 stars sequentially (single line)

### Goal
Print exactly 100 `*` characters in a single line.

```python
def print_hundred_stars_single_line() -> None:
    """Print 100 '*' characters in one line."""
    count_max = 100
    line = ''.join('*' for _ in range(1, count_max + 1))
    print(line)

# Demo
if __name__ == '__main__':
    print('Example 1: 100 stars in one line')
    print_hundred_stars_single_line()
    print()
```

**Key idea:** When you know **exact repetition count**, generate with a comprehension or a simple loop.

---

## 2) Example: Print 100 stars in a 10 × 10 grid

### Goal
Arrange 100 stars as a 10-row by 10-column grid.

```python
def print_stars_grid_10x10() -> None:
    """Print a 10 by 10 grid of '*' (total 100 stars)."""
    row_max = 10
    column_max = 10
    for row in range(1, row_max + 1):
        # Build a row with exactly 10 '*' characters
        line = ''.join('*' for column in range(1, column_max + 1))
        print(line)

# Demo
if __name__ == '__main__':
    print('Example 2: 10x10 grid of stars')
    print_stars_grid_10x10()
    print()
```

**Loop roles:**
- **Outer loop** drives **rows** (lines).
- **Inner loop** builds **columns** (characters per line).

---

## 3) Example: From a list of integers, print those many stars — one star per new line

### Goal
Given a list of non-negative integers, print **that many lines** each containing a single `*`.  
For example, for `[3, 1, 4]`, print:
```
*
*
*
*
****  (see variant B below for line-of-stars version)
```
To eliminate ambiguity, we provide **two common variants**:

### Variant A — **One star per line (as specified)**
```python
from typing import Iterable

def print_one_star_per_line_from_counts(counts: Iterable[int] | None) -> None:
    """For each integer n in counts, print n lines each with a single '*'."""
    if counts is None:
        print('(no data)')
        return

    counts_list = [max(0, int(n)) for n in counts]  # clamp negatives to 0
    for row in range(1, len(counts_list) + 1):
        lines_to_print = counts_list[row - 1]
        for column in range(1, lines_to_print + 1):
            print('*')

# Demo
if __name__ == '__main__':
    print('Example 3A: one star per line per count')
    print_one_star_per_line_from_counts([3, 1, 4])
    print()
```

### Variant B — **All stars for a number on the same line** (popular interview variant)
```python
def print_stars_per_count_on_one_line(counts: Iterable[int] | None) -> None:
    """For each integer n in counts, print one line of n '*' characters."""
    if counts is None:
        print('(no data)')
        return

    counts_list = [max(0, int(n)) for n in counts]  # clamp negatives to 0
    for row in range(1, len(counts_list) + 1):
        column_max = counts_list[row - 1]
        line = ''.join('*' for column in range(1, column_max + 1))
        print(line)

# Demo
if __name__ == '__main__':
    print('Example 3B: stars per count on one line')
    print_stars_per_count_on_one_line([3, 1, 4, 0, 2])
    print()
```

---

## 4) Example: Print stars **alternatively** (skip one, print one)

### Goal
Given a length (e.g., 20), print positions 1, 3, 5, ... as `*` and positions 2, 4, 6, ... as spaces.

```python
def print_alternate_stars(length_max: int) -> None:
    """Print '*' at odd positions and ' ' (space) at even positions."""
    if length_max < 0:
        length_max = 0

    # Build one line with alternate stars
    chars = []
    for column in range(1, length_max + 1):
        is_odd_position = (column % 2 == 1)
        chars.append('*' if is_odd_position else ' ')
    print(''.join(chars))

# Demo
if __name__ == '__main__':
    print('Example 4: alternate stars (length 20)')
    print_alternate_stars(20)
    print()
```

**Extension:** Apply the same idea to a grid (e.g., checkerboard).

```python
def print_alternate_stars_grid(height_max: int, width_max: int) -> None:
    """Checkerboard-like grid with '*' at (row+column) odd positions."""
    for row in range(1, height_max + 1):
        chars = []
        for column in range(1, width_max + 1):
            if (row + column) % 2 == 1:
                chars.append('*')
            else:
                chars.append(' ')
        print(''.join(chars))

# Demo
if __name__ == '__main__':
    print('Example 4 (grid): alternate stars checkerboard 8x16')
    print_alternate_stars_grid(8, 16)
    print()
```

---

## 5) Example: Print stars **only at the edges** (hollow rectangle)

### Goal
Given `height_max` × `width_max`, print stars on the **border** only.

```python
def print_hollow_rectangle(height_max: int, width_max: int) -> None:
    """Print a hollow rectangle: stars on the border, spaces inside."""
    for row in range(1, height_max + 1):
        chars = []
        for column in range(1, width_max + 1):
            is_border = (row == 1 or row == height_max or column == 1 or column == width_max)
            chars.append('*' if is_border else ' ')
        print(''.join(chars))

# Demo
if __name__ == '__main__':
    print('Example 5: hollow rectangle 6x12')
    print_hollow_rectangle(6, 12)
    print()
```

---

## 6) Example: Print **diagonals and edges**

### Goal
On an `N × N` grid, print both diagonals **and** the border.

- Main diagonal: `row == column`
- Anti-diagonal: `row + column == N + 1`

```python
def print_diagonals_and_edges(n: int) -> None:
    """On an n x n grid, print stars on both diagonals and all edges."""
    row_max = n
    column_max = n

    for row in range(1, row_max + 1):
        chars = []
        for column in range(1, column_max + 1):
            on_edge = (row == 1 or row == row_max or column == 1 or column == column_max)
            on_main_diag = (row == column)
            on_anti_diag = (row + column == n + 1)

            if on_edge or on_main_diag or on_anti_diag:
                chars.append('*')
            else:
                chars.append(' ')
        print(''.join(chars))

# Demo
if __name__ == '__main__':
    print('Example 6: diagonals and edges (n=9)')
    print_diagonals_and_edges(9)
    print()
```

---

## 7) Triangle Patterns

The building blocks are **spaces** and **stars** per row. Always derive counts from `row` and `row_max`.

### 7.1 Left-aligned triangle
Row `r` has exactly `r` stars.

```python
def print_left_aligned_triangle(row_max: int) -> None:
    """Left aligned triangle of height row_max."""
    for row in range(1, row_max + 1):
        star_count = row  # grows with the row
        line = ''.join('*' for column in range(1, star_count + 1))
        print(line)

# Demo
if __name__ == '__main__':
    print('Example 7.1: left-aligned triangle (row_max=5)')
    print_left_aligned_triangle(5)
    print()
```

### 7.2 Right-aligned triangle
Spaces first, then stars.  
- `space_count = row_max - row`
- `star_count = row`

```python
def print_right_aligned_triangle(row_max: int) -> None:
    """Right aligned triangle of height row_max."""
    for row in range(1, row_max + 1):
        space_count = row_max - row
        star_count = row
        line = ''.join(' ' for _ in range(1, space_count + 1)) +                ''.join('*' for _ in range(1, star_count + 1))
        print(line)

# Demo
if __name__ == '__main__':
    print('Example 7.2: right-aligned triangle (row_max=5)')
    print_right_aligned_triangle(5)
    print()
```

### 7.3 Centered pyramid
- `left_spaces = row_max - row`
- `stars = 2 * row - 1`

```python
def print_centered_pyramid(row_max: int) -> None:
    """Centered pyramid of height row_max."""
    for row in range(1, row_max + 1):
        left_spaces = row_max - row
        star_count = 2 * row - 1
        line = ''.join(' ' for _ in range(1, left_spaces + 1)) +                ''.join('*' for _ in range(1, star_count + 1))
        print(line)

# Demo
if __name__ == '__main__':
    print('Example 7.3: centered pyramid (row_max=5)')
    print_centered_pyramid(5)
    print()
```

### 7.4 Inverted centered pyramid
- `left_spaces = row - 1`
- `stars = 2 * (row_max - row) + 1`

```python
def print_inverted_centered_pyramid(row_max: int) -> None:
    """Inverted centered pyramid of height row_max."""
    for row in range(1, row_max + 1):
        left_spaces = row - 1
        star_count = 2 * (row_max - row) + 1
        line = ''.join(' ' for _ in range(1, left_spaces + 1)) +                ''.join('*' for _ in range(1, star_count + 1))
        print(line)

# Demo
if __name__ == '__main__':
    print('Example 7.4: inverted centered pyramid (row_max=5)')
    print_inverted_centered_pyramid(5)
    print()
```

---



## 10) Bonus Variations To Practice

- **Hollow pyramid** (stars only at left edge, right edge, and base).  
- **Diamond** (pyramid up + inverted pyramid down, avoid duplicating the middle row).  
- **Checkerboard** with tunable cell size.  
- **Numbers instead of stars** (e.g., print `row` or `column` values).

---

## 11) Quick Mastery Checklist

- [ ] I can convert a visual pattern into **row/column counts**.  
- [ ] I can write **two-nested loops** for grids and **three-nested loops** for layers.  
- [ ] I can debug **off-by-one** issues quickly.  
- [ ] I can derive **space/star** formulas for triangles and pyramids.  
- [ ] I can handle **array-driven** problems (counts per row).

---

## 12) Mini Runner (Optional)

```python
def _run_all_demos() -> None:
    print('--- Demo Suite ---')
    print_hundred_stars_single_line()
    print_stars_grid_10x10()

    print_one_star_per_line_from_counts([3, 1, 4])
    print_stars_per_count_on_one_line([3, 1, 4, 0, 2])

    print_alternate_stars(20)
    print_alternate_stars_grid(8, 16)

    print_hollow_rectangle(6, 12)
    print_diagonals_and_edges(9)

    print_left_aligned_triangle(5)
    print_right_aligned_triangle(5)
    print_centered_pyramid(5)
    print_inverted_centered_pyramid(5)

if __name__ == '__main__':
    _run_all_demos()
```

---

### Final Tip
Think **grid-first**: *What goes at (row, column)?* Once counts are right, code follows naturally.
