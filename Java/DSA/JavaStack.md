
# 🗃️ Stack Implementation in Java

## 📌 What is a Stack?

A **Stack** is a linear data structure that follows the **LIFO** (Last In, First Out) principle:
- The last element added is the first to be removed.
- Think of a stack of plates — you remove the top plate first.

---

## 🔧 Core Stack Operations

| Operation | Description                     |
|----------|---------------------------------|
| `push`   | Adds an item to the top         |
| `pop`    | Removes the top item            |
| `peek`   | Returns the top item without removing it |
| `isEmpty`| Checks if the stack is empty    |
| `size`   | Returns the number of items     |

---

## 🧪 Implementation Methods

There are **two main ways** to implement a stack in Java:

### 1️⃣ Using Array

```java
class StackArray {
    private int maxSize;
    private int[] stackArray;
    private int top;

    public StackArray(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1; // stack is empty
    }

    public void push(int value) {
        if (top == maxSize - 1) {
            System.out.println("Stack is full");
            return;
        }
        stackArray[++top] = value;
        // top = top + 1
        // stackArray[top] = value;
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty");
            return -1;
        }
        return stackArray[top--];
        // int returnValue = stackArray[top]
        // top = top - 1
        // return returnValue
    }

    public int peek() {
        if (isEmpty()) return -1;
        return stackArray[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public int size() {
        return top + 1;
    }
}
```

### ✅ Pros:
- Fast access (constant time array indexing).
- Simple and easy to implement.

### ❌ Cons:
- Fixed size; not dynamic.

---

### 2️⃣ Using Linked List

```java
class StackLinkedList {
    private class Node {
        int data;
        Node next;
        Node(int data) { this.data = data; }
    }

    private Node top = null;

    public void push(int data) {
        Node newNode = new Node(data);
        newNode.next = top;
        top = newNode;
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty");
            return -1;
        }
        int value = top.data;
        top = top.next;
        return value;
    }

    public int peek() {
        if (isEmpty()) return -1;
        return top.data;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public int size() {
        int count = 0;
        Node current = top;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }
}
```

### ✅ Pros:
- Dynamically resizable.
- No need to define initial capacity.

### ❌ Cons:
- Slightly more memory due to node references.

---

### 3️⃣ Using Java Built-in `Stack` Class

```java
import java.util.Stack;

public class BuiltInStackExample {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(10);
        stack.push(20);
        System.out.println("Top: " + stack.peek());
        stack.pop();
        System.out.println("After pop, top: " + stack.peek());
    }
}
```

- Java's built-in `Stack` class is a part of the `java.util` package.
- Internally it uses **Vector**, which is synchronized.

---

## ⚖️ Comparison Table

| Feature             | Array Stack | LinkedList Stack | Java Built-in Stack |
|---------------------|-------------|------------------|---------------------|
| Dynamic resizing    | ❌ No       | ✅ Yes           | ✅ Yes              |
| Memory efficient    | ✅ Yes      | ❌ Overhead      | ❌ Overhead         |
| Easy to implement   | ✅ Yes      | ✅ Yes           | ✅ Easiest          |
| Performance         | ✅ Fast     | ✅ Moderate      | ⚠️ Slower (Vector overhead) |
| Synchronized        | ❌ No       | ❌ No            | ✅ Yes              |

---

## ⏱️ Time Complexity

| Operation | Time Complexity |
|----------|-----------------|
| push     | O(1)            |
| pop      | O(1)            |
| peek     | O(1)            |
| isEmpty  | O(1)            |
| size     | O(1) (Array), O(n) (Linked List) |

---

## 🌍 Real-World Applications

1. **Undo Mechanism** – Editors and IDEs.
2. **Backtracking** – Path finding, puzzles (like Sudoku).
3. **Function Call Management** – Recursion.
4. **Syntax Parsing** – Compilers and interpreters.
5. **Expression Evaluation** – Infix to postfix, postfix evaluation.

---

## ✅ Summary

- Stack is a fundamental LIFO structure.
- Choose implementation based on **requirements**:
  - Use **Array** if you know the size and want performance.
  - Use **Linked List** for dynamic, flexible storage.
  - Use **Java’s Stack class** for simplicity and built-in sync.

