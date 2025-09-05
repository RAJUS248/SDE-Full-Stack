# 10 Industry-Standard 2D Array / Matrix Interview Questions

These are **commonly asked 2D matrix problems** in product companies, startups, and service companies.  
Each problem includes: function declarations (Python & Java), assumptions, examples, and solution hints.

---

## 1) Search in a 2D Matrix

**Task**: Given an `m × n` matrix sorted row-wise with each row’s first element greater than the previous row’s last element, search for a `target`.

**Python**
```python
from typing import List
def search_matrix(matrix: List[List[int]], target: int) -> bool: ...
```

**Java**
```java
public static boolean searchMatrix(int[][] matrix, int target) { ... }
```

**Examples**  
- [[1,3,5],[7,9,11]], target=9 → True  
- [[1,3,5],[7,9,11]], target=8 → False  
- Invalid: matrix=None → Error

**Hints**: Flatten to 1D → binary search.

---

## 2) Rotate Image 90°

**Task**: Rotate an `n × n` matrix 90° clockwise in place.

**Python**
```python
from typing import List
def rotate_image_clockwise(matrix: List[List[int]]) -> None: ...
```

**Java**
```java
public static void rotateImageClockwise(int[][] matrix) { ... }
```

**Examples**  
- [[1,2,3],[4,5,6],[7,8,9]] → [[7,4,1],[8,5,2],[9,6,3]]  
- [[1]] → [[1]]  
- Invalid: non-square matrix → Error

**Hints**: Transpose + reverse rows.

---

## 3) Spiral Order Traversal

**Task**: Return all elements in spiral order.

**Python**
```python
from typing import List
def spiral_order(matrix: List[List[int]]) -> List[int]: ...
```

**Java**
```java
public static List<Integer> spiralOrder(int[][] matrix) { ... }
```

**Examples**  
- [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]  
- [[1,2,3,4]] → [1,2,3,4]  
- Invalid: empty matrix → Error

**Hints**: Maintain boundaries top, bottom, left, right.

---

## 4) Word Search

**Task**: Check if word exists in a grid of letters. Adjacent = up, down, left, right.

**Python**
```python
from typing import List
def word_search(board: List[List[str]], word: str) -> bool: ...
```

**Java**
```java
public static boolean wordSearch(char[][] board, String word) { ... }
```

**Examples**  
- [["A","B","C"],["D","E","F"]], "BE" → True  
- "ABF" → False  
- Invalid: board empty → Error

**Hints**: DFS/backtracking with visited set.

---

## 5) Set Matrix Zeroes

**Task**: If any element is 0, set row and column to 0.

**Python**
```python
from typing import List
def set_matrix_zeroes(matrix: List[List[int]]) -> None: ...
```

**Java**
```java
public static void setMatrixZeroes(int[][] matrix) { ... }
```

**Examples**  
- [[1,1,1],[1,0,1],[1,1,1]] → [[1,0,1],[0,0,0],[1,0,1]]  
- [[0,1]] → [[0,0]]  
- Invalid: matrix=None → Error

**Hints**: Use first row/col as markers.

---

## 6) Search in Sorted 2D Matrix II

**Task**: Each row and column sorted ascending. Search for target.

**Python**
```python
from typing import List
def search_sorted_matrix(matrix: List[List[int]], target: int) -> bool: ...
```

**Java**
```java
public static boolean searchSortedMatrix(int[][] matrix, int target) { ... }
```

**Examples**  
- [[1,4,7],[2,5,8],[3,6,9]], target=6 → True  
- target=10 → False  
- Invalid: matrix=None → Error

**Hints**: Start at top-right; eliminate row/col.

---

## 7) Island Count

**Task**: Count islands (1=land, 0=water).

**Python**
```python
from typing import List
def count_islands(grid: List[List[str]]) -> int: ...
```

**Java**
```java
public static int countIslands(char[][] grid) { ... }
```

**Examples**  
- [["1","1","0"],["0","1","0"],["0","0","1"]] → 2  
- [["0","0"],["0","0"]] → 0  
- Invalid: empty → Error

**Hints**: DFS/BFS flood fill.

---

## 8) Maximal Square

**Task**: Find area of largest square of 1s.

**Python**
```python
from typing import List
def maximal_square(matrix: List[List[str]]) -> int: ...
```

**Java**
```java
public static int maximalSquare(char[][] matrix) { ... }
```

**Examples**  
- [["1","0","1","0"],["1","0","1","1"],["1","1","1","1"]] → 4  
- [["0","1"],["1","0"]] → 1  
- Invalid: None → Error

**Hints**: DP with min(top, left, diag)+1.

---

## 9) Sudoku Validator

**Task**: Validate 9×9 Sudoku board.

**Python**
```python
from typing import List
def is_valid_sudoku(board: List[List[str]]) -> bool: ...
```

**Java**
```java
public static boolean isValidSudoku(char[][] board) { ... }
```

**Examples**  
- Valid board → True  
- Row with duplicate → False  
- Invalid: size≠9×9 → Error

**Hints**: Check row, col, 3×3 boxes.

---

## 10) Minimum Path Sum

**Task**: Find path from top-left to bottom-right with minimal sum.

**Python**
```python
from typing import List
def min_path_sum(grid: List[List[int]]) -> int: ...
```

**Java**
```java
public static int minPathSum(int[][] grid) { ... }
```

**Examples**  
- [[1,3,1],[1,5,1],[4,2,1]] → 7  
- [[1,2,3],[4,5,6]] → 12  
- Invalid: None → Error

**Hints**: DP: dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]).

---

# Mastery Tips
- Visualize rows/columns before coding.  
- Handle small/edge cases.  
- Practice DFS, BFS, and DP templates.  
- Think about space optimization (in-place).  
