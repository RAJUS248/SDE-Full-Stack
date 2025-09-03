# 🧱 Queue Implementations in Python

This document provides a comprehensive guide to implementing a **Queue** in Python using various methods. Each method is explained with pros and cons, and is implemented with clean, well-commented code.

---

## 📚 What is a Queue?

A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle.

- **FIFO** means the first item added is the first one to be removed.
- Think of it like a line at a ticket counter—the person who arrives first gets served first.

---

## ⚙️ Ways to Implement a Queue in Python

### 1. Using a List

#### ✅ Pros
- Simple and intuitive for small use cases
- Built-in methods like `append()` and `pop(0)`

#### ❌ Cons
- `pop(0)` is O(n) due to element shifting

```python
class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow!"
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)
```

---

### 2. Using `collections.deque`

#### ✅ Pros
- Efficient O(1) for both enqueue and dequeue
- Thread-safe

#### ❌ Cons
- Requires importing from `collections`

```python
from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow!"
        return self.queue.popleft()

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", list(self.queue))
```

---

### 3. Using a Custom Linked List

#### ✅ Pros
- No need to shift elements
- Good for learning pointer-based data structures

#### ❌ Cons
- Slightly more code to manage nodes and pointers

```python
# Node class representing each element in the queue
class Node:
    def __init__(self, value):
        self.value = value      # Holds the data
        self.next = None        # Points to the next node in the queue


# Queue implementation using a linked list
class QueueLinkedList:
    def __init__(self):
        self.front_node = None   # Points to the front node of the queue
        self.rear_node = None    # Points to the rear node of the queue
        self.element_count = 0   # Tracks number of elements in the queue

    # Add an element to the end (rear) of the queue
    def enqueue(self, item):
        new_node = Node(item)    # Create a new node with the given item

        if self.rear_node:
            self.rear_node.next = new_node  # Link the current rear node to the new node

        self.rear_node = new_node  # Update rear to point to the new node

        # If the queue was empty, set front to the new node as well
        if not self.front_node:
            self.front_node = new_node

        self.element_count += 1   # Increment element count

    # Remove and return the front element of the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow!"  # Nothing to dequeue

        removed_value = self.front_node.value  # Store value to return
        self.front_node = self.front_node.next  # Move front to the next node

        # If the queue becomes empty after removal, reset rear to None
        if not self.front_node:
            self.rear_node = None

        self.element_count -= 1   # Decrement element count
        return removed_value

    # View the front element without removing it
    def peek(self):
        return self.front_node.value if not self.is_empty() else None

    # Check if the queue is empty
    def is_empty(self):
        return self.front_node is None

    # Return the number of elements in the queue
    def size(self):
        return self.element_count

    # Display the elements in the queue from front to rear
    def display(self):
        current_node = self.front_node
        print("Queue (front -> rear):", end=" ")
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()

```

---

## 🧠 Real-World Applications

- **Print queues**
- **Task scheduling**
- **CPU job scheduling**
- **Customer service lines**
- **Breadth-First Search (BFS) in graphs**

---

## 🚀 Example Usage

```python
if __name__ == "__main__":
    print("Using Linked List:")
    q1 = QueueLinkedList()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.display()
    print("Dequeued:", q1.dequeue())
    q1.display()

    print("\nUsing List:")
    q2 = QueueList()
    q2.enqueue('A')
    q2.enqueue('B')
    q2.display()
    print("Dequeued:", q2.dequeue())
    q2.display()

    print("\nUsing Deque:")
    q3 = QueueDeque()
    q3.enqueue('X')
    q3.enqueue('Y')
    q3.display()
    print("Dequeued:", q3.dequeue())
    q3.display()
```

---

## ✅ Summary

| Method               | Time Complexity (Enqueue/Dequeue) | Best For                               |
|----------------------|------------------------------------|-----------------------------------------|
| Python List          | O(1) / O(n)                        | Small data and simplicity               |
| `collections.deque`  | O(1) / O(1)                        | Performance-critical applications       |
| Custom Linked List   | O(1) / O(1)                        | Learning, flexibility, interview prep   |

Choose the one that fits your needs best!
