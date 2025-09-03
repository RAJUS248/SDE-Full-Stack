
# Python Data Structures: Tuple, Set, and Dictionary

These notes explain three important Python data structures: **Tuple**, **Set**, and **Dictionary**, along with their syntax, use cases, how they store data in memory, mutability, performance aspects, and internal implementation.

---

## 📌 Tuple

### ✅ Syntax:
```python
# A student's basic record stored as a tuple
student_record = (101, "Alice", "Computer Science")
```

### 🔍 Characteristics
- Immutable (cannot change after creation)
- Ordered
- Allows duplicates

### 🧠 Memory and Mutability
- Stored in the heap memory.
- Once created, contents cannot be changed (immutable).
- Tuples are more memory-efficient than lists.
- Being immutable, they are hashable and can be used as dictionary keys.

### 📍 Where It’s Used:
- Return multiple values from a function.
- Store fixed-size records like (latitude, longitude), or (id, name, branch).
- Used as keys in dictionaries (only if elements are also immutable).

### ⚙️ Operations with Time Complexity:
```python
# Accessing element - O(1)
print(student_record[1])  # Output: Alice

# Count occurrences - O(n)
print(student_record.count("Alice"))  # Output: 1

# Find index - O(n)
print(student_record.index("Computer Science"))  # Output: 2
```

### ✅ Advantages
- Less memory compared to lists.
- Safer for fixed data.

### ❌ Disadvantages
- Cannot be modified.

---

## 📌 Set

### ✅ Syntax:
```python
# Set of enrolled student IDs
enrolled_students = {101, 102, 103}
```

### 🔍 Characteristics
- Unordered
- Mutable
- No duplicates allowed

### 🧠 Memory and Mutability
- Stored in heap memory.
- Internally uses a hash table.
- Mutable: elements can be added or removed.
- Only hashable (immutable) objects can be added.

### 📍 Where It’s Used:
- Removing duplicates from a collection.
- Set operations like union, intersection, difference.
- Fast membership testing.

### ⚙️ Operations with Time Complexity:
```python
# Add a new student - O(1)
enrolled_students.add(104)

# Remove a student - O(1)
enrolled_students.remove(102)

# Membership test - O(1)
print(101 in enrolled_students)  # Output: True

# Set union - O(len(s) + len(t))
all_students = enrolled_students.union({105, 106})
print(all_students)  # Output: {101, 103, 104, 105, 106}

enrolled_student_names = { "Mahesh", "Mahesh", "Mahesh", "Santosh", "Sushil", "Amit", "Mahesh Bisur", "Sangeeta"}
paid_course_student_names = { "Santosh", "Sushil", "Vidya"}

common_students = enrolled_student_names & paid_course_student_names
print(common_students)

combined_students = enrolled_student_names | paid_course_student_names
print(combined_students)

unpaid_students = enrolled_student_names -  paid_course_student_names 
print(unpaid_students)

paid_but_not_enrolled = paid_course_student_names - enrolled_student_names
print(paid_but_not_enrolled)

call_list = paid_course_student_names ^ enrolled_student_names
print(call_list)
```

### ✅ Advantages
- High performance for membership testing.
- Useful for mathematical set operations.

### ❌ Disadvantages
- No indexing.
- No duplicate elements.

---

## 📌 Dictionary (dict)

### ✅ Syntax:
```python
# Dictionary storing student info with student ID as key
student_directory = {
    101: {"name": "Alice", "branch": "Computer Science"},
    102: {"name": "Bob", "branch": "Electronics"},
    103: {"name": "Charlie", "branch": "Mechanical"}
}
```

### 🔍 Characteristics
- Key-value pair
- Unordered (insertion ordered in Python 3.7+)
- Mutable

### 🧠 Memory and Mutability
- Stored in heap memory.
- Uses a hash table internally for key lookups.
- Mutable: keys can be added, updated, or deleted.
- Keys must be hashable (immutable).

### 🔐 Hashing, Hash Lookups & Collisions
- Keys are hashed using a hash function to index into an internal array.
- Hash collisions are handled using open addressing or chaining.
- Fast average time complexity for insert, delete, and lookup is O(1).

### 📍 Where It’s Used:
- Represent structured data (like JSON)
- Caching/memoization
- Fast lookup tables (e.g., student database, phone book)

### ⚙️ Operations with Time Complexity:
```python
# Access student record by ID - O(1)
print(student_directory[101])

# Update record - O(1)
student_directory[104] = {"name": "David", "branch": "Civil"}

# Delete record - O(1)
student_directory.pop(102)

# Search by value (O(n))
for student_id, info in student_directory.items():
    if info["branch"] == "Mechanical":
        print(f"Student ID {student_id} is in Mechanical")

# Group students by branch
from collections import defaultdict
branch_groups = defaultdict(list)
for student_id, info in student_directory.items():
    branch_groups[info["branch"]].append(info["name"])
print(branch_groups)
```

### ✅ Advantages
- Fast access by key.
- Flexible to store structured and nested data.

### ❌ Disadvantages
- Keys must be unique.
- Memory overhead due to hashing.

---

## 🆚 Set vs Dictionary

| Feature               | Set                        | Dictionary                                |
|-----------------------|----------------------------|--------------------------------------------|
| Stores                | Only values                | Key-value pairs                            |
| Duplicate values      | Not allowed                | Keys must be unique, values can repeat     |
| Internal Structure    | Hash table (keys only)     | Hash table (keys and values)               |
| Syntax                | `{val1, val2}`             | `{key1: val1, key2: val2}`                 |
| Lookup                | By value                   | By key                                     |

---

## 📊 Time Complexity Comparison Table

| Operation         | List/Array | Tuple | Set    | Dictionary |
|------------------|------------|-------|--------|------------|
| Access element   | O(1)       | O(1)  | -      | O(1)       |
| Search element   | O(n)       | O(n)  | O(1)   | O(1)       |
| Insert element   | O(n)       | -     | O(1)   | O(1)       |
| Delete element   | O(n)       | -     | O(1)   | O(1)       |
| Iterate all      | O(n)       | O(n)  | O(n)   | O(n)       |

> ⚠️ Note: The average-case time complexities assume hash functions distribute values well and that there are no collisions.

---

## 🧠 Summary

- **Tuple** is best for fixed-size, immutable data like student records (id, name, branch).
- **Set** is ideal for fast membership testing, such as checking if a student is enrolled.
- **Dictionary** is powerful for organizing structured data, such as student databases with IDs as keys.

These structures are widely used in **web development**, **data processing**, **machine learning**, and **system design**.
