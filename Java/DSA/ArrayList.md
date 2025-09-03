# ArrayList in Java 

## 1. What is an ArrayList?

* An **ArrayList** is like a **resizable array**.
* In a normal Java `array`, the size is fixed (e.g., `int[] arr = new int[5];` → can only hold 5 items).
* An **ArrayList** can **grow** or **shrink** automatically when you add or remove items.
* It belongs to the **Collections Framework** and implements the `List` interface.

👉 Think of it as an **array with superpowers**.

---

## 2. Why was ArrayList introduced?

* Introduced in **Java 1.2** (1998).
* Arrays were too rigid (fixed size).
* Developers wanted a **flexible list** with built-in methods like `add`, `remove`, `get`.
* Later in **Java 5**, **Generics** were added → making `ArrayList` type-safe.

---

## 3. Advantages of ArrayList

* **Dynamic sizing** – no need to worry about fixed size.
* **Easy to use methods** – `add`, `remove`, `contains`, `size`, etc.
* **Fast access** – you can quickly get elements by index.
* **Works with Generics** – ensures **type safety** (e.g., `ArrayList<String>` won’t allow integers).

---

## 4. Comparison: Array vs ArrayList vs LinkedList

| Feature                | Array             | ArrayList             | LinkedList                   |
| ---------------------- | ----------------- | --------------------- | ---------------------------- |
| Size                   | Fixed             | Grows/Shrinks         | Grows/Shrinks                |
| Access by index        | ✅ Fast (O(1))     | ✅ Fast (O(1))         | ❌ Slow (O(n))                |
| Insert/Delete (middle) | ❌ Manual shifting | ❌ Shifting happens    | ✅ Fast (O(1) after locating) |
| Memory                 | Low               | Slight overhead       | High (extra pointers)        |
| Best use case          | Fixed data        | Random access, append | Frequent inserts/deletes     |

---

## 5. Time Complexity (Common Operations)

| Operation         | ArrayList | Array | LinkedList |
| ----------------- | --------- | ----- | ---------- |
| Get/Set (index)   | O(1)      | O(1)  | O(n)       |
| Add at end        | O(1)\*    | N/A   | O(1)       |
| Insert in middle  | O(n)      | O(n)  | O(n)       |
| Remove in middle  | O(n)      | O(n)  | O(n)       |
| Search (contains) | O(n)      | O(n)  | O(n)       |

\*Amortized (because resizing sometimes happens).

---

## 6. Generics in ArrayList

Generics allow you to specify **what type of data** your list will hold.

Example:

```java
// Without generics (old way) – not type-safe
ArrayList names = new ArrayList();
names.add("Mahesh");
names.add(100); // Allowed, but may cause runtime errors

// With generics (better way)
ArrayList<String> namesList = new ArrayList<>();
namesList.add("Mahesh");
namesList.add("Arali");
// namesList.add(100); // ❌ Compile-time error → safer!
```

---

## 7. Example Code (Beginner-Friendly)

```java
import java.util.ArrayList;

public class StudentListDemo {
    public static void main(String[] args) {
        // Create an ArrayList of Strings
        ArrayList<String> students = new ArrayList<>();

        // Add elements
        students.add("Ravi");
        students.add("Priya");
        students.add("Anita");

        // Access elements
        System.out.println("First student: " + students.get(0));

        // Update element
        students.set(1, "Kiran");

        // Remove element
        students.remove("Anita");

        // Iterate over list
        System.out.println("All Students:");
        for (String name : students) {
            System.out.println(name);
        }

        // Check size
        System.out.println("Total students: " + students.size());
    }
}
```

**Output:**

```
First student: Ravi
All Students:
Ravi
Kiran
Total students: 2
```

---

## 8. When should you use ArrayList?

✅ Use it when:

* You need **fast access by index**.
* You mostly **add/remove at the end**.

❌ Avoid when:

* You need frequent insert/delete in the **middle or beginning**. (Use `LinkedList` instead).

---

👉 This should give beginners a **clear mental picture**:

* Array = fixed box
* ArrayList = magic box (can resize)
* LinkedList = chain of boxes


