# C Programming Naming Conventions (Industry Standard)

Consistent naming conventions in C programming improve code readability, maintainability, and collaboration. These conventions are based on practices seen in real-world projects (e.g., Linux kernel, embedded systems, and legacy enterprise systems). While C doesn’t have a single universal standard, the conventions vary slightly across domains. This guide synthesizes best practices used in production-grade systems.

---

## 1. Variable Names

* Use **lowercase** or **lowercase\_with\_underscores**
* Short variables (like `i`, `j`) are acceptable for loop counters
* For clarity, use more descriptive names in broader scopes

**Example:**

```c
int student_age;
float total_marks;
int i; // loop counter
```

---

## 2. Function Names

* Use **lowercase\_with\_underscores** (most common)
* Some codebases (e.g., Windows API) use **PascalCase**, but this is rare in open-source C
* Functions should be **verbs or verb phrases**

**Example:**

```c
void calculate_total();
int get_student_score();
```

---

## 3. Constant Names (Macros)

* Use **ALL\_UPPERCASE** with underscores

**Example:**

```c
#define MAX_STUDENTS 100
#define PI 3.14159
```

---

## 4. Global Variable Names

* Prefix with module or subsystem name to avoid collisions
* May use **g\_** prefix in some legacy systems

**Example:**

```c
int student_db_count;
// or in legacy code:
int g_total_students;
```

---

## 5. Static Variable Names

* May use `s_` prefix to indicate static/internal linkage in some systems

**Example:**

```c
static int s_internal_counter;
```

---

## 6. Struct and Union Names

* Use **PascalCase** or **snake\_case** (project-dependent)
* For typedefs, PascalCase is preferred

**Example:**

```c
typedef struct Student {
    int id;
    char name[50];
} Student;
```

---

## 7. Enum Names

* Enum type: **PascalCase** or **snake\_case**
* Enum constants: **ALL\_UPPERCASE** with prefix

**Example:**

```c
typedef enum Status {
    STATUS_PENDING,
    STATUS_APPROVED,
    STATUS_REJECTED
} Status;
```

---

## 8. Pointer Variables

* Use descriptive names
* May include `_ptr` suffix or type-based prefixes

**Example:**

```c
char *name;
char *name_ptr; // if clarity is needed
```

---

## Complete Example

```c
#include <stdio.h>

#define MAX_STUDENTS 100

typedef struct Student {
    int id;
    char name[50];
} Student;

int student_db_count = 0;

void register_student(Student *student_ptr) {
    printf("Registering student: %s\n", student_ptr->name);
    student_db_count++;
}

int main() {
    Student s1 = {1, "Alice"};
    register_student(&s1);
    return 0;
}
```

---

## Summary Table

| Element          | Convention              | Example                       |
| ---------------- | ----------------------- | ----------------------------- |
| Variable         | lowercase / snake\_case | `student_age`, `i`            |
| Function         | snake\_case             | `calculate_total()`           |
| Constant (Macro) | ALL\_UPPERCASE          | `MAX_STUDENTS`                |
| Global Variable  | module\_prefix or g\_   | `student_db_count`, `g_total` |
| Static Variable  | s\_ prefix (optional)   | `s_internal_counter`          |
| Struct Name      | PascalCase              | `Student`                     |
| Enum Name        | PascalCase/UPPER        | `Status`, `STATUS_PENDING`    |
| Pointer Variable | use `_ptr` optional     | `name_ptr`                    |

---

## Tips for Students

* Study and follow naming conventions used in open-source projects (Linux kernel, Redis, SQLite).
* Stick to your team/project’s style consistently.
* Avoid overly short or cryptic names.
* Use comments to describe logic, not names.
* When in doubt, prioritize clarity and simplicity.
