# 25 Industry-Standard Array Interview Questions

This document contains **25 classic and advanced array problems** commonly asked in technical interviews (product and service companies).  
Each section includes:  
- Problem statement  
- Function declaration (Python & Java)  
- Input assumptions  
- Examples (2 positive + 1 invalid/negative)  
- Solution hints (possible approaches, complexity)  

---

## 1) Two Sum (Return Indices)

**Task**: Return indices of two numbers whose sum equals `target`.  
If no solution, return empty.

**Python**  
```python
from typing import List
def two_sum_indices(nums: List[int], target: int) -> List[int]: ...
```

**Java**  
```java
public static int[] twoSumIndices(int[] nums, int target) { ... }
```

**Examples**  
- Input: nums=[2,7,11,15], target=9 → [0,1]  
- Input: nums=[3,2,4], target=6 → [1,2]  
- Invalid: nums=None → ValueError/IllegalArgumentException

**Hints**: Hash map O(n), two pointers after sorting O(n log n).

---

## 2) Best Time to Buy and Sell Stock (Single Transaction)

**Task**: Maximize profit with one buy & one sell.

**Python**  
```python
from typing import List
def max_profit_single_trade(prices: List[int]) -> int: ...
```

**Java**  
```java
public static int maxProfitSingleTrade(int[] prices) { ... }
```

**Examples**  
- [7,1,5,3,6,4] → 5  
- [7,6,4,3,1] → 0  
- Invalid: len<2 → ValueError/IllegalArgumentException

**Hints**: Track min price; update profit. O(n).

---

## 3) Contains Duplicate

**Python**  
```python
from typing import List
def contains_duplicate(nums: List[int]) -> bool: ...
```

**Java**  
```java
public static boolean containsDuplicate(int[] nums) { ... }
```

**Examples**  
- [1,2,3,1] → True  
- [1,2,3,4] → False  
- Invalid: nums=None → Error

**Hints**: Hash set or sort.  

---

## 4) Product of Array Except Self

**Python**  
```python
from typing import List
def product_except_self(nums: List[int]) -> List[int]: ...
```

**Java**  
```java
public static int[] productExceptSelf(int[] nums) { ... }
```

**Examples**  
- [1,2,3,4] → [24,12,8,6]  
- [-1,1,0,-3,3] → [0,0,9,0,0]  
- Invalid: nums=None → Error

**Hints**: Prefix/suffix products.  

---

## 5) Maximum Subarray (Kadane)

**Python**  
```python
from typing import List
def max_subarray_sum(nums: List[int]) -> int: ...
```

**Java**  
```java
public static int maxSubarraySum(int[] nums) { ... }
```

**Examples**  
- [-2,1,-3,4,-1,2,1,-5,4] → 6  
- [1] → 1  
- Invalid: empty → Error

**Hints**: Kadane’s algorithm.  

---

## 6) Merge Intervals

**Python**  
```python
from typing import List, Tuple
def merge_intervals(intervals: List[Tuple[int,int]]) -> List[Tuple[int,int]]: ...
```

**Java**  
```java
public static int[][] mergeIntervals(int[][] intervals) { ... }
```

**Examples**  
- [[1,3],[2,6],[8,10]] → [[1,6],[8,10]]  
- [[1,4],[4,5]] → [[1,5]]  
- Invalid: start>end → Error

**Hints**: Sort + merge.  

---

## 7) Rotate Array (Right by k)

**Python**  
```python
from typing import List
def rotate_right(nums: List[int], k: int) -> List[int]: ...
```

**Java**  
```java
public static void rotateRight(int[] nums, int k) { ... }
```

**Examples**  
- [1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]  
- [-1], k=2 → [-1]  
- Invalid: nums=None → Error

**Hints**: Reverse method.  

---

## 8) Move Zeroes

**Python**  
```python
from typing import List
def move_zeroes_to_end(nums: List[int]) -> List[int]: ...
```

**Java**  
```java
public static void moveZeroesToEnd(int[] nums) { ... }
```

**Examples**  
- [0,1,0,3,12] → [1,3,12,0,0]  
- [0] → [0]  
- Invalid: None → Error

**Hints**: Two pointers.  

---

## 9) Missing Number (0..n)

**Python**  
```python
from typing import List
def find_missing_number(nums: List[int]) -> int: ...
```

**Java**  
```java
public static int findMissingNumber(int[] nums) { ... }
```

**Examples**  
- [3,0,1] → 2  
- [0,1] → 2  
- Invalid: duplicates → Error

**Hints**: XOR or sum formula.  

---

## 10) Find Duplicate Number

**Python**  
```python
from typing import List
def find_duplicate_number(nums: List[int]) -> int: ...
```

**Java**  
```java
public static int findDuplicateNumber(int[] nums) { ... }
```

**Examples**  
- [1,3,4,2,2] → 2  
- [3,1,3,4,2] → 3  
- Invalid: out-of-range → Error

**Hints**: Floyd’s cycle detection.  

---

## 11) Search in Rotated Sorted Array

**Python**  
```python
from typing import List
def search_rotated(nums: List[int], target: int) -> int: ...
```

**Java**  
```java
public static int searchRotated(int[] nums, int target) { ... }
```

**Examples**  
- [4,5,6,7,0,1,2], target=0 → 4  
- target=3 → -1  
- Invalid: nums=None → Error

**Hints**: Binary search.  

---

## 12) Remove Duplicates from Sorted Array

**Python**  
```python
from typing import List
def remove_duplicates_sorted(nums: List[int]) -> int: ...
```

**Java**  
```java
public static int removeDuplicatesSorted(int[] nums) { ... }
```

**Examples**  
- [1,1,2] → 2  
- [0,0,1,1,2,2,3] → 4  
- Invalid: None → Error

**Hints**: Two pointers.  

---

## 13) Longest Consecutive Sequence

**Python**  
```python
from typing import List
def longest_consecutive(nums: List[int]) -> int: ...
```

**Java**  
```java
public static int longestConsecutive(int[] nums) { ... }
```

**Examples**  
- [100,4,200,1,3,2] → 4  
- [] → 0  
- Invalid: None → Error

**Hints**: Hash set.  

---

## 14) Majority Element

**Python**  
```python
from typing import List
def majority_element(nums: List[int]) -> int: ...
```

**Java**  
```java
public static int majorityElement(int[] nums) { ... }
```

**Examples**  
- [3,2,3] → 3  
- [2,2,1,1,1,2,2] → 2  
- Invalid: no majority → Error

**Hints**: Boyer–Moore.  

---

## 15) 3Sum

**Python**  
```python
from typing import List
def three_sum_zero(nums: List[int]) -> List[List[int]]: ...
```

**Java**  
```java
public static List<List<Integer>> threeSumZero(int[] nums) { ... }
```

**Examples**  
- [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]  
- [0,1,1] → []  
- Invalid: None → Error

**Hints**: Sort + two pointers.  

---

## 16) Trapping Rain Water

**Python**  
```python
from typing import List
def trap_rain_water(heights: List[int]) -> int: ...
```

**Java**  
```java
public static int trapRainWater(int[] heights) { ... }
```

**Examples**  
- [0,1,0,2,1,0,1,3,2,1,2,1] → 6  
- [4,2,0,3,2,5] → 9  
- Invalid: None → Error

**Hints**: Two-pointer / stack.  

---

## 17) Sliding Window Maximum

**Python**  
```python
from typing import List
def sliding_window_max(nums: List[int], k: int) -> List[int]: ...
```

**Java**  
```java
public static int[] slidingWindowMax(int[] nums, int k) { ... }
```

**Examples**  
- [1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]  
- [1], k=1 → [1]  
- Invalid: k<=0 → Error

**Hints**: Deque or heap.  

---

## 18) Subarray Sum Equals K

**Python**  
```python
from typing import List
def count_subarrays_sum_k(nums: List[int], k: int) -> int: ...
```

**Java**  
```java
public static int countSubarraysSumK(int[] nums, int k) { ... }
```

**Examples**  
- [1,1,1], k=2 → 2  
- [1,2,3], k=3 → 2  
- Invalid: None → Error

**Hints**: Prefix sums + map.  

---

## 19) Minimum Size Subarray Sum

**Python**  
```python
from typing import List
def min_length_subarray_at_least_target(nums: List[int], target: int) -> int: ...
```

**Java**  
```java
public static int minLengthSubarrayAtLeastTarget(int[] nums, int target) { ... }
```

**Examples**  
- target=7, nums=[2,3,1,2,4,3] → 2  
- target=4, nums=[1,4,4] → 1  
- Invalid: None → Error

**Hints**: Sliding window.  

---

## 20) Dutch National Flag (Sort Colors)

**Python**  
```python
from typing import List
def sort_colors_dnf(nums: List[int]) -> None: ...
```

**Java**  
```java
public static void sortColorsDNF(int[] nums) { ... }
```

**Examples**  
- [2,0,2,1,1,0] → [0,0,1,1,2,2]  
- [2,0,1] → [0,1,2]  
- Invalid: value>2 → Error

**Hints**: Three pointers.  

---

## 21) Merge Two Sorted Arrays

**Python**  
```python
from typing import List
def merge_sorted_into_first(nums1: List[int], m: int, nums2: List[int], n: int) -> None: ...
```

**Java**  
```java
public static void mergeSortedIntoFirst(int[] nums1, int m, int[] nums2, int n) { ... }
```

**Examples**  
- nums1=[1,2,3,0,0,0], nums2=[2,5,6] → [1,2,2,3,5,6]  
- nums1=[0], m=0, nums2=[1] → [1]  
- Invalid: sizes mismatch → Error

**Hints**: Three pointers backward.  

---

## 22) Intersect Two Arrays II

**Python**  
```python
from typing import List
def intersect_arrays(nums1: List[int], nums2: List[int]) -> List[int]: ...
```

**Java**  
```java
public static int[] intersectArrays(int[] nums1, int[] nums2) { ... }
```

**Examples**  
- [1,2,2,1], [2,2] → [2,2]  
- [4,9,5], [9,4,9,8,4] → [4,9]  
- Invalid: None → Error

**Hints**: Hash map counts / two pointers.  

---

## 23) Minimum in Rotated Sorted Array

**Python**  
```python
from typing import List
def find_min_in_rotated(nums: List[int]) -> int: ...
```

**Java**  
```java
public static int findMinInRotated(int[] nums) { ... }
```

**Examples**  
- [3,4,5,1,2] → 1  
- [4,5,6,7,0,1,2] → 0  
- Invalid: empty → Error

**Hints**: Binary search.  

---

## 24) Median of Two Sorted Arrays

**Python**  
```python
from typing import List
def median_two_sorted(nums1: List[int], nums2: List[int]) -> float: ...
```

**Java**  
```java
public static double medianTwoSorted(int[] nums1, int[] nums2) { ... }
```

**Examples**  
- [1,3],[2] → 2.0  
- [1,2],[3,4] → 2.5  
- Invalid: both empty → Error

**Hints**: Binary partition or merge.  

---

## 25) Range Sum Query – Immutable

**Python**  
```python
from typing import List
class NumArray:
    def __init__(self, nums: List[int]): ...
    def sum_range(self, left: int, right: int) -> int: ...
```

**Java**  
```java
public static class NumArray {
    public NumArray(int[] nums) { ... }
    public int sumRange(int left, int right) { ... }
}
```

**Examples**  
- nums=[-2,0,3,-5,2,-1], sumRange(0,2)=1  
- sumRange(2,5)=-1  
- Invalid: left>right → Error

**Hints**: Prefix sum array.  

---

# Tips for Algorithms365 Students

- Always clarify **constraints** (array size, element range).  
- Check for **corner cases**: empty array, single element, all negatives, all duplicates.  
- Discuss at least 2 approaches in interviews (brute force vs optimized).  
- Prioritize readability: good variable names, comments, edge case handling.  

---
