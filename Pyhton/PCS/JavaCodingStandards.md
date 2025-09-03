# Java Code Naming Conventions (Industry Standard)

Naming conventions make code readable, maintainable, and consistent across teams and projects. These are guidelines widely adopted in professional Java development, especially important for students to learn early.

---

## 1. Class Names

* Use **PascalCase** (UpperCamelCase)
* Should be **nouns**, representing objects/entities

**Example:**

```java
public class StudentRecord {
    // fields and methods
}
```

---

## 2. Interface Names

* Use **PascalCase**
* Describe a capability or role, often using **adjectives** or **abstract nouns**

**Example:**

```java
public interface Drivable {
    void drive();
}
```

---

## 3. Method Names

* Use **camelCase**
* Should be **verbs or verb phrases**

**Example:**

```java
public void calculateSalary() {
    // logic here
}
```

---

## 4. Variable Names

* Use **camelCase**
* Should be **nouns**, representing data

**Example:**

```java
int studentAge;
String employeeName;
```

---

## 5. Constant Names

* Use **ALL\_UPPERCASE** with underscores
* Defined using `static final`

**Example:**

```java
public static final int MAX_LOGIN_ATTEMPTS = 3;
```

---

## 6. Package Names

* Use **all lowercase**
* Follow reverse domain naming convention: `com.companyname.project`

**Example:**

```java
package com.college.records;
```

---

## 7. Generic Type Parameters

* Use **single uppercase letters**

  * `T` = Type, `E` = Element, `K` = Key, `V` = Value, `N` = Number

**Example:**

```java
public class Box<T> {
    private T item;
}
```

---

## 8. Enum Names

* Use **PascalCase** for the enum name
* Enum constants in **ALL\_UPPERCASE**

**Example:**

```java
public enum Status {
    PENDING, APPROVED, REJECTED;
}
```

---

## 9. Annotation Names

* Use **PascalCase**, like class names

**Example:**

```java
@interface MyCustomAnnotation {
}
```

---

## Complete Example

```java
package com.university.coursemanagement;

public class CourseManager {

    private String courseName;
    private int maxStudents;
    public static final int MAX_COURSE_DURATION = 180;

    public CourseManager(String courseName, int maxStudents) {
        this.courseName = courseName;
        this.maxStudents = maxStudents;
    }

    public void registerStudent(String studentName) {
        // logic
    }

    public String getCourseName() {
        return courseName;
    }
}
```

---

## Summary Table

| Element      | Convention       | Example                     |
| ------------ | ---------------- | --------------------------- |
| Class        | PascalCase       | `StudentProfile`            |
| Interface    | PascalCase       | `Serializable`              |
| Method       | camelCase        | `calculateInterest()`       |
| Variable     | camelCase        | `userName`                  |
| Constant     | ALL\_UPPERCASE   | `PI_VALUE`                  |
| Package      | lowercase        | `com.example.utility`       |
| Generic Type | Single Capital   | `T`, `K`, `V`               |
| Enum         | PascalCase/UPPER | `UserType { ADMIN, GUEST }` |
| Annotation   | PascalCase       | `@MyAnnotation`             |

---

## Tips for Students

* Be consistent in your naming.
* Use meaningful names (avoid shortcuts like `sName` — use `studentName`).
* Avoid abbreviations unless they're very common (`URL`, `ID`).
* Always follow team or project-specific guidelines when applicable.
