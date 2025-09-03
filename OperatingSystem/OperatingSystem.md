# Operating Systems - Comprehensive Notes for Computer Science Engineering

---

## Chapter 1: Introduction to Operating Systems

### What is an Operating System (OS)?
An Operating System is system software that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between users and the computer hardware.

### Functions of OS:
- Process management
- Memory management
- File system management
- Device management
- Security and access control
- User interface (CLI/GUI)

### Types of Operating Systems:
| Type               | Description                                  | Examples          |
|--------------------|----------------------------------------------|-------------------|
| Batch OS           | Executes jobs without user interaction       | Early IBM OS      |
| Time-Sharing OS    | Multiple users interact simultaneously       | UNIX, Linux       |
| Distributed OS     | Manages group of distinct computers          | Amoeba, LOCUS     |
| Real-Time OS (RTOS)| Responds instantly, used in embedded systems | VxWorks, QNX      |

---

## Chapter 2: Process Management

### What is a Process?
A process is a program in execution. It includes program code, current activity, program counter, registers, and variables.

### Process States:
- **New**: Process is being created.
- **Ready**: Process is waiting to be assigned to a processor.
- **Running**: Instructions are being executed.
- **Waiting**: Process is waiting for some event (I/O completion).
- **Terminated**: Process has finished execution.

### Process Control Block (PCB):
A data structure in OS containing process information: PID, state, CPU registers, scheduling info, memory limits, I/O status, etc.

### Example:
Opening a text editor moves the process through states: New → Ready → Running → Waiting (if waiting for user input) → Ready → Terminated.

---

## Chapter 3: CPU Scheduling

### Scheduling Criteria:
- CPU Utilization (keep CPU busy)
- Throughput (processes completed per unit time)
- Turnaround Time (total time taken for process)
- Waiting Time (time spent in ready queue)
- Response Time (time to first response)

### Scheduling Algorithms:

| Algorithm       | Description                                  | Pros                    | Cons                         |
|-----------------|----------------------------------------------|-------------------------|------------------------------|
| FCFS            | Processes served in order of arrival          | Simple                  | Long waiting times (convoy)  |
| SJF             | Process with shortest burst time runs first  | Minimizes average waiting| Starvation risk, needs prior knowledge |
| Round Robin     | Fixed time quantum for each process           | Fair for time-sharing    | Overhead, quantum tuning needed|
| Priority        | Highest priority runs first                    | Prioritizes important tasks| Starvation of low priority  |

### Example: Round Robin Scheduling in Python

```python
def round_robin(processes, burst_times, quantum):
    n = len(processes)
    rem_bt = burst_times.copy()
    t = 0
    waiting_time = [0] * n

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    waiting_time[i] = t - burst_times[i]
                    rem_bt[i] = 0
        if done:
            break

    return waiting_time

processes = [1, 2, 3]
burst_times = [5, 3, 8]
quantum = 2

wt = round_robin(processes, burst_times, quantum)
print("Waiting times:", wt)
```

---

## Chapter 4: Interprocess Communication & Synchronization

### Interprocess Communication (IPC)
Mechanisms for processes to exchange data:
- **Shared Memory**: Processes share a common memory space.
- **Message Passing**: Processes send and receive messages.

### Synchronization
Ensures that multiple processes accessing shared resources do so without conflict.

### Critical Section Problem
Only one process should enter the critical section at a time.

### Requirements:
- Mutual Exclusion
- Progress
- Bounded Waiting

### Synchronization Tools
- Mutex
- Semaphores (wait and signal operations)
- Monitors

### Classic Problem: Producer-Consumer (using Semaphore in Python)

```python
import threading
import time
import random

buffer = []
buffer_size = 5

empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)
mutex = threading.Lock()

def producer():
    while True:
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Produced: {item}")
        mutex.release()
        full.release()
        time.sleep(random.random())

def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(random.random())

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
```

---

## Chapter 5: Memory Management & Virtual Memory

### Memory Management
The OS manages RAM allocation and deallocation to processes, protecting memory spaces.

### Allocation Techniques:
- **Contiguous Allocation**: Each process occupies contiguous memory.
- **Paging**: Divides memory into fixed-size pages and frames.
- **Segmentation**: Divides memory into variable-sized logical segments.

### Paging Details:
- Logical address = (Page Number, Offset)
- Physical address = (Frame Number, Offset)
- Uses page tables to map logical pages to physical frames.

### Virtual Memory
Allows programs larger than physical memory by using secondary storage.

### Demand Paging
Pages loaded on demand when a page fault occurs.

### Page Replacement Algorithms
- FIFO
- Optimal (theoretical)
- LRU (Least Recently Used)
- Clock (Efficient approximation of LRU)

### Effective Access Time (EAT) Formula
\[
\text{EAT} = (1-p) \times \text{memory access time} + p \times \text{page fault time}
\]
where \(p\) = page fault rate.

---

## Chapter 6: File Systems

### File System Role
Organizes data on storage devices into files and directories.

### File Concepts:
- File attributes (name, size, timestamps, permissions)
- File operations (create, read, write, delete)

### File Allocation Methods:

| Method                | Description                                 | Pros                  | Cons                       |
|-----------------------|---------------------------------------------|-----------------------|----------------------------|
| Contiguous Allocation | Files stored in contiguous blocks           | Fast access           | External fragmentation      |
| Linked Allocation     | File blocks linked together                  | No external fragmentation | Slow random access        |
| Indexed Allocation    | Uses an index block with pointers            | Supports direct access | Index overhead, size limits |

### Directory Structures:
- Single-level, two-level, tree-structured, acyclic graph, general graph.

### Disk Scheduling Algorithms:

| Algorithm | Description                     | Pros                   | Cons                    |
|-----------|---------------------------------|------------------------|-------------------------|
| FCFS      | Requests served in arrival order | Simple                 | High average seek time  |
| SSTF      | Closest request served first     | Reduces seek time      | Starvation risk         |
| SCAN      | Moves arm in one direction       | Fair                   | Variance in wait times  |
| C-SCAN    | Circular SCAN (returns to start) | Uniform wait times     | More head movement      |

### File Protection
- Permissions (read, write, execute)
- Access Control Lists (ACLs)

---

## Chapter 7: Sample File Operations in Python

```python
import os

filename = "example.txt"

# Create a file
with open(filename, "w") as f:
    f.write("This is a sample file.\n")

# Check if file exists
if os.path.exists(filename):
    print(f"{filename} exists.")

# Read file
with open(filename, "r") as f:
    content = f.read()
    print("File content:")
    print(content)

# Delete file
os.remove(filename)
print(f"{filename} deleted.")
```

---
# Kernel Mode vs User Mode in Operating Systems (Windows Example)

Operating systems like Windows use a **dual-mode architecture** to isolate system-level and application-level code. These two primary modes are:

- **Kernel Mode** (Ring 0): Full system access
- **User Mode** (Ring 3): Limited access for applications

---

## 🔄 Key Differences Between Kernel Mode and User Mode

| Feature                  | **Kernel Mode**                                        | **User Mode**                                             |
|--------------------------|--------------------------------------------------------|------------------------------------------------------------|
| Access Level             | Full system access (privileged)                       | Restricted access to system resources                     |
| CPU Ring Level           | Ring 0                                                | Ring 3                                                    |
| Code Examples            | `ntoskrnl.exe`, `hal.dll`, device drivers             | `explorer.exe`, `chrome.exe`, user programs               |
| Fault Impact             | Crash (BSOD)                                          | Process crash only                                        |
| Memory Access            | Can access all memory                                 | Can only access its own virtual memory space              |
| System API Availability  | Full set of internal OS functions                     | Uses system APIs via system calls                         |
| Isolation                | No isolation between kernel components                | Isolated from other processes                             |
| Performance              | Fast (direct hardware access)                         | Slower (must call into kernel for hardware access)        |
| Scheduling               | Schedulers run in kernel mode                         | Processes/threads run in user mode                        |
| Use Cases                | Drivers, kernel routines, low-level hardware access   | Applications, services, GUI programs                      |

---


## 🖼️ Windows OS Architecture Diagram

```text
+------------------------------------------------------------+
|                    User Mode (Ring 3)                      |
|                                                            |
|  +---------------------+   +----------------------------+  |
|  |  User Applications  |   |  User Mode System Services|  |
|  |  (e.g., Chrome.exe) |   |  (e.g., csrss.exe, lsass) |  |
|  +---------------------+   +----------------------------+  |
|             |                                |             |
|             +-------------+------------------+             |
|                           |                                |
+---------------------------|--------------------------------+
                            |
                            ▼
+------------------------------------------------------------+
|                    Kernel Mode (Ring 0)                    |
|                                                            |
|  +------------------------------------------------------+  |
|  |              Executive (Windows Kernel Services)      |  |
|  |  - Process Manager                                    |  |
|  |  - Memory Manager                                     |  |
|  |  - I/O Manager                                        |  |
|  |  - Object Manager                                     |  |
|  |  - Security Reference Monitor                         |  |
|  +------------------------------------------------------+  |
|                                                            |
|  +--------------------+    +----------------------------+  |
|  | Kernel (ntoskrnl)  |    |  Hardware Abstraction Layer|  |
|  +--------------------+    |      (hal.dll)             |  |
|                            +----------------------------+  |
|                                                            |
|  +----------------------+                                 |  
|  | Device Drivers       |                                 |  
|  | (e.g., GPU, Disk)    |                                 |  
|  +----------------------+                                 |  
|                                                            |
+------------------------------------------------------------+



# Summary

These notes cover the fundamental topics of Operating Systems, including process management, CPU scheduling, IPC, memory management, virtual memory, file systems, and examples with Python code for practical understanding.

---

Feel free to ask for further clarifications, examples, or exercises on any topic!
