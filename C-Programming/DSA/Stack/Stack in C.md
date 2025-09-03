# Stack Data Structure in C

## Overview of Stack
A **stack** is a linear data structure that follows the **LIFO** (Last In, First Out) principle. It means that the element added most recently is the first one to be removed.

### Real-Life Examples of Stack Usage
1. **Browser History**: When you visit web pages, the back button uses a stack to keep track of previous pages.
2. **Undo Operations**: Text editors like MS Word use a stack to store previous states for undo operations.
3. **Call Stack in Programming**: When functions are called, their information is stored in a stack to maintain the order of execution.

### Time Complexity of Stack Operations
| Operation       | Time Complexity |
|-----------------|-----------------|
| Push (Insert)   | O(1)            |
| Pop (Remove)    | O(1)            |
| Peek (Top View) | O(1)            |
| IsEmpty         | O(1)            |

## Ways to Implement a Stack
### 1. **Array-Based Stack**
- **Pros**:
  - Simple and fast.
  - Memory is allocated contiguously, leading to better cache performance.
- **Cons**:
  - Fixed size; cannot dynamically grow.
  - Risk of stack overflow if capacity is exceeded.

### 2. **Linked List-Based Stack**
- **Pros**:
  - Dynamic size; no risk of overflow (limited only by system memory).
  - Efficient memory utilization as nodes are allocated dynamically.
- **Cons**:
  - Higher overhead due to memory allocation for each node.
  - Non-contiguous memory leads to slower cache performance.

---

## C Implementation of Stack Operations

### Using Array
```c
#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100

// Stack structure definition
typedef struct {
    int items[MAX_SIZE]; // Array to hold stack elements
    int top;             // Index of the top element
} Stack;

// Initialize the stack
void initializeStack(Stack *stack) {
    stack->top = -1;
}

// Check if the stack is empty
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Check if the stack is full
int isFull(Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

// Push an element onto the stack
void push(Stack *stack, int value) {
    if (isFull(stack)) {
        printf("Stack overflow! Cannot push %d.\n", value);
        return;
    }
    stack->top = stack->top + 1;
    stack->items[stack->top] = value;
    printf("Pushed %d onto the stack.\n", value);
}

// Pop an element from the stack
int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack underflow! Cannot pop.\n");
        return -1;
    }
    int poppedValue = stack->items[stack->top];
    stack->top = stack->top - 1;
    return poppedValue;
}

// Peek at the top element without removing it
int peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        return -1;
    }
    return stack->items[stack->top];
}

int main() {
    Stack stack;
    initializeStack(&stack);

    push(&stack, 10);
    push(&stack, 20);
    printf("Top element is %d\n", peek(&stack));
    printf("Popped element is %d\n", pop(&stack));
    printf("Popped element is %d\n", pop(&stack));
    pop(&stack); // Attempt to pop from an empty stack

    return 0;
}
```

### Using Linked List
```c
#include <stdio.h>
#include <stdlib.h>

// Node structure definition
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Push an element onto the stack
void push(Node **top, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Heap overflow!\n");
        return;
    }
    newNode->data = value;
    newNode->next = *top;
    *top = newNode;
    printf("Pushed %d onto the stack.\n", value);
}

// Pop an element from the stack
int pop(Node **top) {
    if (*top == NULL) {
        printf("Stack underflow!\n");
        return -1;
    }
    Node *nodeToRemove = *top;
    int poppedValue = nodeToRemove->data;
    *top = nodeToRemove->next;
    free(nodeToRemove);
    return poppedValue;
}

// Peek at the top element without removing it
int peek(Node *top) {
    if (top == NULL) {
        printf("Stack is empty!\n");
        return -1;
    }
    return top->data;
}

int main() {
    Node *stack = NULL; // Initialize an empty stack

    push(&stack, 30);
    push(&stack, 40);
    printf("Top element is %d\n", peek(stack));
    printf("Popped element is %d\n", pop(&stack));
    printf("Popped element is %d\n", pop(&stack));
    pop(&stack); // Attempt to pop from an empty stack

    return 0;
}
```

---

## Comparison of Array and Linked List Implementations
| Feature                | Array-Based Stack | Linked List-Based Stack |
|------------------------|-------------------|-------------------------|
| Memory Allocation      | Fixed size        | Dynamic size            |
| Overflow Handling      | Yes               | No                      |
| Cache Performance      | Better            | Worse                   |
| Implementation Overhead| Low               | High                    |

---

## Conclusion
The stack is a versatile data structure used in various real-world applications, particularly when LIFO operations are required. Depending on the use case, you can implement stacks using arrays or linked lists, each with its own trade-offs. Understanding both implementations and their nuances helps in choosing the best solution for a given problem.
