# 🧠 Operating System Memory Management

## 📋 Executive Summary

This document explains memory management in operating systems in a structured and intuitive way. It covers key concepts like paging, segmentation, virtual memory, memory layout, page table isolation (PTI), and real-world OS implementations. Analogies and diagrams are used to simplify complex ideas.

---

## 🔍 What is Memory Management?

Memory Management is a core function of an Operating System (OS). It ensures:

* Allocation/deallocation of memory to processes
* Safe and efficient memory usage
* Isolation and protection between processes

### 🧰 Analogy:

Think of memory as a large apartment building (RAM). The OS is the building manager that rents out apartments (memory blocks) to tenants (processes), ensures no one intrudes into others’ apartments, and tracks available rooms.

---

## 📦 Types of Memory

### 1. **Primary Memory (RAM)**

* Fast, volatile memory
* Holds active processes and data

### 2. **Secondary Memory (HDD/SSD)**

* Slower, non-volatile
* Stores data not in active use (swap, files, etc.)

---

## 📚 Memory Allocation Techniques

### 1. **Contiguous Memory Allocation**

* Each process gets one continuous block of memory
* Can use:

  * **Fixed Partitioning**
  * **Dynamic Partitioning**

### 2. **Non-Contiguous Allocation**

* Allocates memory in scattered chunks
* Achieved using:

  * **Paging**
  * **Segmentation**

---

# 📦 Paging

## 🔍 What is Paging?

Paging divides memory into equal-size blocks:

* **Physical Memory** → Frames
* **Logical Memory** → Pages

### 🎯 Goals:

* Avoid external fragmentation
* Allow non-contiguous memory use
* Enable virtual memory

### 🧠 How Paging Works:

1. Logical address = Page number + Offset
2. Page Table maps pages → frames
3. Translates to physical address

### 🧾 Example Page Table:

| Virtual Page | Physical Frame |
| ------------ | -------------- |
| 0            | 5              |
| 1            | 2              |
| 2            | 8              |
| 3            | *(on disk)*    |

➡️ Accessing page 3 → **page fault** → Load from disk

### 🖥️ Memory Layout with Paging:

```
Low Address
┌──────────────────────────┐
│ Code / Text Segment      │
├──────────────────────────┤
│ Initialized Data Segment │
├──────────────────────────┤
│ Uninitialized Data (BSS) │
├──────────────────────────┤
│ Heap                     │ ← Grows Up
│   (malloc/new memory)    │
├──────────────────────────┤
│                          │
├──────────────────────────┤
│ Stack                    │ ← Grows Down
└──────────────────────────┘
High Address
```

---

## 🪟 Paging in Windows

* Uses **Demand Paging** + **pagefile.sys**
* Page size = 4 KB
* Pages loaded into RAM when needed

---

## 🧮 Page Replacement Algorithms

| Algorithm   | Description                                              |
| ----------- | -------------------------------------------------------- |
| **FIFO**    | Replace oldest loaded page                               |
| **LRU**     | Replace least recently accessed page                     |
| **Optimal** | Replace page that won’t be used for longest time (ideal) |
| **Clock**   | Circular queue with reference bits (2nd chance)          |

### 🧰 Analogy:

Like cleaning a crowded fridge (RAM) to make space: FIFO removes the oldest item, LRU removes what you haven’t touched in days.

---

# 🧱 Memory Layout in Virtual Address Space

| Segment | Allocated at Load? | Grows? | Access         |
| ------- | ------------------ | ------ | -------------- |
| Code    | ✅ Yes              | ❌ No   | Read + Execute |
| Data    | ✅ Yes              | ❌ No   | Read + Write   |
| Heap    | ❌ On Demand        | ✅ Up   | Read + Write   |
| Stack   | ✅ Yes              | ✅ Down | Read + Write   |

> All segments are composed of pages and mapped via the page table.

---

## 🔐 Page Table Isolation (PTI)

### 🔍 Why PTI?

To protect kernel memory from user access (Meltdown fix).

### 🔐 How PTI Works:

* Separate page tables for user and kernel mode
* Switches on context change

### ✅ PTI Impact:

| Feature             | Before PTI | After PTI |
| ------------------- | ---------- | --------- |
| Kernel mapped?      | ✅ Yes      | ❌ No      |
| Protected by perms? | ✅ Yes      | ✅ Yes     |
| Speculation-safe?   | ❌ No       | ✅ Yes     |

### 💻 OS Support:

| OS      | PTI Support      |
| ------- | ---------------- |
| Linux   | ✅ Kernel 4.15+   |
| Windows | ✅ Win 10 v1803+  |
| macOS   | ✅ macOS 10.13.2+ |

---

# 🧮 Segmentation

## 🔍 What is Segmentation?

* Divides logical memory into **logical segments**: code, data, stack
* Each segment has a **number + offset**

## 🔄 Paging vs Segmentation:

| Feature       | Paging            | Segmentation               |
| ------------- | ----------------- | -------------------------- |
| Division      | Fixed-size pages  | Logical segments           |
| Fragmentation | Internal          | External                   |
| Structure     | Hardware-enforced | Aligned with program logic |

### 📚 Analogy:

Paging is like cutting paper into squares. Segmentation is like dividing a book into chapters.

---

# 🐧 OS-Specific Segmentation

## Linux:

* Uses **flat segments**
* 64-bit mode disables segmentation except FS/GS
* FS/GS used for TLS (Thread Local Storage)

## macOS:

* Based on Darwin (XNU), follows flat model
* Uses paging and virtual memory only

## Windows:

* Uses **pure paging**, segmentation obsolete

| OS      | Segmentation Use?  | Notes                         |
| ------- | ------------------ | ----------------------------- |
| Linux   | 🟡 Minimal (FS/GS) | TLS & legacy systems only     |
| macOS   | ❌ No               | Pure paging                   |
| Windows | ❌ No               | Pure paging with flat address |

---

# 🚀 Virtual Memory

## 🔍 What is Virtual Memory?

* Lets processes exceed RAM limits
* Maps virtual pages to disk when RAM is full
* Enables **Demand Paging**

## 🔄 Swapping & Thrashing

* **Swapping**: inactive pages moved to disk
* **Thrashing**: system spends more time swapping than executing

---

# 👨‍💼 Common Interview Questions

1. **Paging vs Segmentation**

   > Paging = fixed blocks; Segmentation = logical blocks

2. **What is a Page Fault?**

   > Accessing a page not in RAM; must load from disk

3. **Virtual Memory?**

   > Use of disk as extension of RAM

4. **FIFO vs LRU?**

   > FIFO is simpler; LRU is smarter

5. **What is TLB?**

   > Hardware cache for recent page table lookups

6. **Internal vs External Fragmentation?**

   > Internal = unused space inside block
   > External = scattered small free blocks

7. **Segmentation Fault?**

   > Illegal access outside segment boundaries

---

# ✅ Final Takeaways

* Paging is the dominant memory management method
* Segmentation is mostly historical (except FS/GS)
* Page table isolation is key to security
* OSes like Linux, Windows, and macOS all use pure paging with virtual memory

> 🔐 Modern OSes protect memory via isolation, translation, and permission checks—making multi-process computing secure and efficient.
