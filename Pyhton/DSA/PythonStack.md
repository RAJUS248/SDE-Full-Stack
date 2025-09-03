
# 🧱 Stack Implementation Using Linked List in Python

This document provides a complete and well-commented implementation of a **Stack** using a **custom singly linked list** in Python. It also includes usage examples, time complexity, and real-world use cases.

---

## 📚 What is a Stack?

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle.

- **LIFO** means the last item added is the first one to be removed.
- Think of it like a pile of books or plates—only the top can be accessed directly.

---

## 🔁 Operations Supported

| Operation     | Description                                       | Time Complexity |
|---------------|---------------------------------------------------|------------------|
| `push(item)`  | Adds an element to the top of the stack           | O(1)             |
| `pop()`       | Removes and returns the top element               | O(1)             |
| `peek()`      | Returns the top element without removing it       | O(1)             |
| `is_empty()`  | Checks if the stack has no elements               | O(1)             |
| `size()`      | Returns the number of elements in the stack       | O(1)             |
| `display()`   | Displays the entire stack from top to bottom      | O(n)             |

---

## 🧠 Real-World Applications

- **Undo/Redo** in text editors
- **Function call stack** in programming languages
- **Expression parsing** (e.g., postfix evaluation)
- **Browser history navigation**
- **Backtracking algorithms** (e.g., maze solving, DFS)

---

## 🧾 Complete Python Code

```python
class Node:
    """
    Node class for linked list-based stack.

    Attributes:
        data: The value stored in the node.
        next: Reference to the next node in the stack.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    Stack implementation using a singly linked list.
    Follows Last-In-First-Out (LIFO) principle.
    """
    def __init__(self):
        self.top = None   # Top of the stack
        self.count = 0    # Number of elements in the stack

    def push(self, item):
        """
        Pushes an item onto the stack.

        Time Complexity: O(1)
        """
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        """
        Removes and returns the top item of the stack.

        Time Complexity: O(1)
        """
        if self.is_empty():
            return "Stack Underflow!"
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped

    def peek(self):
        """
        Returns the top item without removing it.

        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        """
        Checks whether the stack is empty.

        Time Complexity: O(1)
        """
        return self.top is None

    def size(self):
        """
        Returns the number of items in the stack.

        Time Complexity: O(1)
        """
        return self.count

    def display(self):
        """
        Prints the contents of the stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty")
            return

        current = self.top
        print("Stack (top -> bottom):")
        while current:
            print(current.data)
            current = current.next


# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(100)
    stack.push(200)
    stack.push(300)

    stack.display()
    print("Top element:", stack.peek())
    print("Popped:", stack.pop())
    stack.display()
    print("Stack size:", stack.size())
    print("Is stack empty?", stack.is_empty())
```

---

## ✅ Summary Notes

- The stack is implemented using a **custom linked list**, not Python's built-in list.
- It allows for **constant-time operations** for push/pop/peek.
- Useful for understanding how memory and pointers work under the hood.
- Excellent for applications that require LIFO ordering.

---

Let me know if you want a version for **Queue using Linked List**, or if you'd like to **turn this into a PDF** or **Jupyter notebook**!
