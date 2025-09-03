# Process and Threads - OS Interview Notes

These notes cover frequently asked interview questions on **Processes and Threads** in Operating Systems, specifically targeted for software product companies like Google, Microsoft, Amazon, Adobe, etc.

---

## 1. Basic Concepts

### What is a process?

A **process** is an instance of a program in execution. It has its own address space, code, data, and system resources.

### What is a thread?

A **thread** is the smallest unit of CPU execution within a process. Multiple threads can run concurrently within the same process and share its resources.

### Difference between process and thread

| Feature       | Process                     | Thread                      |
| ------------- | --------------------------- | --------------------------- |
| Memory        | Separate memory space       | Shared memory of process    |
| Overhead      | High (context switch heavy) | Low                         |
| Isolation     | Fully isolated              | Not isolated                |
| Communication | IPC needed                  | Easier via shared variables |

### What is context switching?

It is the act of storing the state of a process/thread so it can be resumed later. This involves saving registers, program counter, and stack information.

---

## 2. Process Lifecycle & Management

### States of a Process

* New
* Ready
* Running
* Waiting
* Terminated

### What is a zombie process?

A process that has completed execution but still has an entry in the process table.

### What is an orphan process?

A child process whose parent has terminated before the child finishes.

---

## 3. Threads and Multithreading

### Benefits of multithreading

* Faster execution (parallelism)
* Better resource utilization
* Simplified program structure

### Challenges

* Synchronization
* Race conditions
* Deadlocks

### User-level vs Kernel-level threads

| Feature     | User-Level Threads   | Kernel-Level Threads      |
| ----------- | -------------------- | ------------------------- |
| Managed by  | User libraries       | OS kernel                 |
| Performance | Faster (no syscall)  | Slower (needs syscall)    |
| Parallelism | Not true parallelism | True parallelism possible |

---

## 4. Concurrency and Synchronization

### Race Condition

Occurs when multiple threads access shared data and try to change it concurrently.

### Critical Section

A part of the code that accesses shared resources and must not be executed by more than one thread at a time.

### Synchronization tools

* **Mutex**: Ensures only one thread accesses critical section.
* **Semaphore**: A signaling mechanism (counting or binary).
* **Monitor**: High-level abstraction that encapsulates mutex and condition variables.

### Deadlock conditions

* Mutual exclusion
* Hold and wait
* No preemption
* Circular wait

---

## 5. Inter-Process Communication (IPC)

### Why IPC?

Processes are isolated; IPC allows them to share data.

### IPC Mechanisms

* **Pipes**: One-way communication, parent-child
* **Named Pipes**: Two unrelated processes
* **Shared Memory**: Fastest, needs synchronization
* **Message Queues**: Messages between processes
* **Sockets**: Used over networks or localhost

---

## 6. Process Scheduling

### Scheduling Algorithms

* FCFS (First Come First Serve)
* SJF (Shortest Job First)
* RR (Round Robin)
* Priority Scheduling
* Multilevel Queue Scheduling

### Preemptive vs Non-preemptive

* **Preemptive**: Can take the CPU away from running process (e.g., RR)
* **Non-preemptive**: Once scheduled, process runs till end or I/O (e.g., FCFS)

### Priority Inversion

Occurs when a lower-priority process holds a resource needed by a higher-priority process.

---

## 7. Advanced Scenarios

### Thread crash in a process

If one thread crashes, it can potentially crash the whole process depending on the nature of the failure (e.g., segmentation fault).

### Can threads from different processes share memory?

Not directly. Shared memory regions must be explicitly created (e.g., mmap in Linux).

### Multicore and threads

OS distributes threads across cores to maximize CPU utilization and performance.

---

## 8. Coding Questions

### Producer-Consumer Problem

Use semaphores or condition variables to manage synchronization between producer and consumer threads accessing a bounded buffer.

### Reader-Writer Problem

Readers can read simultaneously, but writers need exclusive access.

### Dining Philosophers Problem

Classic deadlock and starvation problem involving limited resources (forks).

### Thread-Safe Singleton

Ensure only one instance of a class is created even in multithreaded environments.

---

## Tips for Preparation

* Understand OS concepts from Galvin or Tanenbaum.
* Write multithreaded code in C/C++/Java using mutex, semaphores.
* Visualize with diagrams (process states, memory models).
* Think in terms of real-world analogies (ATM withdrawal = critical section).

---

Let me know if you’d like a PDF export, code samples, or mock interview scenarios.
