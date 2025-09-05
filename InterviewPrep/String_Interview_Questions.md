# 25 Industry-Standard String Interview Questions (Specs + Declarations Only)

This set contains **25 high-frequency, industry-standard string problems** asked across **startups, product companies, and service firms**.  
Each problem provides: a precise spec, **Python & Java function declarations** (no implementation), **two valid examples**, **two invalid/edge inputs** with expected behavior, and **solution hints**.

**Error-handling convention**  
- **Python**: raise `ValueError` for invalid inputs (e.g., `None`, malformed arguments, overflow constraints when specified).  
- **Java**: throw `IllegalArgumentException` for the same classes of invalid inputs.  
Use clear names like `text`, `pattern`, `leftIndex`, `rightIndex`, `windowLength`, etc.

---

## Pattern-Recognition Playbook for String Problems

1. **Two Pointers (Left/Right or Both Ends)**  
   - Palindromes, reverse-in-place, trimming, skipping non-alphanumerics, comparison ignoring case.  
   - Sliding bounds for substrings (expand/shrink window).

2. **Sliding Window**  
   - Longest/shortest substrings under constraints: *no repeats, at most K distinct, contains all target chars*.  
   - Maintain counts with hash maps; move `left` to maintain invariant.

3. **Counting / Hashing**  
   - Anagrams, frequency sort, isomorphic checks, ransom-note feasibility.  
   - Normalize (case-fold, strip, filter) before counting if spec requires.

4. **Dynamic Programming**  
   - Edit distance, longest palindromic substring, decode ways, wildcard matching.  
   - Define subproblems and transitions, then optimize space.

5. **Stacks**  
   - Parentheses validation, decoding nested patterns (e.g., `3[a2[c]]`), expression parsing.

6. **Scanning & Parsing**  
   - `atoi` semantics, Roman numerals, IP restore, email normalization.  
   - Be explicit about overflow, whitespace, sign, invalid characters.

7. **Classic Algorithms**  
   - KMP / Z-algorithm / Rabin–Karp for substring search.  
   - Manacher for O(n) palindromes (advanced).

---

## 1) Longest Substring Without Repeating Characters

**Task**: Return the length of the longest substring with all distinct characters.  
**Assumptions**: ASCII or Unicode; clarify in prod—assume full Unicode code points if using Python/Java.

**Python**
```python
def length_of_longest_substring_without_repeats(text: str) -> int: ...
```

**Java**
```java
public static int lengthOfLongestSubstringWithoutRepeats(String text) { ... }
```

**Valid Examples**  
- `"abcabcbb"` → `3` (`"abc"`)  
- `"bbbbb"` → `1`

**Invalid Examples**  
- `text=None` → ValueError/IllegalArgumentException  
- Extremely long input with memory limits specified by caller → ValueError/IllegalArgumentException

**Hints**: Sliding window with last-seen index map (O(n)). Alternative: set + two pointers.

---

## 2) Longest Palindromic Substring

**Task**: Return the longest palindromic substring. If multiple, return any.  
**Assumptions**: Case-sensitive unless stated; treat full code points.

**Python**
```python
def longest_palindromic_substring(text: str) -> str: ...
```

**Java**
```java
public static String longestPalindromicSubstring(String text) { ... }
```

**Valid Examples**  
- `"babad"` → `"bab"` or `"aba"`  
- `"cbbd"` → `"bb"`

**Invalid Examples**  
- `text=None` → Error  
- Empty string allowed? If not, empty → Error (else return empty)

**Hints**: Expand-around-center (O(n^2), O(1)); Manacher’s (O(n)).

---

## 3) Valid Anagram

**Task**: Return whether `text` and `pattern` are anagrams (same counts).  
**Assumptions**: Normalize case/whitespace only if specified; default: exact character counts.

**Python**
```python
def is_anagram(text: str, pattern: str) -> bool: ...
```

**Java**
```java
public static boolean isAnagram(String text, String pattern) { ... }
```

**Valid Examples**  
- `"anagram", "nagaram"` → `True`  
- `"rat", "tar"` → `True`

**Invalid Examples**  
- `text=None, pattern="x"` → Error  
- Mismatched lengths but caller demands same-length → Error (otherwise return False)

**Hints**: Count map or fixed-size array if charset bounded.

---

## 4) Group Anagrams

**Task**: Group words that are anagrams. Return list of lists.

**Python**
```python
from typing import List
def group_anagrams(words: List[str]) -> List[List[str]]: ...
```

**Java**
```java
public static List<List<String>> groupAnagrams(List<String> words) { ... }
```

**Valid Examples**  
- `["eat","tea","tan","ate","nat","bat"]` → groups like `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`  
- `[""]` → `[[""]]`

**Invalid Examples**  
- `words=None` → Error  
- Very large list with null entries → Error

**Hints**: Signature key (sorted word) or frequency signature; O(n * k log k) / O(n*k).

---

## 5) Valid Parentheses

**Task**: Return true if parentheses/brackets/braces are properly closed and nested.

**Python**
```python
def is_valid_parentheses(text: str) -> bool: ...
```

**Java**
```java
public static boolean isValidParentheses(String text) { ... }
```

**Valid Examples**  
- `"()[]{}"` → `True`  
- `"{[]}"` → `True`

**Invalid Examples**  
- `"(]"` → `False` (or Error if malformed is defined invalid)  
- `text=None` → Error

**Hints**: Stack with pair map; O(n).

---

## 6) String Compression (Basic)

**Task**: Compress runs: `"aabcccccaaa"` → `"a2b1c5a3"`. If compressed not shorter, return original.

**Python**
```python
def compress_basic(text: str) -> str: ...
```

**Java**
```java
public static String compressBasic(String text) { ... }
```

**Valid Examples**  
- `"aabcccccaaa"` → `"a2b1c5a3"`  
- `"abc"` → `"abc"`

**Invalid Examples**  
- `text=None` → Error  
- Non-letter characters present but spec forbids → Error

**Hints**: Linear scan, count runs. Beware integer-to-string cost.

---

## 7) Run-Length Encoding

**Task**: Return run-length encoded form without the “shorter check”.

**Python**
```python
def run_length_encode(text: str) -> str: ...
```

**Java**
```java
public static String runLengthEncode(String text) { ... }
```

**Valid Examples**  
- `"wwwwaaadexxxxxx"` → `"w4a3d1e1x6"`  
- `"aaa"` → `"a3"`

**Invalid Examples**  
- `text=None` → Error  
- Empty string (if spec forbids) → Error

**Hints**: Iterate, count consecutive, append `char+count`.

---

## 8) Run-Length Decoding

**Task**: Decode strings like `"a2b1c5a3"` → `"aabcccccaaa"`.

**Python**
```python
def run_length_decode(encoded: str) -> str: ...
```

**Java**
```java
public static String runLengthDecode(String encoded) { ... }
```

**Valid Examples**  
- `"w4a3d1e1x6"` → `"wwwwaaadexxxxxx"`  
- `"a3"` → `"aaa"`

**Invalid Examples**  
- Non-numeric counts (e.g., `"a#"`), negative counts → Error  
- `encoded=None` → Error

**Hints**: Parse digits possibly multi-digit; watch for overflow/invalid format.

---

## 9) Implement `strStr` / Substring Search

**Task**: Return first index of `pattern` in `text`; `-1` if absent.

**Python**
```python
def find_substring_index(text: str, pattern: str) -> int: ...
```

**Java**
```java
public static int findSubstringIndex(String text, String pattern) { ... }
```

**Valid Examples**  
- `text="hello", pattern="ll"` → `2`  
- `text="aaaaa", pattern="bba"` → `-1`

**Invalid Examples**  
- `pattern=""` with undefined behavior → Error (or define as 0)  
- `text=None` or `pattern=None` → Error

**Hints**: KMP (O(n+m)), or Rabin–Karp; brute force O(n*m).

---

## 10) Minimum Window Substring

**Task**: Find the smallest substring of `text` containing all chars (with multiplicity) of `required`. Return `""` if none.

**Python**
```python
def min_window_substring(text: str, required: str) -> str: ...
```

**Java**
```java
public static String minWindowSubstring(String text, String required) { ... }
```

**Valid Examples**  
- `text="ADOBECODEBANC", required="ABC"` → `"BANC"`  
- `text="a", required="a"` → `"a"`

**Invalid Examples**  
- `required=""` → Error  
- `text=None` or `required=None` → Error

**Hints**: Sliding window with need/have counts; O(n).

---

## 11) Check String Rotation

**Task**: Return true if `s2` is a rotation of `s1` (same length).

**Python**
```python
def is_rotation(s1: str, s2: str) -> bool: ...
```

**Java**
```java
public static boolean isRotation(String s1, String s2) { ... }
```

**Valid Examples**  
- `"waterbottle", "erbottlewat"` → `True`  
- `"aa", "aa"` → `True`

**Invalid Examples**  
- Different lengths → `False` (or Error if spec demands equal length)  
- `s1=None` or `s2=None` → Error

**Hints**: Check `s2 in s1+s1` when lengths match.

---

## 12) Repeated Substring Pattern

**Task**: Return true if the string can be built by repeating a substring.

**Python**
```python
def is_repeated_substring_pattern(text: str) -> bool: ...
```

**Java**
```java
public static boolean isRepeatedSubstringPattern(String text) { ... }
```

**Valid Examples**  
- `"abab"` → `True`  
- `"aba"` → `False`

**Invalid Examples**  
- `text=None` → Error  
- Empty string if forbidden → Error

**Hints**: Check in `(text+text)[1:-1]` or KMP prefix function.

---

## 13) Edit Distance (Levenshtein)

**Task**: Return minimum edits (insert/delete/replace) to convert `source` → `target`.

**Python**
```python
def edit_distance(source: str, target: str) -> int: ...
```

**Java**
```java
public static int editDistance(String source, String target) { ... }
```

**Valid Examples**  
- `"horse" → "ros"` → `3`  
- `"intention" → "execution"` → `5`

**Invalid Examples**  
- Either is `None` → Error  
- Very large sizes without DP memory bound → Error

**Hints**: Classic DP (O(mn)); space-optimized rows.

---

## 14) Isomorphic Strings

**Task**: Return true if a bijection between characters of two strings exists.

**Python**
```python
def are_isomorphic(text: str, pattern: str) -> bool: ...
```

**Java**
```java
public static boolean areIsomorphic(String text, String pattern) { ... }
```

**Valid Examples**  
- `"egg","add"` → `True`  
- `"foo","bar"` → `False`

**Invalid Examples**  
- Different lengths with spec requiring equal → Error  
- `None` inputs → Error

**Hints**: Two maps (forward & reverse) or one map + seen set.

---

## 15) Remove Adjacent Duplicates

**Task**: Repeatedly remove adjacent equal characters until no more can be removed; return result.

**Python**
```python
def remove_adjacent_duplicates(text: str) -> str: ...
```

**Java**
```java
public static String removeAdjacentDuplicates(String text) { ... }
```

**Valid Examples**  
- `"abbaca"` → `"ca"`  
- `"azxxzy"` → `"ay"`

**Invalid Examples**  
- `text=None` → Error  
- Non-string types → Error

**Hints**: Stack of chars; O(n).

---

## 16) String to Integer (atoi)

**Task**: Parse string to 32-bit signed integer with whitespace, optional sign, digits, and overflow clamping.

**Python**
```python
def parse_atoi_32(text: str) -> int: ...
```

**Java**
```java
public static int parseAtoi32(String text) { ... }
```

**Valid Examples**  
- `"42"` → `42`  
- `"   -42"` → `-42`

**Invalid Examples**  
- Overflow beyond 32-bit → clamp or Error (define behavior)  
- `text=None` → Error

**Hints**: Scan; handle sign; accumulate; clamp to INT_MIN/INT_MAX if required.

---

## 17) Roman to Integer

**Task**: Convert valid Roman numeral to integer.

**Python**
```python
def roman_to_int(roman: str) -> int: ...
```

**Java**
```java
public static int romanToInt(String roman) { ... }
```

**Valid Examples**  
- `"III"` → `3`  
- `"MCMXCIV"` → `1994`

**Invalid Examples**  
- Invalid subtractive pair (e.g., `"IL"`) → Error  
- `roman=None` → Error

**Hints**: Map values; handle subtractive cases by lookahead.

---

## 18) Integer to Roman

**Task**: Convert integer (1..3999) to Roman numeral.

**Python**
```python
def int_to_roman(value: int) -> str: ...
```

**Java**
```java
public static String intToRoman(int value) { ... }
```

**Valid Examples**  
- `3` → `"III"`  
- `1994` → `"MCMXCIV"`

**Invalid Examples**  
- Out of range (`<=0` or `>3999`) → Error  
- Non-integer types → Error

**Hints**: Greedy with value-symbol pairs.

---

## 19) Zigzag Conversion

**Task**: Convert string in zigzag over `numRows` and read row-by-row.

**Python**
```python
def zigzag_convert(text: str, num_rows: int) -> str: ...
```

**Java**
```java
public static String zigzagConvert(String text, int numRows) { ... }
```

**Valid Examples**  
- `"PAYPALISHIRING", numRows=3` → `"PAHNAPLSIIGYIR"`  
- `"A", numRows=1` → `"A"`

**Invalid Examples**  
- `numRows<=0` → Error  
- `text=None` → Error

**Hints**: Simulate row traversal; track direction; O(n).

---

## 20) URLify (Replace Spaces)

**Task**: Replace spaces with `%20` (optionally trim trailing spaces).

**Python**
```python
def urlify(text: str) -> str: ...
```

**Java**
```java
public static String urlify(String text) { ... }
```

**Valid Examples**  
- `"Mr John Smith"` → `"Mr%20John%20Smith"`  
- `" a b "` → `"%20a%20b%20"` (if not trimming)

**Invalid Examples**  
- `text=None` → Error  
- If only ASCII allowed and text has unicode spaces → Error

**Hints**: Scan and build; or in-place with char array sizing.

---

## 21) Text Justification (Full Justify)

**Task**: Given list of words and `maxWidth`, return fully-justified text lines.

**Python**
```python
from typing import List
def full_justify(words: List[str], max_width: int) -> List[str]: ...
```

**Java**
```java
public static List<String> fullJustify(List<String> words, int maxWidth) { ... }
```

**Valid Examples**  
- `["This","is","an","example","of","text","justification."], maxWidth=16` → lines as per LeetCode 68  
- Left-justify last line

**Invalid Examples**  
- `max_width<=0` → Error  
- `words=None` or contains `None` → Error

**Hints**: Greedy pack words; distribute spaces; handle last line specially.

---

## 22) Restore IP Addresses

**Task**: Return all valid IPv4 addresses formed by inserting 3 dots in a numeric string.

**Python**
```python
from typing import List
def restore_ip_addresses(digits: str) -> List[str]: ...
```

**Java**
```java
public static List<String> restoreIPAddresses(String digits) { ... }
```

**Valid Examples**  
- `"25525511135"` → `["255.255.11.135","255.255.111.35"]`  
- `"0000"` → `["0.0.0.0"]`

**Invalid Examples**  
- Segments with leading zeros like `"01"` (if length>1) → Error/skip  
- Non-digit characters or `digits=None` → Error

**Hints**: Backtracking with pruning (segment length 1..3, value 0..255).

---

## 23) Add Binary Strings

**Task**: Add two binary strings and return binary sum string.

**Python**
```python
def add_binary_strings(a: str, b: str) -> str: ...
```

**Java**
```java
public static String addBinaryStrings(String a, String b) { ... }
```

**Valid Examples**  
- `"11" + "1"` → `"100"`  
- `"1010" + "1011"` → `"10101"`

**Invalid Examples**  
- Non-binary characters → Error  
- `a=None` or `b=None` → Error

**Hints**: Add from right to left; carry; O(n).

---

## 24) Multiply Strings (Big Integer)

**Task**: Multiply two non-negative integer strings (no built-in big-int).

**Python**
```python
def multiply_numeric_strings(lhs: str, rhs: str) -> str: ...
```

**Java**
```java
public static String multiplyNumericStrings(String lhs, String rhs) { ... }
```

**Valid Examples**  
- `"2" * "3"` → `"6"`  
- `"123" * "456"` → `"56088"`

**Invalid Examples**  
- Leading `+/-` if not supported → Error  
- Non-digit characters or None → Error

**Hints**: Grade-school multiplication; result array; trim leading zeros.

---

## 25) Frequency Sort Characters

**Task**: Sort characters by frequency (desc). Ties can keep any order unless required.

**Python**
```python
def frequency_sort_characters(text: str) -> str: ...
```

**Java**
```java
public static String frequencySortCharacters(String text) { ... }
```

**Valid Examples**  
- `"tree"` → `"eetr"` or `"eert"`  
- `"cccaaa"` → `"aaaccc"` or `"cccaaa"` (both valid depending on tie rule)

**Invalid Examples**  
- `text=None` → Error  
- Extremely large text with memory cap → Error

**Hints**: Count map + bucket sort / heap.

---

## Tips & Tricks for String Interviews

- **Normalize Early**: Decide on case-folding, trimming, and filtering non-alphanumerics before logic.  
- **Choose the Right Pattern**:  
  - *Two pointers*: palindromes, in-place swaps, ends-meet comparisons.  
  - *Sliding window*: longest/shortest substrings under constraints.  
  - *DP*: edit distance, palindromic substrings.  
  - *Stack*: parentheses, nested decodings.  
  - *Greedy/Parsing*: text justification, `atoi`, Roman numerals.  
- **Complexity Awareness**: String concatenation repeatedly can be O(n²). Prefer builders (`StringBuilder` in Java) or list-join in Python.  
- **Unicode Caveats**: In real systems, handle grapheme clusters (emoji), normalization forms (NFC/NFD).  
- **Robust Contracts**: Define behavior for empty strings, `None`/`null`, overflow/underflow, and invalid formats.  
- **Explain Before You Code**: State invariants for sliding windows, what your pointers represent, and when they move.

Good luck and happy practicing!