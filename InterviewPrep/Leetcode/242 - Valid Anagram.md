# ✅ Valid Anagram — Interviewer/Interviewee Walkthrough (Multi-Solution Master Notes)

## 1) Title Section

**Valid Anagram (LeetCode 242)**
**Problem.** Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
**Typical constraints.**

* `1 ≤ len(s), len(t) ≤ 5 * 10^4` (varies by platform)
* Characters may be lowercase English letters in the basic version; some follow-ups allow arbitrary Unicode.

**Examples**

* `s = "anagram", t = "nagaram" → true`
* `s = "rat", t = "car" → false`

---

## 2) 👥 Roleplay: Interviewer ↔ Candidate

**Candidate → Interviewer (clarifying):**

1. *Are the inputs limited to lowercase English letters (`a`–`z`)?*
   **Interviewer:** Base problem: yes. Follow-up: may include Unicode.
2. *Do I need to ignore spaces, punctuation, or case?*
   **Interviewer:** No. Compare strings exactly as given.
3. *Should I consider very long inputs (e.g., 50k+) and optimize time/space?*
   **Interviewer:** Yes, aim for near-linear time.
4. *Is memory usage a concern (constant vs. linear)?*
   **Interviewer:** Prefer O(1) extra space for the lowercase-only version if possible.

**Candidate (thinking aloud):**

* First, if lengths differ, answer is `false`.
* For lowercase-only, I can use a fixed array of size 26 to count frequency differences in O(n) time, O(1) space.
* Generic/Unicode case needs a dictionary/hash map.
* Sorting both strings is O(n log n), simple and acceptable but not optimal.
* I’ll compare multiple approaches (sort, freq arrays/maps, one-pass differential). I’ll also call out a couple of wrong ideas (like XOR/bitset).

---

## 3) 🏷️ Important Keywords & Why They Matter

* **Frequency counting / Hash map lookups:** Core idea—anagrams have identical character multiplicities.
* **Fixed-size array (26 bucket counts):** O(1) extra space when alphabet is small and known.
* **Sorting comparison:** Simple baseline; turns problem into equality of sorted representations.
* **Early length check:** Constant-time pruning when `len(s) != len(t)`.
* **Unicode-aware map:** Necessary when alphabet is unbounded.
* **One-pass differential counting:** Count up for `s`, down for `t` to stay O(n) with minimal passes.

---

## 4) 🧠 Human (Mechanical) Approach → Brute Force

**Human way:**
Write letters of `s`, then “cross them out” using letters from `t`. If every letter in `t` finds a matching unused letter in `s` and no leftovers remain, it’s an anagram.

**Brute force logic (impractical):**
Generate all permutations of `s` and check if any equals `t`.

* **Time:** O(n!) — infeasible beyond tiny inputs.

**Pseudocode (brute force, conceptual):**

```
if len(s) != len(t): return false
for each permutation p of s:
    if p == t: return true
return false
```

We only keep this to anchor understanding; we won’t implement O(n!) in code.

---

## 5) 🪓 Brute Force Implementations (Usable Baseline: Sorting)

**Idea:** Sort both strings and compare equality.
**Time:** O(n log n)
**Space:** O(1) to O(n) depending on language sort implementation.

### Python (function-only, simple & clean)

```python
from typing import List

def is_anagram_sorting(s: str, t: str) -> bool:
    # Early length check to avoid unnecessary work
    if len(s) != len(t):
        return False
    # Sorting both and comparing
    return sorted(s) == sorted(t)
```

### Java (function-only, clean)

```java
import java.util.Arrays;

public static boolean isAnagramSorting(final String s, final String t) {
    if (s.length() != t.length()) return false;
    final char[] a = s.toCharArray();
    final char[] b = t.toCharArray();
    Arrays.sort(a);
    Arrays.sort(b);
    return Arrays.equals(a, b);
}
```

---

## 6) 🧭 Mapping Brute Force → CS Concepts

* **Brute force permutations:** exhaustive search; guarantees correctness but is combinatorial explosion.
* **Sorting baseline:** reduces to comparing canonical forms; widely applicable, simple to write.
* **Signals to optimize:** n can be large; O(n log n) sorting is costlier than O(n) counting with small fixed alphabet.

---

## 7) ⚙️ Optimizations (5–8+ distinct approaches)

> Below, each approach includes idea, when it works, pseudocode, code (Python & Java), complexity, and DS choice.

### A) Fixed-Size Array (26 Counts) — **O(n) time, O(1) space**

**Core Idea:** For lowercase English only, maintain an int[26]; increment for `s[i]`, decrement for `t[i]`. All zeros ⇒ anagram.
**Better than sorting:** Linear time, constant extra space.
**When it works:** Only when alphabet is known and small (e.g., lowercase `'a'..'z'`).
**Pseudocode:**

```
if len(s) != len(t): return false
cnt[26] = {0}
for i in [0..len(s)-1]:
    cnt[s[i]-'a'] += 1
    cnt[t[i]-'a'] -= 1
for x in cnt:
    if x != 0: return false
return true
```

**Python**

```python
from typing import List

def is_anagram_counts_26(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26
    base = ord('a')
    for cs, ct in zip(s, t):
        counts[ord(cs) - base] += 1
        counts[ord(ct) - base] -= 1
    return all(v == 0 for v in counts)
```

**Java**

```java
public static boolean isAnagramCounts26(final String s, final String t) {
    if (s.length() != t.length()) return false;
    final int[] cnt = new int[26];
    for (int i = 0; i < s.length(); i++) {
        cnt[s.charAt(i) - 'a']++;
        cnt[t.charAt(i) - 'a']--;
    }
    for (int v : cnt) if (v != 0) return false;
    return true;
}
```

**Complexity:** Time O(n), Space O(1).
**DS rationale:** Fixed array is the most cache-friendly, constant-space frequency counter.

---

### B) Hash Map (Two Passes) — **O(n) time, O(k) space**

**Core Idea:** Build frequency map for `s`; subtract with `t`; verify all zeros or no negatives.
**Why better than sorting:** Linear time; supports variable alphabets (e.g., Unicode).
**When it works:** Always; required if characters aren’t limited to `'a'..'z'`.

**Pseudocode:**

```
if len(s) != len(t): return false
map = {}
for c in s: map[c] += 1
for c in t:
    if c not in map: return false
    map[c] -= 1
    if map[c] < 0: return false
return true
```

**Python**

```python
from typing import Dict

def is_anagram_map_two_pass(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq: Dict[str, int] = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in t:
        if c not in freq:
            return False
        freq[c] -= 1
        if freq[c] < 0:
            return False
    return True
```

**Java**

```java
import java.util.HashMap;
import java.util.Map;

public static boolean isAnagramMapTwoPass(final String s, final String t) {
    if (s.length() != t.length()) return false;
    final Map<Character, Integer> map = new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
        final char c = s.charAt(i);
        map.put(c, map.getOrDefault(c, 0) + 1);
    }
    for (int i = 0; i < t.length(); i++) {
        final char c = t.charAt(i);
        final Integer count = map.get(c);
        if (count == null || count == 0) return false;
        map.put(c, count - 1);
    }
    return true;
}
```

**Complexity:** Time O(n), Space O(k) where k = unique chars.
**DS rationale:** Hash map supports arbitrary alphabets with average O(1) updates.

---

### C) Hash Map (Single Pass Differential) — **O(n) time, O(k) space**

**Core Idea:** In one loop `i`, `+1` for `s[i]`, `-1` for `t[i]`. Validate zeros at end.
**Why better:** Fewer passes over memory; still O(n).
**When it works:** Any alphabet; `len(s) == len(t)` required.

**Pseudocode:**

```
if len(s) != len(t): return false
map = {}
for i in [0..n-1]:
    map[s[i]] += 1
    map[t[i]] -= 1
for v in map.values():
    if v != 0: return false
return true
```

**Python**

```python
from typing import Dict

def is_anagram_map_single_pass(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    diff: Dict[str, int] = {}
    for cs, ct in zip(s, t):
        diff[cs] = diff.get(cs, 0) + 1
        diff[ct] = diff.get(ct, 0) - 1
    return all(v == 0 for v in diff.values())
```

**Java**

```java
import java.util.HashMap;
import java.util.Map;

public static boolean isAnagramMapSinglePass(final String s, final String t) {
    if (s.length() != t.length()) return false;
    final Map<Character, Integer> diff = new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
        final char a = s.charAt(i), b = t.charAt(i);
        diff.put(a, diff.getOrDefault(a, 0) + 1);
        diff.put(b, diff.getOrDefault(b, 0) - 1);
    }
    for (int v : diff.values()) if (v != 0) return false;
    return true;
}
```

**Complexity:** Time O(n), Space O(k).
**DS rationale:** Same as B, but memory access patterns can be slightly friendlier.

---

### D) Python `collections.Counter` Equality — **O(n) time, O(k) space**

**Core Idea:** Build `Counter(s)` and `Counter(t)` and compare.
**Why better:** Concise, readable; leverages well-optimized C implementations.
**When it works:** Python only; any alphabet.

**Pseudocode:**

```
if len(s) != len(t): return false
return Counter(s) == Counter(t)
```

**Python**

```python
from typing import Counter as _Counter
from collections import Counter

def is_anagram_counter(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
```

**Complexity:** Time O(n), Space O(k).
**DS rationale:** High-level frequency map with clean semantics.

---

### E) Frequency Signature (Tuple) — **O(n) time, O(1)/O(k) space**

**Core Idea:** Build a canonical frequency “signature” and compare. For `'a'..'z'`, this is a 26-tuple; for Unicode, use sorted (char,count) pairs.
**Why better:** Clear canonical form; enables hashing if needed.
**When it works:** Known alphabet → fixed tuple; else requires sorting keys (adds `k log k`).

**Pseudocode (lowercase):**

```
if len(s) != len(t): return false
sig_s = 26-array counts(s)
sig_t = 26-array counts(t)
return sig_s == sig_t
```

**Python (lowercase)**

```python
def is_anagram_signature_26(s: str, t: str) -> bool:
    if len(s) != len(t): 
        return False
    freq_s = [0]*26
    freq_t = [0]*26
    base = ord('a')
    for c in s: freq_s[ord(c)-base] += 1
    for c in t: freq_t[ord(c)-base] += 1
    return tuple(freq_s) == tuple(freq_t)
```

**Complexity:** Time O(n), Space O(1) for fixed alphabet; O(k log k) if you must sort map items.
**DS rationale:** Tuples give an immutable, comparable “fingerprint”.

---

### F) Unicode-Aware Map with Early Exit — **O(n) average, O(k) space**

**Core Idea:** As we decrement counts for `t`, *immediately* return `false` if a count would drop below zero.
**Why better:** Fails fast on early mismatches.
**When it works:** General alphabets; especially useful when mismatch appears early.

**Python**

```python
def is_anagram_unicode_fastfail(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in t:
        cnt = freq.get(c, 0)
        if cnt == 0:
            return False
        freq[c] = cnt - 1
    return True
```

**Java**

```java
import java.util.HashMap;
import java.util.Map;

public static boolean isAnagramUnicodeFastFail(final String s, final String t) {
    if (s.length() != t.length()) return false;
    final Map<Integer, Integer> freq = new HashMap<>(); // code point safe if needed
    s.codePoints().forEach(cp -> freq.put(cp, freq.getOrDefault(cp, 0) + 1));
    final int[] ok = {1};
    t.codePoints().forEach(cp -> {
        if (ok[0] == 1) {
            final Integer c = freq.get(cp);
            if (c == null || c == 0) ok[0] = 0;
            else freq.put(cp, c - 1);
        }
    });
    return ok[0] == 1;
}
```

**Complexity:** O(n) average, O(k) space.
**DS rationale:** Hash map handles arbitrary Unicode via code points.

---

### G) Sorting + Two Pointers (Educational Variant) — **O(n log n) time**

**Core Idea:** Sort both, then walk with two pointers to confirm all chars match.
**Why:** Same as basic sort, but explicitly demonstrates pointer comparison.
**When it works:** Always; useful as a teaching tool.

**Pseudocode:**

```
sort a = chars(s)
sort b = chars(t)
i = j = 0
while i < n and j < n:
    if a[i] != b[j]: return false
    i++, j++
return true
```

**(Code is same as sorting baseline; the pointer walk is trivial after sort.)**

---

### H) Prime-Product Hash (Not Recommended in Practice) — **Theoretical Variant**

**Core Idea:** Map each letter to a unique prime and multiply to get a product “hash”. Equal products imply equal multisets.
**Why not recommended:** Overflow risk, collisions under modular arithmetic, tricky for Unicode/large counts. Shows creative hashing but brittle.

**Python (demo only)**

```python
def is_anagram_prime_hash_demo(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
    prod_s = 1
    prod_t = 1
    for c in s: prod_s *= primes[ord(c)-97]
    for c in t: prod_t *= primes[ord(c)-97]
    return prod_s == prod_t  # overflow risk; demonstration only
```

**Complexity:** O(n) multiplications; **unsafe** due to overflow.
**DS rationale:** Number theory trick; highlight why robust counters are preferred.

---

## 8) 🚫 Common Wrong/Naïve Algorithms

1. **XOR / Sum Equality**

* **Why it seems plausible:** If you XOR/sum all chars of `s` and `t`, identical totals might “prove” equality.
* **Counterexample:** `s="ab", t="ba"` → XOR totals equal, but that’s *fine* here; however `s="aac", t="bba"` → sums can accidentally match; XOR breaks with duplicates in many patterns.
* **Intuition of failure:** XOR/sum lose multiplicity structure—distinct multisets can collide.

2. **Bitset / Boolean Set Equality**

* **Why it seems plausible:** If the set of used letters matches, maybe they’re anagrams.
* **Counterexample:** `s="aab", t="ab"` have the same set `{a,b}` but not the same counts.
* **Intuition of failure:** Sets ignore frequency; anagrams need **counts**, not presence.

(Optionally, **Priority Queue/Heap**: building two heaps and popping to compare is just a slower sort; offers no benefit here.)

---

## 9) 🧪 Edge Case Checklist

* **Different lengths** → immediately `false`.
* **Single character** (e.g., `"a"` vs. `"a"`, `"a"` vs. `"b"`).
* **All identical characters** (`"aaaa"`, `"aaaa"`).
* **Duplicates with mismatch** (`"aabb"` vs. `"abbb"`).
* **Non-lowercase / Unicode** (emojis, accented letters) → use hash map / code points.
* **Very long strings** → prefer O(n) counting to avoid O(n log n) sort.
* **Empty strings** (if allowed) → both empty ⇒ `true`; one empty ⇒ `false`.
* **Locale/case sensitivity** → problem states exact match; don’t transform unless specified.

---

## 10) ⏱️ Complexity Summary

| Approach Name          | Core Idea                      |                 Time |     Space | Notes / When to Use                             |
| ---------------------- | ------------------------------ | -------------------: | --------: | ----------------------------------------------- |
| Sorting Baseline       | Sort both and compare          |           O(n log n) | O(1)–O(n) | Easiest to implement; acceptable for moderate n |
| Fixed 26 Counts        | int[26] differential           |             **O(n)** |  **O(1)** | Best for lowercase `'a'..'z'`                   |
| Hash Map (2-Pass)      | Build for `s`, subtract by `t` |             **O(n)** |      O(k) | Unicode/general alphabets                       |
| Hash Map (1-Pass)      | Simultaneous +1/-1             |             **O(n)** |      O(k) | Slightly tighter memory traversal               |
| Counter Equality (Py)  | `Counter(s) == Counter(t)`     |             **O(n)** |      O(k) | Cleanest Pythonic solution                      |
| Frequency Signature    | Tuple fingerprint              | O(n) or O(n+k log k) | O(1)/O(k) | Canonical hashable signature                    |
| Sorting + Two Pointers | Compare after sort             |           O(n log n) | O(1)–O(n) | Educational variant of sorting                  |
| Prime Product (Demo)   | Product of primes              |                 O(n) |      O(1) | **Not robust**; overflow/collisions risk        |

---

## 11) 🧰 Why Optimization Works (Conceptual)

* **Hash/array counts** compress the multiset equality check to **O(1)** average updates per character, eliminating the **O(n log n)** sorting overhead.
* **Fixed-size arrays** exploit known small alphabets to achieve **true O(1) space** and excellent cache locality.
* **Early exit** (length check, negative count) stops work as soon as mismatch is provable.

---

## 12) 🧑‍💻 Final "Ready-to-Use" Functions (Recommended)

### Python (type hints) — Fixed 26 Counts (lowercase)

```python
from typing import List

def is_anagram(s: str, t: str) -> bool:
    """
    Return True if t is an anagram of s (lowercase English letters), else False.
    Time: O(n), Space: O(1)
    """
    if len(s) != len(t):
        return False
    counts = [0] * 26
    base = ord('a')
    for cs, ct in zip(s, t):
        counts[ord(cs) - base] += 1
        counts[ord(ct) - base] -= 1
    return all(v == 0 for v in counts)
```

### Java — Fixed 26 Counts (lowercase)

```java
public static boolean isAnagram(final String s, final String t) {
    // Return true if t is an anagram of s (lowercase English letters).
    // Time: O(n), Space: O(1)
    if (s.length() != t.length()) return false;
    final int[] cnt = new int[26];
    for (int i = 0; i < s.length(); i++) {
        cnt[s.charAt(i) - 'a']++;
        cnt[t.charAt(i) - 'a']--;
    }
    for (int v : cnt) if (v != 0) return false;
    return true;
}
```

> **Unicode follow-up:** swap the 26-array with a hash map (Approach B/C).

---

## 13) 📌 Quick Practice Plan

**How to practice**

1. **Unit tests (tiny):**

   * `("anagram", "nagaram") → True`
   * `("rat", "car") → False`
   * `("a", "a") → True`, `("a", "b") → False`
   * `("aabb", "baba") → True`, `("aabb", "abbb") → False`
2. **Edge tests:**

   * Empty vs. empty (if allowed); case with Unicode like `"résumé"` vs. `"ésumér"`.
   * Very long random strings—compare your `O(n)` solution with sorting baseline for correctness equivalence.
3. **Differential checks:**

   * Randomly shuffle `s` to generate a positive case.
   * Mutate one character in `t` to generate a negative case.
4. **Cross-approach validation:**

   * Implement both **sorting** and **counts**; compare outputs across 1000 random trials.

**Sample I/O**

* Input: `s="anagram", t="nagaram"` → Output: `true`
* Input: `s="rat", t="car"` → Output: `false`
* Input: `s="aabbcc", t="baccab"` → Output: `true`
* Input: `s="abc", t="abz"` → Output: `false`

---

### 🚀 Recap

* Start with length check.
* Prefer **O(n) counting** (fixed array for lowercase; hash map for Unicode).
* Use sorting as a simple baseline.
* Avoid misleading shortcuts (XOR, sets).
* Be ready to discuss trade-offs (time, space, alphabet assumptions).
