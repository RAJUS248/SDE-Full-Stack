# Queue Data Structure in C

## Overview of Queue
A **queue** is a linear data structure that follows the **FIFO** (First In, First Out) principle. This means the element added first is removed first, similar to real-life queues.

### Real-Life Examples of Queue Usage
- **Ticket Counters**: People wait their turn.
- **Printers**: Jobs are processed in order.
- **CPU Scheduling**: Processes scheduled in FIFO manner.

### Time Complexity of Queue Operations
| Operation        | Time Complexity |
|------------------|-----------------|
| Enqueue (Insert) | O(1)            |
| Dequeue (Remove) | O(1)            |
| Peek (Front)     | O(1)            |
| IsEmpty          | O(1)            |

---

## Implementations of Queue
We explore three implementations:
1. **Array-Based Queue (non-circular)**
2. **Array-Based Queue (circular)**
3. **Linked List-Based Queue**

### 1. Array-Based Queue (Non-Circular)
In this version, `front` and `rear` pointers manage the start and end of the queue. However, once an element is dequeued, that space is not reused, leading to inefficient space usage.

#### Pros:
- Easy to implement.
- Direct indexing.

#### Cons:
- Space is wasted unless elements are shifted manually.

```c
#define MAX_SIZE 100

// Define a Queue structure
typedef struct {
    int items[MAX_SIZE];
    int front;
    int rear;
} Queue;

// Initialize the queue
void initializeQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

// Check if the queue is empty
int isQueueEmpty(Queue *q) {
    return q->front > q->rear;
}

// Check if the queue is full
int isQueueFull(Queue *q) {
    return q->rear == MAX_SIZE - 1;
}

// Add an element to the queue
void enqueue(Queue *q, int value) {
    if (isQueueFull(q)) {
        printf("Queue overflow!\n");
        return;
    }
    q->rear++;
    q->items[q->rear] = value;
    printf("Enqueued %d\n", value);
}

// Remove and return the front element
int dequeue(Queue *q) {
    if (isQueueEmpty(q)) {
        printf("Queue underflow!\n");
        return -1;
    }
    int value = q->items[q->front];
    q->front++;
    return value;
}
```

### 2. Array-Based Queue (Circular)
This approach reuses array space using modulo arithmetic. When `rear` reaches the end, it wraps around if space is available at the front.

#### Pros:
- Efficient space utilization.

#### Cons:
- Slightly more complex logic.

```c
#define MAX_SIZE 100

// Define a circular queue
typedef struct {
    int items[MAX_SIZE];
    int front;
    int rear;
} Queue;

// Initialize the queue
void initializeQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

// Check if queue is empty
int isQueueEmpty(Queue *q) {
    return q->front == -1;
}

// Check if queue is full
int isQueueFull(Queue *q) {
    return (q->rear + 1) % MAX_SIZE == q->front;
}

// Add an element to the queue
void enqueue(Queue *q, int value) {
    if (isQueueFull(q)) {
        printf("Queue overflow!\n");
        return;
    }

    if (isQueueEmpty(q)) {
        q->front = 0;
    }

    q->rear = (q->rear + 1) % MAX_SIZE;
    q->items[q->rear] = value;
    printf("Enqueued %d\n", value);
}

// Remove and return the front element
int dequeue(Queue *q) {
    if (isQueueEmpty(q)) {
        printf("Queue underflow!\n");
        return -1;
    }

    int value = q->items[q->front];

    if (q->front == q->rear) {
        // Only one element was present
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX_SIZE;
    }

    return value;
}
```

### 3. Linked List-Based Queue
A queue using dynamically allocated nodes, which grows and shrinks as needed.

#### Pros:
- Dynamic size.
- No overflow (unless heap is full).

#### Cons:
- Slightly more memory usage due to pointers.

```c
#include <stdio.h>
#include <stdlib.h>

// Define a node structure
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Define a Queue using front and rear pointers
typedef struct {
    Node *front;
    Node *rear;
} Queue;

// Initialize an empty queue
void initializeQueue(Queue *q) {
    q->front = NULL;
    q->rear = NULL;
}

// Check if queue is empty
int isQueueEmpty(Queue *q) {
    return q->front == NULL;
}

// Add an element to the queue
void enqueue(Queue *q, int value) {
    Node *newNode = malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;

    if (isQueueEmpty(q)) {
        q->front = newNode;
    } else {
        q->rear->next = newNode;
    }

    q->rear = newNode;
    printf("Enqueued %d\n", value);
}

// Remove and return the front element
int dequeue(Queue *q) {
    if (isQueueEmpty(q)) {
        printf("Queue underflow!\n");
        return -1;
    }

    Node *temp = q->front;
    int value = temp->data;
    q->front = q->front->next;

    if (q->front == NULL) {
        q->rear = NULL;
    }

    free(temp);
    return value;
}
```

---

## Comparison Table
| Feature                | Array (Non-Circular) | Array (Circular) | Linked List |
|------------------------|----------------------|------------------|--------------|
| Memory Utilization     | Inefficient          | Efficient        | Optimal      |
| Size Limit             | Fixed                | Fixed            | Dynamic      |
| Implementation         | Simple               | Moderate         | Moderate     |
| Overflow Risk          | High                 | Low              | None         |
| Performance (Cache)    | High                 | High             | Medium       |

---

## Driver Code Example
```c
int main() {
    Queue q;

    // Initialize the queue
    initializeQueue(&q);

    // Add items to the queue
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);

    // Remove and print each item
    int removedItem;

    removedItem = dequeue(&q);
    printf("Dequeued: %d\n", removedItem);

    removedItem = dequeue(&q);
    printf("Dequeued: %d\n", removedItem);

    enqueue(&q, 40);

    removedItem = dequeue(&q);
    printf("Dequeued: %d\n", removedItem);

    removedItem = dequeue(&q);
    printf("Dequeued: %d\n", removedItem);

    // Try to dequeue from an empty queue
    removedItem = dequeue(&q);
    printf("Dequeued: %d\n", removedItem);

    return 0;
}
```

## Conclusion
Queues are vital in software applications requiring ordered processing. While the array approach is faster and simpler, the circular method optimizes space, and the linked list approach offers dynamic scaling.

### Notes from algorithms365

#### Websites:
- **Skills Website**: [https://skills.algorithms365.com/](https://skills.algorithms365.com/)  
- **Company Website**: [https://algorithms365.com/](https://algorithms365.com/)  

---

#### Follow & Subscribe on Social Media Platforms:
- **Instagram**: [https://www.instagram.com/algorithms365/](https://www.instagram.com/algorithms365/)  
- **YouTube**: [https://www.youtube.com/@algorithms365](https://www.youtube.com/@algorithms365)  
- **Facebook**: [https://www.facebook.com/algorithms365](https://www.facebook.com/algorithms365)  
- **Twitter (X)**: [https://x.com/algorithms365](https://x.com/algorithms365)  
- **LinkedIn**: [https://www.linkedin.com/company/algorithms365-technologies-llp/](https://www.linkedin.com/company/algorithms365-technologies-llp/)  

---

## Join Our Communities:
- **WhatsApp**: [https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht](https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht)  
- **Telegram**: [https://t.me/+hyVHX
