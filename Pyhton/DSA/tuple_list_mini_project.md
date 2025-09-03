
# 📘 Tuples in Python: Real-World Examples and Mini Project

## ✅ Real-World Examples of Tuples

1. **GPS Coordinates**
   ```python
   location = (12.9352, 77.6101)  # latitude, longitude
   ```

2. **Database Records**
   ```python
   employee = (101, "Alice", "Software Engineer")
   ```

3. **RGB Color Values**
   ```python
   red_color = (255, 0, 0)  # RGB tuple
   ```

4. **Chess Board Moves**
   ```python
   move = ("E2", "E4")  # from, to
   ```

5. **Student Marksheet Entries**
   ```python
   student_data = ("Alice", 85, 90, 92)  # Name and marks
   ```

---

## 🧪 Mini Project: Student Records System Using Tuples

### 🎯 Description:
This project demonstrates how to use tuples to store and manage student records. Each student record is a tuple of the form:
```python
(student_id, name, branch, year)
```

### Features:
- Add a new student
- Display all students
- Search for a student by ID

### 🧾 Code (under 50 lines):
```python
# Student Records System using Tuples

student_db = []

def add_student():
    student_id = int(input("Enter ID: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    year = int(input("Enter year: "))
    record = (student_id, name, branch, year)
    student_db.append(record)
    print("✅ Student added!")

def display_all():
    if not student_db:
        print("No records available.")
    for student in student_db:
        print(f"ID: {student[0]}, Name: {student[1]}, Branch: {student[2]}, Year: {student[3]}")

def search_by_id():
    search_id = int(input("Enter ID to search: "))
    found = False
    for student in student_db:
        if student[0] == search_id:
            print(f"✅ Found: {student}")
            found = True
            break
    if not found:
        print("❌ Student not found.")

def main():
    while True:
        print("\n1. Add Student  2. Display All  3. Search by ID  4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_all()
        elif choice == '3':
            search_by_id()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
```

### 🔍 Why Tuples?
- Immutability ensures records aren’t accidentally altered.
- Lightweight and faster than lists for fixed structured data.
- Can be used as dictionary keys for enhanced searchability in advanced versions.
