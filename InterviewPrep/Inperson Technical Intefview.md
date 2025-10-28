# 🧑‍💻 In-person Technical Interview Roleplay: “Two Sum” — Full Walkthrough

> **Problem (as stated by interviewer in two lines):**
> “Given an array of integers and a target sum, return the **indices** of the two numbers that add up to the target.
> Assume exactly one solution exists in valid cases.”

---

## 🎭 Interview Dialogue (Interviewer ↔ Candidate)

**Interviewer:** You’re given an array of integers and a target sum. Return the indices of two numbers that add up to the target.

**Candidate:** Thanks! I have a few clarifying questions:

1. Can the array contain negative numbers and zeros?
2. Are indices 0-based?
3. Can the same element be used twice?
4. What if no such pair exists—should I return a sentinel like `[-1, -1]` or throw an error?
5. If multiple answers are possible, which one should I return?
6. What’s the expected time/space complexity? Any constraints on input size or integer ranges?

**Interviewer:**

1. Yes, negatives and zeros are allowed.
2. Indices are 0-based.
3. You cannot reuse the same element instance; indices must be different.
4. If no pair exists, throw an exception.
5. Any valid pair is fine, but be deterministic.
6. Aim for an optimal solution; the array can be large.

**Candidate (repeating to confirm):**
So, I need to implement a function: given `int[] nums` and `int target`, find two **distinct** indices `i` and `j` such that `nums[i] + nums[j] == target`. Indices are 0-based, negatives allowed. If no pair exists, I should throw an exception. If multiple pairs exist, I’ll return the first found by a left-to-right deterministic pass.

**Candidate (gives quick examples):**

* Input: `nums = [2, 7, 11, 15], target = 9` → Output: `[0, 1]` (since `2 + 7 = 9`)
* Input: `nums = [3, 2, 4], target = 6` → Output: `[1, 2]`
* Input: `nums = [3, 3], target = 6` → Output: `[0, 1]`
* Input: `nums = [-1, 10, 4, 6], target = 5` → Output: `[0, 3]` (since `-1 + 6 = 5`)

---

## 🧠 Think-Aloud: Approaches & Trade-offs

### 1) Brute Force (All pairs)

* **Idea:** Check every pair `(i, j)` with `i < j`.
* **Time:** `O(n^2)`
* **Space:** `O(1)`
* **Pros:** Simple, preserves original indices naturally.
* **Cons:** Too slow for large inputs.

### 2) Sort + Search (Binary Search / Two Pointers)

* **Idea A (Binary Search):** For each `i`, binary search for `target - nums[i]` in a **sorted** copy.
* **Idea B (Two Pointers):** Sort pairs `(value, originalIndex)` and then use two pointers from both ends.
* **Time:** Sorting `O(n log n)` + search `O(n)` → overall `O(n log n)`
* **Space:** `O(n)` to retain original indices (store `(value, index)` tuples).
* **Pros:** Faster than brute force.
* **Cons:** Sorting changes order; must carry original indices. Slightly more complex.
* **Note:** Two pointers is cleaner than per-element binary search here.

### 3) Hashing (Set/Map)

* **Set:** Can check presence in `O(1)` average, **but loses indices**. You’d need to store more info.
* **Map (Dictionary):** Store `value → index`. While scanning, for each `value`, compute `complement = target - value`; if complement exists in map, you have both indices.
* **Time:** `O(n)` average
* **Space:** `O(n)`
* **Pros:** Optimal time; preserves indices via the map.
* **Cons:** Extra memory; careful with duplicates.

**Candidate (conclusion):**
Given constraints and the need for **indices**, the **hash map** approach is best. I’ll do a single left-to-right pass, keeping the **first index** of each number in a `Map<Integer, Integer>`. For each `nums[i]`, I’ll compute `complement = target - nums[i]` and check if it’s already in the map. If yes, return `[map.get(complement), i]`. This is deterministic and `O(n)` average time.

---

## 📝 Pseudocode (Hash Map)

```
function twoSum(nums, target):
    if nums == null or length < 2: throw IllegalArgumentException

    map = new HashMap<value, index>()

    for i from 0 to n-1:
        complement = target - nums[i]
        if map.containsKey(complement):
            return [map.get(complement), i]
        if !map.containsKey(nums[i]):   // keep first occurrence to stay deterministic
            map.put(nums[i], i)

    throw IllegalArgumentException("No two sum solution")
```

---

## 💡 Edge Cases to Handle

* `nums == null` or `nums.length < 2` → invalid input.
* Large arrays (performance).
* Negative numbers and zeros.
* Duplicates (e.g., `[3,3]` with target `6`).
* Potential integer overflow in `target - nums[i]` (rare but guardable).
* No solution → throw exception (as required).

---

## ✍️ Java (Production-Quality) Implementation

```java
import java.util.*;

/**
 * Utility class providing a deterministic Two Sum solver.
 */
public final class TwoSumSolver {

    private TwoSumSolver() {
        // Prevent instantiation
    }

    /**
     * Finds indices of two distinct elements in the array that sum to the target.
     *
     * <p>Behavior & Contracts:
     * <ul>
     *   <li>Indices are 0-based and distinct (i != j).</li>
     *   <li>If multiple valid pairs exist, returns the first pair discovered via a left-to-right scan,
     *       i.e., the smallest j encountered; deterministic across runs.</li>
     *   <li>On invalid input (null or length < 2), throws IllegalArgumentException.</li>
     *   <li>If no solution exists, throws NoSuchElementException.</li>
     * </ul>
     *
     * @param nums   input array (not null; length >= 2)
     * @param target desired sum
     * @return an int[2] containing the indices [i, j] with nums[i] + nums[j] == target
     * @throws IllegalArgumentException if nums is null or length < 2
     * @throws NoSuchElementException   if no valid pair exists
     */
    public static int[] twoSum(final int[] nums, final int target) {
        validateInput(nums);

        // Map: value -> first index where it appears
        final Map<Integer, Integer> firstIndexByValue = new HashMap<>(Math.max(16, nums.length));

        for (int j = 0; j < nums.length; j++) {
            final int value = nums[j];

            // Use long to safely compute complement and avoid silent int overflow wrap-around
            final long complementLong = (long) target - (long) value;
            if (complementLong >= Integer.MIN_VALUE && complementLong <= Integer.MAX_VALUE) {
                final int complement = (int) complementLong;
                final Integer i = firstIndexByValue.get(complement);
                if (i != null && i != j) {
                    return new int[]{i, j};
                }
            }

            // Only store the first index for determinism
            firstIndexByValue.putIfAbsent(value, j);
        }

        throw new NoSuchElementException("No two sum solution for the provided input.");
    }

    /**
     * Optional-returning variant. Returns Optional.empty() when no pair exists.
     */
    public static Optional<int[]> tryTwoSum(final int[] nums, final int target) {
        try {
            return Optional.of(twoSum(nums, target));
        } catch (IllegalArgumentException | NoSuchElementException ex) {
            return Optional.empty();
        }
    }

    private static void validateInput(final int[] nums) {
        if (nums == null) {
            throw new IllegalArgumentException("Input array must not be null.");
        }
        if (nums.length < 2) {
            throw new IllegalArgumentException("Input array must have at least two elements.");
        }
    }

    // --- Demonstration main (not required in production code) ---
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]"); // [0, 1]
    }
}
```

### Complexity

* **Time:** `O(n)` average (hash lookups).
* **Space:** `O(n)` for the map.

---

## 🔍 “Why Not a Set?”

* A **Set** can tell you whether a complement exists, but it **doesn’t store indices**.
* You’d have to store **value → index** pairs somehow (essentially reinventing a map) or keep duplicate structures.
* A **Map** gives you direct access to the index in `O(1)` average, which is exactly what we need.

---

## 📊 Approach Comparison (TL;DR)

| Approach               | Time       | Space | Keeps Indices Easily | Notes                                         |
| ---------------------- | ---------- | ----- | -------------------- | --------------------------------------------- |
| Brute Force            | O(n²)      | O(1)  | ✅                    | Simple but slow                               |
| Sort + Two Pointers    | O(n log n) | O(n)  | ✅ (with tuple copy)  | Requires storing original indices before sort |
| Hash Map (Recommended) | O(n) avg   | O(n)  | ✅                    | Optimal time, straightforward                 |

---

## 🧪 Sample Walkthrough (Think-Aloud on Input)

**Input:** `nums = [3, 2, 4]`, `target = 6`
**Goal:** Find two indices `i, j` with `nums[i] + nums[j] == 6`.

**Candidate’s narration:**

1. Initialize empty map `firstIndexByValue = {}`.
2. `j = 0`, `value = 3`, `complement = 6 - 3 = 3`.

   * Map doesn’t have 3 yet → store `{3: 0}`.
3. `j = 1`, `value = 2`, `complement = 4`.

   * Map doesn’t have 4 → store `{3: 0, 2: 1}`.
4. `j = 2`, `value = 4`, `complement = 2`.

   * Map **has** 2 at index 1 → return `[1, 2]`.

**Output:** `[1, 2]` ✅

---

## ❓ Typical Follow-ups from Interviewer

1. **What if there are multiple valid pairs?**

   * Current implementation returns the first pair found in a left-to-right scan—deterministic. If lexicographically smallest pair is required, constraints must be specified; we could adapt the scan or use a different strategy.

2. **Can you return all pairs?**

   * Yes; we’d need to track multiple indices per value (e.g., `Map<Integer, List<Integer>>`) and collect all non-duplicate pairs.

3. **What about integer overflow?**

   * We compute `complement` in `long` to avoid silent wrap-around when `target - value` exceeds `int` range. We guard before casting back.

4. **Space optimization?**

   * Sorting + two pointers uses `O(n)` space (for storing `(value, index)`), similar to map. True `O(1)` extra space generally forces `O(n^2)` time for this problem.

5. **Streaming input?**

   * The hash map approach naturally works in a streaming fashion; you can process values as they arrive.

---

## ✅ Takeaways for Students (Driving the Conversation)

* **Start with clarifications.** Nail down indices, duplicates, invalid cases, and what to do if no solution exists.
* **Echo the problem back.** Shows active listening and ensures alignment.
* **Offer examples.** Tiny I/O checks anchor the problem.
* **Think out loud.** Present brute force → improved (`O(n log n)`) → optimal (`O(n)`) and articulate **why**.
* **State trade-offs.** Time vs space, determinism, and implementation complexity.
* **Code cleanly.** Use validation, clear names, comments/Javadoc, and deterministic behavior.
* **Explain complexity.** Close with `O(n)` time and `O(n)` space reasoning.

---

## 📚 Appendix: Brute Force Reference (for contrast)

```java
public static int[] twoSumBruteForce(int[] nums, int target) {
    if (nums == null || nums.length < 2) {
        throw new IllegalArgumentException("Input array must have at least two elements.");
    }
    for (int i = 0; i < nums.length - 1; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return new int[]{i, j};
            }
        }
    }
    throw new java.util.NoSuchElementException("No two sum solution.");
}
```

---

### ✍️ Authored by

**Mahesh Arali**  
_Former Principal Engineering Manager, Microsoft_  
_Founder & CEO, algorithms365_


**End of Notes.**
