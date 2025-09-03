
## 1. `HashMap<K,V>` – Fast lookups, no order

* **Problem it solves:** quickly find a value by key.
* **Issue:** order is not guaranteed.

```java
Map<Integer, String> products = new HashMap<>();
products.put(101, "Laptop");
products.put(102, "Phone");

System.out.println(products.get(101)); // Laptop
```

👉 Use when: you just care about speed.

---

## 2. `LinkedHashMap<K,V>` – Keeps order

* **Problem:** `HashMap` loses order.
* **Fix:** `LinkedHashMap` remembers order.

```java
Map<String, Integer> dialCodes = new LinkedHashMap<>();
dialCodes.put("India", 91);
dialCodes.put("USA", 1);
dialCodes.put("UK", 44);

System.out.println(dialCodes); 
// Prints in same order you inserted
```

👉 Use when: you want predictable order.

---

## 3. `TreeMap<K,V>` – Sorted keys

* **Problem:** `HashMap` doesn’t sort keys.
* **Fix:** `TreeMap` keeps them sorted.

```java
Map<Integer, String> scores = new TreeMap<>();
scores.put(50, "Alice");
scores.put(80, "Bob");
scores.put(70, "Charlie");

System.out.println(scores); 
// {50=Alice, 70=Charlie, 80=Bob}
```

👉 Use when: you need **sorting** or **range queries**.

---

## 4. `ConcurrentHashMap<K,V>` – Thread-safe

* **Problem:** `HashMap` breaks with multiple threads.
* **Fix:** `ConcurrentHashMap` handles concurrency safely.

```java
ConcurrentHashMap<String, Integer> counter = new ConcurrentHashMap<>();
counter.put("views", 1);
counter.merge("views", 1, Integer::sum); // Atomic increment
```

👉 Use when: multiple threads update/read at the same time.

---

## 5. `WeakHashMap<K,V>` – Auto-remove when key is unused

* **Problem:** cache grows forever.
* **Fix:** entries disappear when key is garbage-collected.

```java
Map<Object, String> cache = new WeakHashMap<>();
Object key = new Object();
cache.put(key, "metadata");

key = null; // no strong reference left
System.gc(); // entry may vanish
```

👉 Use when: you want a memory-sensitive cache.

---

## 6. `IdentityHashMap<K,V>` – Key comparison by `==`

* **Problem:** sometimes you want to check object **identity**, not equality.
* **Fix:** `IdentityHashMap` compares references.

```java
Map<String, String> map = new IdentityHashMap<>();
map.put(new String("A"), "one");
map.put(new String("A"), "two");

System.out.println(map.size()); // 2 (because keys are different objects)
```

👉 Use when: identity matters (rare).

---

## 7. `EnumMap<K,V>` – For enums

* **Problem:** `HashMap` wastes memory for enums.
* **Fix:** `EnumMap` is super-fast and compact.

```java
enum State { CREATED, RUNNING, DONE }
Map<State, String> workflow = new EnumMap<>(State.class);
workflow.put(State.CREATED, "start");
workflow.put(State.RUNNING, "process");
```

👉 Use when: key is an enum.

---

## 8. `ConcurrentSkipListMap<K,V>` – Sorted + thread-safe

* **Problem:** need sorted map + multiple threads.
* **Fix:** `ConcurrentSkipListMap`.

```java
ConcurrentSkipListMap<Long, String> events = new ConcurrentSkipListMap<>();
events.put(1000L, "Start");
events.put(2000L, "Process");
events.put(1500L, "Check");

System.out.println(events); 
// Sorted by timestamp
```

👉 Use when: both **concurrency** and **sorting** needed.

---

## 9. `Collections.synchronizedMap()` – Simple sync wrapper

* **Problem:** make existing map thread-safe quickly.
* **Fix:** wrap it.

```java
Map<String, String> map = Collections.synchronizedMap(new HashMap<>());
map.put("a", "apple");
```

👉 Use when: you need quick sync but don’t care about high performance.

---

## 10. Custom Key with `equals()` and `hashCode()`

* **Problem:** wrong equality leads to lookup bugs.
* **Fix:** make key class immutable with proper equality.

```java
final class EmployeeId {
    private final String id;
    public EmployeeId(String id) { this.id = id; }

    @Override public boolean equals(Object o) { return o instanceof EmployeeId e && id.equals(e.id); }
    @Override public int hashCode() { return id.hashCode(); }
}
```

👉 Use when: your key is a custom object.

---

### 🔑 Key takeaway

* Start with **HashMap**.
* Switch to **LinkedHashMap** (order), **TreeMap** (sorting), **ConcurrentHashMap** (threads), **EnumMap** (enums) only if you need their special behavior.

