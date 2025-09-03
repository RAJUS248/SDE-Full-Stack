# Singly Linked List in Python - Enhanced Notes

This document includes a **professional and educational version** of Singly Linked List (SLL) implementation in Python. It combines clean code with rich context: **real-world analogies, industry relevance**, and **detailed comments** to ensure both learners and professionals benefit.

---

## 🚀 What is a Singly Linked List?

A **Singly Linked List** is a **linear dynamic data structure** made of nodes, where each node contains:
- `data`: The actual information
- `next`: Reference to the next node in the list

Only the first node (head) is accessible directly. All navigation is done sequentially.

### 🏗️ Real-World Analogy:
Think of a **treasure map** where each clue (node) points to the location of the next clue. You can’t jump to the end—you have to follow the clues one by one.

### 🧠 Why is it useful in the industry?
- **Memory-efficient for dynamic data**: Used when data size is not known beforehand.
- **Web Browsers**: Back and forward button navigation uses linked structures.
- **Music/Playlist Apps**: Playlists where each song leads to the next.
- **Operating Systems**: For task scheduling (ready queue, etc.).

---

## 🧱 Node Structure
```python
class Node:
    """
    A Node in a singly linked list that contains data and reference to the next node.
    """
    def __init__(self, data):
        self.data = data  # The value or payload of the node
        self.next = None  # Pointer to the next node in the list
```

---

## 🧰 SinglyLinkedList Class - Core API
```python
class SinglyLinkedList:
    """
    Implements a singly linked list with operations to manipulate and access data.
    """
    def __init__(self):
        self.head = None  # Head points to the first node in the list
```

---

## 🔧 Core Operations 

### 1. Insert at Beginning
```python
def insert_at_beginning(self, data):
    """
    Inserts a node at the start of the list.
    If the list is empty, new node becomes the head.
    Otherwise, new node points to current head and becomes the new head.
    """
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### 2. Insert at End
```python
def insert_at_end(self, data):
    """
    Appends a node at the end of the list.
    Handles empty list, single-node, and multi-node cases.
    """
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    current_node = self.head
    while current_node.next is not None:
        current_node = current_node.next

    current_node.next = new_node
```

### 3. Insert at a Specific Position
```python
def insert_at_position(self, data, insert_position):
    """
    Inserts a node at a given 1-based index.
    If position is invalid, prints a message.
    """
    if insert_position <= 0:
        print("Invalid position")
        return

    if insert_position == 1:
        self.insert_at_beginning(data)
        return

    current_node = self.head
    current_position = 1

    while current_position < insert_position - 1 and current_node is not None:
        current_position += 1
        current_node = current_node.next

    if current_node is None:
        print("Invalid position, fewer nodes in list")
        return

    new_node = Node(data)
    new_node.next = current_node.next
    current_node.next = new_node
```

### 4. Delete at Beginning
```python
def delete_at_beginning(self):
    """
    Removes the first node in the list by updating head pointer.
    Handles empty and single-node list cases.
    """
    if self.head is None:
        return

    self.head = self.head.next
```

### 5. Delete at End
```python
def delete_at_end(self):
    """
    Removes the last node of the list by traversing to the second-last node.
    Edge cases: empty list and single-node list.
    """
    if self.head is None:
        return

    if self.head.next is None:
        self.head = None
        return

    current_node = self.head
    while current_node.next.next is not None:
        current_node = current_node.next

    current_node.next = None
```

### 6. Delete at a Specific Position
```python
def delete_at_position(self, delete_position):
    """
    Deletes the node at the given 1-based position.
    Verifies the position and edge conditions.
    """
    if delete_position <= 0:
        print("Invalid position")
        return

    if delete_position == 1:
        self.delete_at_beginning()
        return

    current_node = self.head
    current_position = 1

    while current_position < delete_position - 1 and current_node is not None:
        current_position += 1
        current_node = current_node.next

    if current_node is None or current_node.next is None:
        print("Invalid position, fewer nodes in list")
        return

    current_node.next = current_node.next.next
```

### 7. Search for a Key
```python
def search(self, key):
    """
    Searches the list for the specified key.
    If found, prints confirmation. Otherwise, says not found.
    """
    if self.head is None:
        print("List is empty")
        return

    current_node = self.head
    while current_node is not None:
        if key == current_node.data:
            print("Key found")
            return
        current_node = current_node.next

    print("Key not found")
```

### 8. Display List
```python
def print_list(self):
    """
    Prints the entire linked list in human-readable format.
    """
    if self.head is None:
        print("List is empty")
        return

    current_node = self.head
    while current_node is not None:
        print(str(current_node.data) + " --> ", end='')
        current_node = current_node.next
    print("None")
```

---

## 🧪 Driver Code Examples
```python
def insert_delete_at_given_position(list):
    """
    Demonstrates inserting and deleting at specific positions.
    Shows valid and invalid examples.
    """
    list.insert_at_position(10, -1)
    list.delete_at_position(-1)

    list.insert_at_position(10, 1)
    list.delete_at_position(1)

    list.insert_at_end(10)
    list.insert_at_end(20)
    list.insert_at_end(30)

    list.insert_at_position(15, 2)
    list.insert_at_position(40, 4)
    list.insert_at_position(100, 10)
```

---

## 📌 Tips
- Always validate positions
- Handle edge cases (empty list, single-node list)
- Use helper functions for testing and debugging

---

## 📍 Conclusion
Singly Linked Lists are powerful tools for dynamic memory usage, making them highly useful in **real-time systems**, **compilers**, **network packet routing**, and more.

For source and community:
- [Algorithms365 YouTube](https://www.youtube.com/@algorithms365)
- [MIT License](https://opensource.org/licenses/MIT)

Stay connected with **Algorithms365** for more industry-grade implementations!

