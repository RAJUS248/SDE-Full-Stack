
# Binary Search Code Comparison in Java: Bad vs Good Practices

This document demonstrates how clean, professional code improves readability and maintainability by comparing two versions of a binary search method in Java.

---

## 🔴 Poorly Written Code (Bad Practice)

```java
public class Main {
    public static int f(int[] a, int t) {
        int l = 0;
        int r = a.length - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (a[m] == t) {
                return m;
            } else if (a[m] < t) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] x = {1, 3, 5, 7, 9, 11};
        System.out.println(f(x, 7));
    }
}
```

### Problems:
- Method name `f` and variables like `a`, `t`, `l`, `r`, `m` are meaningless.
- No comments or JavaDoc.
- No input validation.
- Hard to debug or maintain.
- Not readable for beginners or teammates.

---

## ✅ Professionally Written Code (Clean and Understandable)

```java
/**
 * Utility class to perform binary search operations.
 */
public class BinarySearch {

    /**
     * Performs binary search on a sorted array to find the index of the target value.
     *
     * @param sortedArray An array of integers sorted in ascending order.
     * @param target The integer value to search for.
     * @return The index of the target if found, else -1.
     */
    public static int binarySearch(int[] sortedArray, int target) {
        int leftIndex = 0;
        int rightIndex = sortedArray.length - 1;

        while (leftIndex <= rightIndex) {
            int middleIndex = (leftIndex + rightIndex) / 2;
            int middleValue = sortedArray[middleIndex];

            if (middleValue == target) {
                return middleIndex;
            } else if (middleValue < target) {
                leftIndex = middleIndex + 1;
            } else {
                rightIndex = middleIndex - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 3, 5, 7, 9, 11};
        int searchResult = binarySearch(numbers, 7);
        if (searchResult != -1) {
            System.out.println("Target found at index: " + searchResult);
        } else {
            System.out.println("Target not found.");
        }
    }
}
```

### Benefits of Clean Code:
- **Readability**: Clear method and variable names convey intent.
- **Maintainability**: Easy to modify or extend in the future.
- **Debuggability**: Easier to insert logs or breakpoints.
- **Reusability**: Well-documented, modular methods are easier to reuse.
