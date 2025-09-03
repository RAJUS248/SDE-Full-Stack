# Doubly Linked List 

This guide explains **Doubly Linked Lists (DLLs)** in a fun, relatable, and student-friendly way. It uses the exact code and variable names from the attached `.py` file, maintaining its structure and enhancing the comments for clarity.

---

## 📘 What is a Doubly Linked List?
A **Doubly Linked List** is a linear data structure where each node links to both its previous and next neighbors.

> 🎯 Real-World Analogy: Think of your browser history—go back to the previous page or forward to the next. That's a DLL in action!

---

## 🧱 Node Structure
```python
class Node:
    def __init__(self, data):
        self.data = data      # Value to store in the node
        self.prev = None      # Pointer to the previous node
        self.next = None      # Pointer to the next node
```

---

## 🛠️ DoublyLinkedList Operations 
```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head points to the first node in the list

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head  # New node's next is the old head
        self.head.prev = new_node  # Old head's prev is the new node
        self.head = new_node       # Update head to the new node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def insert_at_position(self, data, target_position):
        print(f"\nInsert at position {target_position} value {data}")
        if target_position <= 0:
            print("Invalid position")
            return

        if self.head is None and target_position != 1:
            print("Invalid position")
            return

        if target_position == 1:
            self.insert_at_beginning(data)
            return

        current_position = 1
        current_node = self.head
        while current_node is not None and current_position < target_position - 1:
            current_position += 1
            current_node = current_node.next

        if current_node is None:
            print("Invalid position")
            return

        new_node = Node(data)

        if current_node.next is not None:
            current_node.next.prev = new_node  # Update next node's prev
            new_node.next = current_node.next  # Link to the next node

        current_node.next = new_node  # Link current to new
        new_node.prev = current_node  # Link new to current

    def delete_at_beginning(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None  # Remove back reference

    def delete_at_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        last_node = self.head
        while last_node.next.next is not None:
            last_node = last_node.next

        last_node.next = None

    def delete_at_position(self, target_position):
        if self.head is None:
            print("List is empty")
            return

        if target_position <= 0:
            print(f"Invalid target position {target_position}")
            return

        if self.head.next is None:
            self.head = None
            return

        to_be_deleted = self.head
        current_position = 1

        while current_position < target_position and to_be_deleted is not None:
            current_position += 1
            to_be_deleted = to_be_deleted.next

        if to_be_deleted is None:
            print(f"Target position {target_position} is invalid")
            return

        if to_be_deleted.next is None:
            to_be_deleted.prev.next = None
            return

        to_be_deleted.next.prev = to_be_deleted.prev
        to_be_deleted.prev.next = to_be_deleted.next

    def search(self, key):
        if self.head is None:
            print("Key is not found in the list")
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                print("Key is found in the list")
                return
            current_node = current_node.next

        print("Key is not found in the list")

    def print_all_nodes(self):
        print("\nPrinting all the nodes in the doubly linked list\n")
        if self.head is None:
            print("List is empty")
            return

        current_node = self.head
        while current_node is not None:
            print(f"<-- {current_node.data} -->", end=" ")
            current_node = current_node.next
        print()
```

---

## ✅ Advantages vs Other Structures
| Feature                   | Array     | Singly Linked List | Doubly Linked List |
|--------------------------|-----------|---------------------|--------------------|
| Dynamic Size             | ❌         | ✅                   | ✅                 |
| Direct Index Access      | ✅ (O(1)) | ❌ (O(n))            | ❌ (O(n))          |
| Forward/Backward Traverse| ❌         | ❌                   | ✅                 |
| Efficient Insert/Delete  | ❌         | ✅                   | ✅                 |
| Memory Usage             | ✅         | ✅                   | ❌ (extra pointer) |

---

## ⏱️ Time Complexity Comparison
| Operation              | Time Complexity |
|------------------------|-----------------|
| Insert at Beginning    | O(1)            |
| Insert at End          | O(n)            |
| Insert at Position     | O(n)            |
| Delete at Beginning    | O(1)            |
| Delete at End          | O(n)            |
| Delete at Position     | O(n)            |
| Search                 | O(n)            |

---

## 💡 Real-World Use Cases
- Web browser forward/back buttons
- Undo-redo operations in editors
- Media playlists
- Navigation systems with backtracking

---

## 🎓 Summary
Doubly Linked Lists are:
- Flexible with two-way traversal
- Easy to insert/delete from both ends
- A bit heavier on memory

But totally worth it when direction and flexibility matter. 🔄

Happy coding! 🚀

