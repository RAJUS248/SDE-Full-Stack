# Circular Linked List in Java - Enhanced Notes

This guide explains the **Circular Linked List (CLL)** in Java using clean, commented code and industry-oriented explanations. It follows the same style as the Singly and Doubly Linked List notes, aiming to help both learners and professionals.

---

## 🚀 What is a Circular Linked List?

A **Circular Linked List** is a linked list in which:
- The last node's `next` points back to the `head`
- There is **no null** at the end of the list
- Can be singly or doubly linked

Traversal continues until you circle back to the head.

### 🏗️ Real-World Analogy:
Think of a **merry-go-round** where each person (node) is linked to the next, and the last one points to the first — a continuous loop.

### 🧠 Industry Use Cases:
- **Circular queues**
- **Round-robin schedulers**
- **Gaming systems** (players turn-based loop)
- **Buffer management**

---

## 🧱 Node Class
```java
/**
 * Represents a node in a circular linked list.
 */
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
```

---

## 🧰 CircularLinkedList Class - Core API
```java
/**
 * Implements a Circular Linked List with essential operations.
 */
public class CircularLinkedList {
    Node head;

    public CircularLinkedList() {
        this.head = null;
    }
```

---

## 🔧 Core Operations

### 1. Insert at Beginning
```java
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            newNode.next = head;
            return;
        }

        Node current = head;
        while (current.next != head) {
            current = current.next;
        }

        newNode.next = head;
        current.next = newNode;
        head = newNode;
    }
```

### 2. Insert at End
```java
    public void insertAtEnd(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            newNode.next = head;
            return;
        }

        Node current = head;
        while (current.next != head) {
            current = current.next;
        }

        current.next = newNode;
        newNode.next = head;
    }
```

### 3. Delete at Beginning
```java
    public void deleteAtBeginning() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }

        if (head.next == head) {
            head = null;
            return;
        }

        Node current = head;
        while (current.next != head) {
            current = current.next;
        }

        current.next = head.next;
        head = head.next;
    }
```

### 4. Delete at End
```java
    public void deleteAtEnd() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }

        if (head.next == head) {
            head = null;
            return;
        }

        Node current = head;
        Node prev = null;

        while (current.next != head) {
            prev = current;
            current = current.next;
        }

        prev.next = head;
    }
```

### 5. Search for a Key
```java
    public void search(int key) {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }

        Node current = head;
        do {
            if (current.data == key) {
                System.out.println("Key found");
                return;
            }
            current = current.next;
        } while (current != head);

        System.out.println("Key not found");
    }
```

### 6. Display List
```java
    public void printList() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }

        Node current = head;
        do {
            System.out.print(current.data + " --> ");
            current = current.next;
        } while (current != head);
        System.out.println("(back to head)");
    }
}
```

---

## 🧪 Driver Code Example
```java
public class Main {
    public static void main(String[] args) {
        CircularLinkedList list = new CircularLinkedList();

        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtBeginning(5);

        list.printList();  // Expected: 5 --> 10 --> 20 --> 30 --> (back to head)

        list.deleteAtBeginning();
        list.printList();

        list.deleteAtEnd();
        list.printList();

        list.search(20);
        list.search(99);
    }
}
```

---

## 📌 Notes for Developers
- Always use `do-while` for traversal to ensure one full loop
- Be careful with edge cases in insertion and deletion
- `head.next == head` is a good way to check for single-node list

---

## 📍 Conclusion
Circular Linked Lists are powerful for systems that need **cyclical traversal**. They're extensively used in OS scheduling, buffering, and real-time applications.

Follow **Algorithms365** for more professional-grade data structure tutorials:
- [Algorithms365 YouTube](https://www.youtube.com/@algorithms365)
- [MIT License](https://opensource.org/licenses/MIT)

Keep coding smart, and keep learning.