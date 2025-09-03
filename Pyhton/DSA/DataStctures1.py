# ---------------- Tuple Example ----------------
# A student's basic record stored as a tuple (Immutable and Ordered)
student_record = (101, "Alice", "Computer Science")

# Accessing element - O(1)
print("Student Name:", student_record[1])  # Output: Alice

# Count occurrences - O(n)
print("Count of 'Alice':", student_record.count("Alice"))  # Output: 1

# Find index - O(n)
print("Index of 'Computer Science':", student_record.index("Computer Science"))  # Output: 2


# ---------------- Set Example ----------------
# Set of enrolled student IDs (Unordered, No duplicates)
enrolled_students = {101, 102, 103}

# Add a new student - O(1)
enrolled_students.add(104)

# Remove a student - O(1)
enrolled_students.remove(102)

# Membership test - O(1)
print("Is student 101 enrolled?", 101 in enrolled_students)  # Output: True

# Set union - O(len(s) + len(t))
all_students = enrolled_students.union({105, 106})
print("All students after union:", all_students)


# ---------------- Dictionary Example ----------------
# Dictionary storing student info with student ID as key (Key-Value structure)
student_directory = {
    101: {"name": "Alice", "branch": "Computer Science"},
    102: {"name": "Bob", "branch": "Electronics"},
    103: {"name": "Charlie", "branch": "Mechanical"}
}

# Access student record by ID - O(1)
print("Record for ID 101:", student_directory[101])

# Update record (insert new) - O(1)
student_directory[104] = {"name": "David", "branch": "Civil"}

# Delete a record - O(1)
student_directory.pop(102)

# Search by value (e.g., find students in 'Mechanical') - O(n)
print("Students in Mechanical branch:")
for student_id, info in student_directory.items():
    if info["branch"] == "Mechanical":
        print(f" - Student ID {student_id}: {info['name']}")

# Group students by branch - O(n)
from collections import defaultdict

branch_groups = defaultdict(list)
for student_id, info in student_directory.items():
    branch_groups[info["branch"]].append(info["name"])

print("Grouped by branch:")
for branch, names in branch_groups.items():
    print(f"{branch}: {names}")
