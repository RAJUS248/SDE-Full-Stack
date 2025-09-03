# Java `HashMap` 

> **What is it?**
> A `HashMap<K, V>` stores **pairs** like `rollNo → studentName`.
> You look up by **key** (e.g., roll number) and get the **value** (e.g., the student’s name).
> It’s **fast on average**: `put`, `get`, and `remove` are typically **O(1)**.

---

## 1) Why use a `HashMap`?

* **Fast lookups**: Find a value by key without scanning the whole list.
* **Flexible keys/values**: Keys and values can be any objects.
* **Real life analogy**: Think of a **college library index**. You don’t scan every shelf; you go to a specific drawer using the index.

---

## 2) Quick picture: how it stores things

A `HashMap` keeps an **array of buckets** (think of them as **boxes**).
The **key’s hash** decides **which box** an entry goes into.

```
array index →     0      1      2      3      4      5      6      7  ...  n-1
                 ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐
bucket pointer → │   │→ │ A │→ │   │  │ B │→ │   │  │   │  │ C │→ │   │ ...
                 └───┘  └───┘  └───┘  └───┘  └───┘  └───┘  └───┘  └───┘

Legend: A/B/C = linked lists of entries (if multiple keys land in the same bucket)
```

* If two different keys go to the **same bucket**, they form a small **linked list** there (a **collision**).
* Modern Java can convert long lists to a **tree** internally to stay fast, but as a beginner just remember: **on average it’s O(1)**.

---

## 3) Minimal, very clear example

```java
import java.util.HashMap;
import java.util.Map;

public class CollegeMapBasics {
    public static void main(String[] args) {
        // Create a map: rollNo (Integer) -> studentName (String)
        Map<Integer, String> students = new HashMap<>();

        // PUT: add (or replace) a key->value
        students.put(101, "Asha");
        students.put(102, "Ravi");
        students.put(103, "Meera");

        // GET: read value by key
        System.out.println(students.get(102)); // "Ravi"

        // UPDATE: putting same key replaces old value
        students.put(102, "Ravi Kumar");
        System.out.println(students.get(102)); // "Ravi Kumar"

        // CONTAINS: check existence
        System.out.println(students.containsKey(999)); // false

        // REMOVE: delete by key
        students.remove(103);

        // SIZE & ITERATION: loop over entries (order is NOT guaranteed)
        System.out.println("Total: " + students.size()); // e.g., 2
        for (Map.Entry<Integer, String> e : students.entrySet()) {
            System.out.println(e.getKey() + " -> " + e.getValue());
        }

        // Safe default if key missing
        String name = students.getOrDefault(555, "Unknown");
        System.out.println(name); // "Unknown"
    }
}
```

**What just happened?**

* `put` stores key→value.
* `get` fetches by key.
* Re-using a key **overwrites** the old value.
* **Order is not guaranteed** (don’t expect insertion order).

---

## 4) How does `HashMap` find things so quickly?

1. It calls `key.hashCode()` to get a number.
2. It **maps** that number to a bucket index (like `index = hash % numberOfBuckets`).
3. It checks that bucket.

   * If the exact key is found (checked via **`equals()`**), it returns the value.
   * If there are multiple entries (collision), it walks that small list to find the match.

**Tiny demo of collisions (conceptual):**

```
Bucket 5:
  [hash=..., key=101, value="Asha"] -> [hash=..., key=205, value="Pooja"] -> null
    ^ both keys happened to land in bucket 5, so we keep a small chain
```

---

## 5) Time complexity (Big-O)

| Operation           | Average time | Worst time (rare) | Notes                                                         |
| ------------------- | ------------ | ----------------- | ------------------------------------------------------------- |
| `put(key, value)`   | **O(1)**     | O(log n) / O(n)\* | \*Java can tree-ify long chains to keep lookups near O(log n) |
| `get(key)`          | **O(1)**     | O(log n) / O(n)\* | Depends on collisions; average is constant time               |
| `remove(key)`       | **O(1)**     | O(log n) / O(n)\* | Similar reasoning                                             |
| Iterate all entries | **O(n)**     | O(n)              | You visit every entry once                                    |

> For beginner intuition: **Assume O(1) on average** for put/get/remove.
> The rare worst cases are handled internally to avoid huge slowdowns.

---

## 6) Important facts you’ll use a lot

* **Nulls**: `HashMap` allows **1 null key** and **many null values**.
* **Overwriting**: `put` with an existing key **replaces** the old value.
* **No order**: `HashMap` does **not** guarantee iteration order.
* **Fail-fast**: Changing the map while iterating (except via iterator’s `remove`) can throw `ConcurrentModificationException`.

---

## 7) Custom keys (beginner-safe version)

If you use **your own class** as a **key**, you must define **logical equality** so that keys behave correctly.

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

// We'll key the map by StudentId (string). Two StudentId objects
// with the same id should be treated as the SAME key.
final class StudentId {
    private final String id; // keep it IMMUTABLE to avoid bugs

    StudentId(String id) {
        this.id = id;
    }

    // Two StudentId are equal if their 'id' text is equal
    @Override public boolean equals(Object o) {
        if (this == o) return true;          // same object
        if (!(o instanceof StudentId)) return false;
        StudentId other = (StudentId) o;
        return Objects.equals(this.id, other.id);
    }

    // Must match equals: equal ids → equal hash codes
    @Override public int hashCode() {
        return Objects.hash(id);
    }

    @Override public String toString() { return id; }
}

public class CustomKeyBeginner {
    public static void main(String[] args) {
        Map<StudentId, String> names = new HashMap<>();

        names.put(new StudentId("21CS001"), "Asha");
        names.put(new StudentId("21CS001"), "Asha Updated"); // replaces previous (same logical key)
        names.put(new StudentId("21CS002"), "Ravi");

        // Works because equals/hashCode say "21CS001" == "21CS001"
        System.out.println(names.get(new StudentId("21CS001"))); // "Asha Updated"
        System.out.println(names.size()); // 2
    }
}
```

**Rule of thumb:**

* Make the fields used in `equals/hashCode` **immutable**.
* If you change a key’s field after insertion, the map may not find it again.

---

## 8) Resizing (what happens when it grows?)

* The map starts with some **capacity** (number of buckets).
* When it gets “too full” (controlled by **load factor**, default \~0.75), it **doubles** the buckets and **re-distributes** entries.
* This keeps buckets from getting crowded and maintains **O(1)** average time.

**Concept sketch:**

```
Before: capacity = 8, size ≈ 7  → resize
After:  capacity = 16 (more buckets) → entries spread out again
```

You usually **don’t** need to manage this manually, but if you know you’ll store, say, **50,000 entries**, you can **pre-size**:

```java
// Rough formula: initialCapacity ≈ expectedSize / loadFactor
Map<Integer, String> big = new HashMap<>( (int)Math.ceil(50_000 / 0.75) );
```

---

## 9) A few very common patterns

### A) Frequency count (word → count)

```java
import java.util.*;

public class WordCount {
    public static void main(String[] args) {
        String[] words = {"java","hashmap","java","map","java","code"};
        Map<String, Integer> freq = new HashMap<>();

        for (String w : words) {
            // If absent, default to 0; then add 1
            freq.put(w, freq.getOrDefault(w, 0) + 1);
        }
        System.out.println(freq); // {java=3, hashmap=1, map=1, code=1}
    }
}
```

### B) Grouping by first letter

```java
import java.util.*;

public class GroupByFirstLetter {
    public static void main(String[] args) {
        List<String> names = List.of("Asha","Anil","Ravi","Ramesh","Meera");
        Map<Character, List<String>> groups = new HashMap<>();

        for (String name : names) {
            char first = name.charAt(0);
            // Make a new list if key not present
            groups.computeIfAbsent(first, k -> new ArrayList<>()).add(name);
        }
        System.out.println(groups); // {A=[Asha, Anil], R=[Ravi, Ramesh], M=[Meera]}
    }
}
```

---

## 10) Quick checklist (for exams & interviews)

* **Use `HashMap`** when you need **fast** key→value lookups and **order doesn’t matter**.
* **Average O(1)** for `put`, `get`, `remove`.
* **One null key** and **many null values** allowed.
* **Equality of keys** is decided by `equals()` and **bucket choice** by `hashCode()`.
* For **custom keys**, **override both** `equals()` and `hashCode()` and keep key fields **immutable**.
* Iteration is **O(n)** and order is **not guaranteed**.

---

### TL;DR

* `HashMap` = **fast dictionary** for Java.
* Think **“index → bucket → (maybe a tiny list)”** when visualizing.
* Use it for **fast lookups**, **counts**, and **grouping** by a key.
