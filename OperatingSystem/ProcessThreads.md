# Process and Thread Scheduling in Operating Systems

## 1. Process States

A process goes through the following states during its lifecycle:

* **New**: Process is being created.
* **Ready**: Process is waiting to be assigned to a processor.
* **Running**: Instructions are being executed.
* **Waiting (Blocked)**: Waiting for some event (I/O completion).
* **Terminated**: Process has finished execution.
* **Suspended**: Process is not ready/running and is swapped out.

---

## 2. Scheduling Algorithms

### 2.1 First-Come, First-Served (FCFS)

* **Description**: Processes are executed in the order they arrive.
* **Pros**:

  * Simple to implement.
* **Cons**:

  * Convoy effect: one long process can delay others.
* **Use Case**: Simple embedded systems.

### 2.2 Shortest Job Next (SJN) / Shortest Job First (SJF)

* **Description**: Process with the shortest burst time is scheduled next.
* **Pros**:

  * Minimizes average waiting time.
* **Cons**:

  * Hard to predict burst time.
  * May cause starvation.

### 2.3 Priority Scheduling

* **Description**: Each process is assigned a priority.
* **Pros**:

  * Important tasks get more CPU time.
* **Cons**:

  * Starvation of low-priority processes.
* **Solution**: Aging technique (gradually increasing priority).

### 2.4 Round Robin (RR)

* **Description**: Each process gets a fixed time slice.
* **Pros**:

  * Fair and responsive.
* **Cons**:

  * Overhead of frequent context switches.
* **Use Case**: Time-sharing systems.

### 2.5 Multilevel Queue Scheduling

* **Description**: Processes are divided into queues (e.g., interactive, batch).
* **Pros**:

  * Special handling for different types of processes.
* **Cons**:

  * Rigid queue boundaries.

### 2.6 Multilevel Feedback Queue

* **Description**: Processes can move between queues based on behavior.
* **Pros**:

  * More flexible than multilevel queue.
* **Cons**:

  * Complex to implement.

---

## 3. Practical Scheduling Examples

### 3.1 Windows

* Uses **preemptive priority-based scheduling**.
* Supports **multilevel feedback queues**.
* Special handling for GUI responsiveness.
* Uses **quantum** for thread execution time.

### 3.2 Linux

* Uses **Completely Fair Scheduler (CFS)**.
* Based on a red-black tree.
* Tries to distribute CPU time fairly among processes.
* Prioritizes interactive tasks with dynamic time-slicing.

---

## 4. Multicore Processing and Scheduling

* Each core can run a separate thread or process.
* OS uses **load balancing** across cores.
* **Processor affinity**: binding process to specific core.
* **Parallelism**: true concurrent execution.
* Challenges:

  * Cache coherence.
  * Synchronization and deadlocks.

---

## 5. Starvation and Deadlock

* **Starvation**: Low-priority process never gets CPU.

* **Cause**: Priority scheduling, resource hoarding.

* **Solution**: Aging, fair scheduling.

* **Deadlock**: Two or more processes waiting on each other indefinitely.

* **Solution**: Deadlock prevention, detection, recovery.

---

## 6. Blue Screen of Death (BSOD)

* Occurs in Windows when **kernel encounters critical error**.
* Common causes:

  * Driver faults.
  * Hardware failures.
  * Invalid memory access.
* Dumps memory content for debugging.

---

## 7. Process Creation and Execution (e.g., Clicking an App Icon)

1. **User clicks icon or runs .exe**.
2. **Shell or GUI sends request to OS**.
3. **OS loader**:

   * Reads executable from disk.
   * Allocates memory (RAM).
   * Sets up process control block (PCB).
   * Initializes stack, heap, data, code segments.
4. **Scheduler places process in Ready Queue**.
5. **CPU assigns time slice** and begins execution.

---

## 8. Process in RAM and Kernel Structures

* **RAM Allocation**:

  * Code segment (text).
  * Data segment (initialized, uninitialized).
  * Stack (function calls, local vars).
  * Heap (dynamic memory).

* **Process Table (Task Struct)**:

  * Maintained in **kernel space**.
  * Contains PID, state, registers, priority, memory pointers.

---

## 9. Threads

* Lightweight subprocesses.
* Share code, data, and OS resources with other threads in process.
* **Thread scheduling** can be user-level or kernel-level.
* Multithreaded applications benefit more from multicore CPUs.

### 9.1 Comparison Between Process and Thread

| Feature                | Process                                  | Thread                                  |
|------------------------|------------------------------------------|------------------------------------------|
| Definition             | Independent program in execution         | Smallest unit of execution in a process |
| Resource Allocation    | Has its own memory and resources         | Shares memory and resources of process  |
| Overhead               | Higher                                   | Lower                                   |
| Communication          | Inter-process communication (IPC) needed | Easier through shared memory            |
| Crash Impact           | Crash does not affect others             | Crash can affect all threads            |
| Creation Time          | Slower                                   | Faster                                  |
| Context Switching Time | Higher                                   | Lower                                   |
| Scheduling             | Managed independently                    | Managed within parent process           |

---

## 10. Memory Allocation to Processes and Threads

### 10.1 How OS Decides Default Memory Assignment

* Based on:

  * **System architecture** (32-bit vs 64-bit).
  * **Available physical RAM**.
  * **Page size and virtual address space limits**.
  * **System and user limits** defined in OS configuration.
  * **Application request and usage pattern**.
* Windows and Linux use **virtual memory** model, so initial memory is reserved but not necessarily committed until accessed.

### 10.2 Memory Allocation Method: Paging vs Contiguous

* **Paging** is used by modern OS:

  * Memory divided into fixed-size pages (usually 4 KB).
  * Avoids external fragmentation.
  * Pages may be scattered in RAM.
* **Contiguous allocation**:

  * Rarely used due to fragmentation issues.

### 10.3 Dynamic Memory Allocation

* Allocated from **heap segment**.
* Functions like `malloc()` (C/C++), `new` (Java/C++), or system-specific calls (`brk`, `mmap`).
* Managed using data structures in the **user space** and kernel.

### 10.4 Heap Memory Characteristics

* Heap memory is **paged**, not necessarily contiguous.
* OS uses **demand paging**:

  * Pages allocated as needed.
  * Swapped in/out based on access.
* Allocator uses techniques like:

  * Free lists.
  * Buddy system.
  * Slab allocators (in kernel).

### 10.5 Virtual Memory and Address Translation

* **CPU generates virtual addresses**.
* **MMU (Memory Management Unit)** translates virtual addresses to physical addresses.
* **Page tables** are used to maintain mappings.
* Address translation involves:

  1. Virtual address is divided into page number and offset.
  2. Page number is used to look up physical frame in page table.
  3. Offset is added to get final physical address.

### 10.6 Virtual Memory Limits

* Not infinite; depends on:

  * **Address bus width**:

    * 32-bit: typically 4 GB virtual address space.
    * 64-bit: can support terabytes (actual usable depends on OS and hardware).
  * **OS design**: Limits total virtual memory per process.
  * **Swap space**: Extends virtual memory using disk.

---

## Summary

| Concept                | Windows                        | Linux                           |
| ---------------------- | ------------------------------ | ------------------------------- |
| Scheduler              | Priority + Multilevel Feedback | Completely Fair Scheduler (CFS) |
| Multicore Support      | Load balancing, affinity       | Load balancing, affinity        |
| Thread Handling        | Preemptive                     | Preemptive                      |
| Process Table          | EPROCESS                       | task\_struct                    |
| Error Handling (Crash) | BSOD                           | Kernel panic                    |
| Memory Allocation      | Virtual memory, paged heap     | Virtual memory, paged heap      |

---

> **Note**: Efficient scheduling and memory management ensures responsive, fair, and efficient use of system resources.
