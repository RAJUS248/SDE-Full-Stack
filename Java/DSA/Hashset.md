
# Beginner-Friendly Notes on **HashSet** in Java

---

## 1. What is a HashSet?

* A **collection** that stores **unique elements only** (no duplicates allowed).
* **No indexing** (cannot access by position).
* **No ordering** guarantee (elements may appear in any order).
* Best for **fast membership checks** like: “Is this item present?”

---

## 2. Syntax & Basic Operations

```java
import java.util.HashSet;
import java.util.Set;

public class HashSetDemo {
    public static void main(String[] args) {
        // 1) Create a HashSet
        Set<String> fruits = new HashSet<>();

        // 2) Add elements
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Mango");
        fruits.add("Apple"); // Duplicate -> ignored

        // 3) Check presence
        System.out.println(fruits.contains("Mango")); // true

        // 4) Remove element
        fruits.remove("Banana");

        // 5) Iterate
        for (String f : fruits) {
            System.out.println(f);
        }

        // 6) Clear all
        fruits.clear();
    }
}
```

---

## 3. Internals: How HashSet Works

* **HashSet is built on top of HashMap.**

  * Each element is stored as a **key** in a hidden HashMap.
  * A dummy object acts as the value.
* When you add an element:

  * Its `hashCode()` decides which **bucket** it goes into.
  * If another element has the same hash → a **collision** happens.
  * Collisions are resolved by **linked lists** or **balanced trees** (since Java 8).
* Complexity:

  * **Add, Remove, Search** → O(1) average
  * Worst-case → O(n) (many collisions)

---

## 4. When to Use HashSet

* To **avoid duplicates** automatically.
* When **fast searching** matters more than ordering.
* Examples:

  * Store unique student roll numbers
  * Keep track of visited nodes in graph search
  * Maintain a list of unique words from a document

---

## 5. Comparison with ArrayList and HashMap

| Feature         | **HashSet**              | **ArrayList**                             | **HashMap**                    |
| --------------- | ------------------------ | ----------------------------------------- | ------------------------------ |
| Purpose         | Store unique values      | Store ordered values (duplicates allowed) | Store key → value pairs        |
| Duplicates      | ❌ No                     | ✅ Yes                                     | Keys ❌, Values ✅               |
| Ordering        | ❌ Not guaranteed         | ✅ Insertion order                         | ❌ Not guaranteed               |
| Access by index | ❌                        | ✅ `list.get(i)`                           | ❌ (use key lookup)             |
| Search speed    | O(1) avg (`contains`)    | O(n)                                      | O(1) avg (`get(key)`)          |
| Best for        | Uniqueness + fast lookup | Maintaining ordered sequence              | Mapping data (dictionary-like) |

---

## 6. Pros & Cons of HashSet

✅ **Pros**

* Very fast add/remove/search (average O(1))
* Automatically prevents duplicates
* Easy to use for “uniqueness” problems

❌ **Cons**

* No ordering or indexing
* Requires good `hashCode()` and `equals()` implementation
* Not memory-efficient compared to arrays

---

## 7. Public Methods in **HashSet**

> These come from the `Set` interface and `Collection` interface (which HashSet implements).
> Some are **most commonly used** (marked ⭐).

### Adding and Removing

* `boolean add(E e)` ⭐ → Adds element if not present; returns true if added.
* `boolean addAll(Collection<? extends E> c)` → Adds all elements from another collection.
* `boolean remove(Object o)` ⭐ → Removes given element if present.
* `boolean removeAll(Collection<?> c)` → Removes all matching elements.
* `boolean retainAll(Collection<?> c)` → Keeps only elements present in given collection.
* `void clear()` ⭐ → Removes all elements.

### Querying

* `boolean contains(Object o)` ⭐ → Checks if element exists.
* `boolean containsAll(Collection<?> c)` → Checks if set contains all elements of another collection.
* `boolean isEmpty()` ⭐ → Returns true if set is empty.
* `int size()` ⭐ → Returns number of elements.

### Iterating

* `Iterator<E> iterator()` ⭐ → Returns iterator to loop over set.
* `Spliterator<E> spliterator()` → For parallel stream operations.
* `Stream<E> stream()` → Creates sequential stream.
* `Stream<E> parallelStream()` → Creates parallel stream.

### Converting

* `Object[] toArray()` → Converts set to plain array.
* `<T> T[] toArray(T[] a)` → Converts to typed array.

### Other

* `boolean equals(Object o)` → Checks equality with another set.
* `int hashCode()` → Returns hash code of the set.

---

⚡ **Key Takeaway**:
Most beginners only need:

* `add()`, `remove()`, `contains()`, `size()`, `isEmpty()`, `clear()`, and `iterator()/for-each`.

