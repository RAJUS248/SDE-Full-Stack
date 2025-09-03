
**Detailed Lesson on `struct` in C**

### What is a `struct` in C?

A `struct` (short for "structure") in C is a user-defined data type that allows grouping of related variables under one name. These variables, known as members, can be of different data types. A `struct` helps organize and manage data logically, especially when dealing with complex data structures.

### Why Use `struct`?

1. **Data Organization:** Simplifies handling related data by grouping them together.
2. **Code Readability:** Improves clarity when managing complex entities like employees, students, or geometric shapes.
3. **Memory Management:** Allocates memory in a contiguous block for all members.
4. **Reusability:** Serves as a blueprint for creating multiple instances of a structure.

### Syntax of `struct`

```c
struct StructName {
    data_type member1;
    data_type member2;
    // Additional members
};
```

### Example: Defining and Using a `struct`

```c
#include <stdio.h>

struct Student {
    int id;
    char name[50];
    float grade;
};

int main() {
    // Creating a variable of type struct Student
    struct Student student1;

    // Setting values
    student1.id = 101;
    strcpy(student1.name, "John Doe");
    student1.grade = 85.5;

    // Accessing values
    printf("ID: %d\n", student1.id);
    printf("Name: %s\n", student1.name);
    printf("Grade: %.2f\n", student1.grade);

    return 0;
}
```

### Memory Allocation for `struct`

When a `struct` variable is declared, memory is allocated in a **contiguous block** for all members. For example:

```c
struct Example {
    int a;       // 4 bytes
    char b;      // 1 byte
    float c;     // 4 bytes
};
```

#### Memory Layout:
- Total size will depend on **padding and alignment** enforced by the compiler. For instance, the above structure may occupy 12 bytes due to padding.

#### Memory Segment:
- `struct` variables are typically allocated in the **stack** for local variables or **heap** when dynamically allocated.

### Creating Variables of `struct`

1. **Direct Declaration:**
   ```c
   struct StructName variableName;
   ```

2. **Array of Structures:**
   ```c
   struct StructName arrayName[size];
   ```

3. **Dynamic Allocation:**
   ```c
   struct StructName* ptr = (struct StructName*)malloc(sizeof(struct StructName));
   ```

### Using `typedef` with `struct`

`typedef` simplifies the usage of structures by providing an alias.

#### Syntax:

```c
typedef struct StructName {
    data_type member1;
    data_type member2;
} AliasName;
```

#### Example:

```c
#include <stdio.h>

typedef struct {
    int id;
    char name[50];
    float grade;
} Student;

int main() {
    Student student1; // Using typedef alias

    student1.id = 102;
    strcpy(student1.name, "Jane Smith");
    student1.grade = 90.0;

    printf("ID: %d\n", student1.id);
    printf("Name: %s\n", student1.name);
    printf("Grade: %.2f\n", student1.grade);

    return 0;
}
```

### Code Examples

#### 1. Setting Values for `struct`

```c
#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p1 = {10, 20}; // Direct initialization

    printf("Point: (%d, %d)\n", p1.x, p1.y);

    return 0;
}
```

#### 2. Dynamically Allocating Memory for `struct`

```c
#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point* p = (struct Point*)malloc(sizeof(struct Point));
    if (p == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Setting values
    p->x = 15;
    p->y = 30;

    printf("Point: (%d, %d)\n", p->x, p->y);

    // Freeing memory
    free(p);

    return 0;
}
```

#### 3. Array of Structures

```c
#include <stdio.h>

struct Employee {
    int id;
    char name[50];
    float salary;
};

int main() {
    struct Employee employees[2] = {
        {1, "Alice", 50000},
        {2, "Bob", 60000}
    };

    for (int i = 0; i < 2; i++) {
        printf("ID: %d, Name: %s, Salary: %.2f\n", employees[i].id, employees[i].name, employees[i].salary);
    }

    return 0;
}
```

### Freeing Dynamically Allocated `struct`

When dynamically allocating memory for a `struct`, always use `free` to release the memory.

#### Example:

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int main() {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    if (node == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    node->data = 42;
    node->next = NULL;

    printf("Node data: %d\n", node->data);

    // Free memory
    free(node);

    return 0;
}
```

### Summary

- **`struct`** groups related variables into a single entity.
- Use **`typedef`** to simplify structure usage.
- Memory for `struct` variables can be allocated statically (stack) or dynamically (heap).
- Always **free dynamically allocated memory** to prevent memory leaks.
- Structures are fundamental for creating complex data types like linked lists, trees, and graphs.

### Notes from algorithms365

#### Websites:
- **Skills Website**: [https://skills.algorithms365.com/](https://skills.algorithms365.com/)  
- **Company Website**: [https://algorithms365.com/](https://algorithms365.com/)  

---

#### Follow & Subscribe on Social Media Platforms:
- **Instagram**: [https://www.instagram.com/algorithms365/](https://www.instagram.com/algorithms365/)  
- **YouTube**: [https://www.youtube.com/@algorithms365](https://www.youtube.com/@algorithms365)  
- **Facebook**: [https://www.facebook.com/algorithms365](https://www.facebook.com/algorithms365)  
- **Twitter (X)**: [https://x.com/algorithms365](https://x.com/algorithms365)  
- **LinkedIn**: [https://www.linkedin.com/company/algorithms365-technologies-llp/](https://www.linkedin.com/company/algorithms365-technologies-llp/)  

---

## Join Our Communities:
- **WhatsApp**: [https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht](https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht)  
- **Telegram**: [https://t.me/+hyVHX
