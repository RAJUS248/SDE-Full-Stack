/*
* -----------------------------------------------------------------------------
*
* Copyright <2024> <algorithms365>
*
* Professional Coding Skills Workshops
*
* Licensed under the MIT License:
*
* https://opensource.org/licenses/MIT
*
* For more information about algorithms365:
* Visit Our Skills Website: https://skills.algorithms365.com/
* Our Company Website: https://algorithms365.com/
*
* For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
* Instagram: https://www.instagram.com/algorithms365/
* YouTube: https://www.youtube.com/@algorithms365
* Facebook: https://www.facebook.com/algorithms365
* Twitter(X): https://x.com/algorithms365
* LinkedIn: https://www.linkedin.com/company/algorithms365-technologies-llp/
*
* Join Our Communities:
* WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
* Telegram: https://t.me/+hyVHXek9WM0zNWQ1
*
* -----------------------------------------------------------------------------
*/
#include <stdio.h>
#define MAX_STACK_SIZE 3

typedef struct{
    int items[MAX_STACK_SIZE];
    int index;
} Stack;

void initialize(Stack* pStack)
{
    pStack->index = -1;
    printf("\n Stack is initialized");
}

void Push(int data, Stack* pStack)
{
    // Check if we have reached the max size 
    if (pStack->index == MAX_STACK_SIZE -1)
    {
        printf("\n Stack is full, we can't insert more items");
        return;
    }

    // Adding the item to the stack
    pStack->index = pStack->index + 1; // Increment the index value 
    pStack->items[pStack->index] = data; // Copy the value
    printf("\n Pushed value %d in the stack", data);
}

int Pop(Stack* pStack)
{
    // Check if there are any items in the stack
    if (pStack->index == -1)
    {
        printf("\nStack is empty");
        return -1;
    }

    // We need to pop the top element and reduce the index 
    int item = pStack->items[pStack->index];
    pStack->index--;
    printf("\n Poped value %d in the stack", item);
    return item;
}

int peek(Stack* pStack)
{
    // Check if it is empty
    if (pStack->index == -1)
    {
        printf("\nStack is empty");
        return -1;
    }

    printf("\n Top element in the stack is %d", pStack->items[pStack->index]);
    return pStack->items[pStack->index];
}

int getSize(Stack* pStack)
{
    printf("\n Current number of elements in the stack =  %d", pStack->index+1);
    return pStack->index+1; // Count will be one greater than the index value
}

int main()
{
    Stack myStack;
    initialize(&myStack);

    int item = Pop(&myStack); // This should not work

    Push(1, &myStack);
    Push(2, &myStack);
    Push(3, &myStack);
    Push(4, &myStack); // This should fail

    int numOfItemsInStack = getSize(&myStack);
    printf("\n Number of items in stack %d ", numOfItemsInStack);
    
    int removedItem = 0;

    removedItem = Pop(&myStack);
    printf("\n Item removed from stack is = %d ", removedItem);

    removedItem = Pop(&myStack);
    printf("\n Item removed from stack is = %d ", removedItem);

    removedItem = Pop(&myStack);
    printf("\n Item removed from stack is = %d ", removedItem);

    removedItem = Pop(&myStack);
    printf("\n Item removed from stack is = %d ", removedItem);
    
    removedItem = Pop(&myStack);
    printf("\n Item removed from stack is = %d ", removedItem);

