# 15 Medium-Complexity Interview Questions — Arrays + Strings Only
Targeted for FAANG/MAMAA-style interviews (Microsoft, Amazon, Google, Meta, etc.).  
**Data structures allowed**: arrays and strings only (treat Python lists as arrays). Avoid hash maps/sets/tries unless you can simulate fixed-size counts with arrays (e.g., 26/128/256 buckets).  
For each problem: implement the function, handle invalid inputs explicitly, and **state time & space complexity** in your submission.

---

## 1) Train Platforms Needed (Minimum Platforms)
**Story**: A station master wants to know the minimum number of platforms required so that no train has to wait.
**Spec**: Given arrival and departure times as **two integer arrays** of equal length (minutes since 00:00), compute the minimum platforms required so no intervals overlap on the same platform.

**Python**
```python
from typing import List
def min_platforms_required(arrivals: List[int], departures: List[int]) -> int: ...
```

**Java**
```java
public static int minPlatformsRequired(int[] arrivals, int[] departures) { ... }
```

**Valid Examples**
- `arrivals=[900, 940, 950, 1100, 1500, 1800], departures=[910,1200,1120,1130,1900,2000]` → `3`
- `arrivals=[1000,1010], departures=[1005,1020]` → `2`
- `arrivals=[600], departures=[700]` → `1`

**Invalid Examples**
- `arrivals=None, departures=[1,2]` → Error
- Length mismatch → Error
- Times outside `[0, 2359]` or malformed (e.g., `2399`) → Error

**Edge Cases**
- All trains non-overlapping → 1
- All trains fully overlapping → n

Ask to report **time/space complexity** (e.g., sorting-based two-pointer).

---

## 2) Bus Seat Manifest Normalizer
**Story**: A bus company stores seats as CSV like `"1A,3C,2B"`. Produce a **sorted, normalized** manifest and also return **missing seats** for a given `rowCount` and seat letters (e.g., `["A","B","C"]`).

**Python**
```python
from typing import List, Tuple
def normalize_manifest_and_missing(manifest_csv: str, row_count: int, seat_letters: List[str]) -> Tuple[List[str], List[str]]: ...
```

**Java**
```java
public static class ManifestResult { public String[] normalized; public String[] missing; }
public static ManifestResult normalizeManifestAndMissing(String manifestCsv, int rowCount, String[] seatLetters) { ... }
```

**Valid Examples**
- `"1A,3C,2B", row_count=3, seat_letters=["A","B","C"]` → normalized `["1A","2B","3C"]`, missing `["1B","1C","2A","2C","3A","3B"]`
- `"2A,2C,1A", row_count=2, seat_letters=["A","B","C"]` → normalized `["1A","2A","2C"]`, missing `["1B","1C","2B"]`

**Invalid Examples**
- `row_count<=0` → Error
- `seat_letters` empty or contains non-letters → Error
- Duplicated seats in input → Error (or de-duplicate per spec)

**Edge Cases**
- Extra spaces, different case (`" 1a , 2B"`) → normalize

---

## 3) School Attendance Streak
**Story**: Each student’s monthly attendance is a string of `'P'` (present) and `'A'` (absent). Find the **longest consecutive presence streak**.

**Python**
```python
def longest_presence_streak(attendance: str) -> int: ...
```

**Java**
```java
public static int longestPresenceStreak(String attendance) { ... }
```

**Valid Examples**
- `"PPAPPPAAAPPPPP"` → `5`
- `"AAAA"` → `0`
- `"P"` → `1`

**Invalid Examples**
- `attendance=None` → Error
- Any char not in `{P,A}` → Error

**Edge Cases**
- Empty string → `0` (if allowed) or Error per contract

---

## 4) Baggage Tag Shortest Unique Prefix
**Story**: Airport baggage tags are strings. For each tag, compute the **shortest unique prefix** among all tags.

**Python**
```python
from typing import List
def shortest_unique_prefixes(tags: List[str]) -> List[str]: ...
```

**Java**
```java
public static String[] shortestUniquePrefixes(String[] tags) { ... }
```

**Valid Examples**
- `["zebra","dog","duck","dove"]` → `["z","do","du","dov"]`
- `["apple","app"]` → `["appl","app"]`

**Invalid Examples**
- `tags=None` → Error
- Empty strings or duplicates → Error (or define behavior)

**Edge Cases**
- All tags share long common prefix

(Prefer array-only techniques: sort array and compare neighbors.)

---

## 5) Flight Booking Window Merge (Day Indices)
**Story**: A portal represents bookings as inclusive windows `[startDay, endDay]` (ints). Merge overlapping windows.

**Python**
```python
from typing import List, Tuple
def merge_booking_windows(windows: List[Tuple[int,int]]) -> List[Tuple[int,int]]: ...
```

**Java**
```java
public static int[][] mergeBookingWindows(int[][] windows) { ... }
```

**Valid Examples**
- `[[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]`
- `[[1,4],[4,5]]` → `[[1,5]]`

**Invalid Examples**
- `start > end` → Error
- `windows=None` → Error

**Edge Cases**
- Single window → same result

---

## 6) Library Shelf Anagram Groups
**Story**: Group book codes that are anagrams (letters only).

**Python**
```python
from typing import List
def group_book_code_anagrams(codes: List[str]) -> List[List[str]]: ...
```

**Java**
```java
public static List<List<String>> groupBookCodeAnagrams(String[] codes) { ... }
```

**Valid Examples**
- `["eat","tea","tan","ate","nat","bat"]` → groups like `[["eat","tea","ate"],["tan","nat"],["bat"]]`
- `[""]` → `[[""]]`

**Invalid Examples**
- `codes=None` → Error
- Non-alpha chars if forbidden → Error

**Edge Cases**
- Case sensitivity policy must be specified

(Hint: Sort each string to build a signature using arrays only.)

---

## 7) Cafeteria Menu Rotation Check
**Story**: Weekly menus are cyclic. Check if `todayMenu` is a **rotation** of `baselineMenu`.

**Python**
```python
def is_menu_rotation(baseline: str, today: str) -> bool: ...
```

**Java**
```java
public static boolean isMenuRotation(String baseline, String today) { ... }
```

**Valid Examples**
- `"pasta-soup-salad", "soup-salad-pasta"` → `True`
- `"abc", "cab"` → `True`

**Invalid Examples**
- Different lengths → `False` (or Error per contract)
- `None` inputs → Error

**Edge Cases**
- Identical strings → `True`

---

## 8) Chat Keyword Minimum Window
**Story**: Moderation needs the **shortest substring** containing all required keywords’ characters (multiplicity matters), within chat text.

**Python**
```python
def min_window_with_required_chars(text: str, required: str) -> str: ...
```

**Java**
```java
public static String minWindowWithRequiredChars(String text, String required) { ... }
```

**Valid Examples**
- `text="ADOBECODEBANC", required="ABC"` → `"BANC"`
- `text="a", required="a"` → `"a"`

**Invalid Examples**
- `required=""` → Error
- `text=None` or `required=None` → Error

**Edge Cases**
- No window exists → `""`

(Use fixed-size count arrays instead of maps.)

---

## 9) Warehouse Bin Run-Length Compression
**Story**: Encode bin labels by run-length (no “shorter” rule).

**Python**
```python
def rle_encode_bins(label: str) -> str: ...
```

**Java**
```java
public static String rleEncodeBins(String label) { ... }
```

**Valid Examples**
- `"AAABCCDDDD"` → `"A3B1C2D4"`
- `"Z"` → `"Z1"`

**Invalid Examples**
- `label=None` → Error
- Empty string if not allowed → Error

**Edge Cases**
- Very long runs; multi-digit counts

---

## 10) Train ID Search in Rotated Manifest
**Story**: Train IDs are stored as a rotated-sorted array. Find the index of a target ID.

**Python**
```python
from typing import List
def search_rotated_manifest(ids: List[int], target_id: int) -> int: ...
```

**Java**
```java
public static int searchRotatedManifest(int[] ids, int targetId) { ... }
```

**Valid Examples**
- `ids=[40,50,5,10,20,30], target=10` → `3`
- `ids=[5,6,7,0,1,2,4], target=3` → `-1`

**Invalid Examples**
- `ids=None` → Error
- Non-unique elements if spec requires uniqueness → Error

**Edge Cases**
- Single-element array

---

## 11) Theatre Bookings — Move Empty Seats to End
**Story**: Represent a row as an array where `0=empty`, `1=booked`. Move all zeros to the **end**, stability of `1`s preserved.

**Python**
```python
from typing import List
def move_empty_seats_to_end(row: List[int]) -> List[int]: ...
```

**Java**
```java
public static void moveEmptySeatsToEnd(int[] row) { ... }
```

**Valid Examples**
- `[0,1,0,3,12]` → `[1,3,12,0,0]`
- `[0]` → `[0]`

**Invalid Examples**
- `row=None` → Error
- Values not in `{0,1}` if binary expected → Error

**Edge Cases**
- Already compacted

---

## 12) School Roll Missing ID (0..n)
**Story**: Student IDs range `0..n` with one missing. Find the missing ID.

**Python**
```python
from typing import List
def find_missing_id(ids: List[int]) -> int: ...
```

**Java**
```java
public static int findMissingId(int[] ids) { ... }
```

**Valid Examples**
- `[3,0,1]` → `2`
- `[0,1]` → `2`

**Invalid Examples**
- Duplicates or out-of-range values → Error
- `ids=None` → Error

**Edge Cases**
- `n=0`

---

## 13) City Walk Validator (Back to Origin)
**Story**: A string of moves `N,S,E,W` determines a city walk. Return true if you end at origin.

**Python**
```python
def walk_returns_to_origin(moves: str) -> bool: ...
```

**Java**
```java
public static boolean walkReturnsToOrigin(String moves) { ... }
```

**Valid Examples**
- `"NS"` → `True`
- `"NESW"` → `True`

**Invalid Examples**
- `moves=None` → Error
- Characters outside `{N,S,E,W}` → Error

**Edge Cases**
- Empty string → `True`

(Use small fixed buckets for counts.)

---

## 14) Conference Agenda Merge (Two Sorted Arrays)
**Story**: Merge two sorted arrays of session start times into the first array which has enough trailing buffer.

**Python**
```python
from typing import List
def merge_sorted_agendas_into_first(a: List[int], m: int, b: List[int], n: int) -> None: ...
```

**Java**
```java
public static void mergeSortedAgendasIntoFirst(int[] a, int m, int[] b, int n) { ... }
```

**Valid Examples**
- `a=[1,2,3,0,0,0], m=3; b=[2,5,6], n=3` → `a=[1,2,2,3,5,6]`
- `a=[0], m=0; b=[1], n=1` → `a=[1]`

**Invalid Examples**
- `m+n != len(a)` → Error
- `a=None` or `b=None` → Error

**Edge Cases**
- One array empty

---

## 15) Baggage Carousel — Find Duplicate Tag
**Story**: Tag IDs are integers in `[1..n]` with one duplicate. Find the **duplicate** without modifying the array and with constant extra space.

**Python**
```python
from typing import List
def find_duplicate_tag(ids: List[int]) -> int: ...
```

**Java**
```java
public static int findDuplicateTag(int[] ids) { ... }
```

**Valid Examples**
- `[1,3,4,2,2]` → `2`
- `[3,1,3,4,2]` → `3`

**Invalid Examples**
- Values outside `[1..n]` → Error
- `ids=None` → Error

**Edge Cases**
- Duplicate value appears more than twice (define allowed or Error)

---

## Submission Requirements (for Students)
- Implement the specified function **signature** exactly (Python &/or Java).  
- For each problem, **print or document your time and space complexity**.  
- Stick to **arrays and strings**. If you need counts, use fixed-size arrays (e.g., 26/128/256); avoid hash maps/sets/graphs/tries unless you convert them to array-based buckets.

