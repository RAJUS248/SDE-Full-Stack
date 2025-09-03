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
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 3

typedef struct 
{
    int items[MAX_SIZE];
    int frontIndex;
    int rearIndex;
} Queue;



void initializeQueue(Queue* pQueue)
{
    pQueue->frontIndex = -1;
    pQueue->rearIndex = -1;
}

bool isQueueFull(Queue* pQueue)
{
    if ( (pQueue->rearIndex + 1) % MAX_SIZE  == pQueue->frontIndex)
        return true;
    else
        return false;

}

bool isQueueEmpty(Queue* pQueue)
{
    if (pQueue->frontIndex == -1)
    {
        return true;
    }
    else
    {
        return false;
    }

}

void printQueue(Queue queue)
{
    printf("\n\n Elements in the queue \n");
    for (int index =0; index < MAX_SIZE; index++)
    {
        printf("\t [ %d ] --> %d ", index, queue.items[index]);
    }

    printf("\n frontIndex = %d  rearIndex = %d", queue.frontIndex, queue.rearIndex);
}

 

void enqueue(Queue* pQueue, int item)
{
    // Check if queue is full
    if (isQueueFull(pQueue))
    {
        printf("\n\n Insert %d  to queue failed, queue is full\n ", item);
        return;
    }

    // Insert elements from at the rear end
    //pQueue->rearIndex = pQueue->rearIndex + 1;
    pQueue->rearIndex = (pQueue->rearIndex + 1 ) % MAX_SIZE;
    pQueue->items[pQueue->rearIndex] = item;

    if (pQueue->frontIndex == -1)
    {
        // We are inserting an element when queue is empty, hence increment the frontIndex
        pQueue->frontIndex++;
    }
}

int dequeue(Queue* pQueue)
{
    if (isQueueEmpty(pQueue))
    {
        printf("\n Queue is empty!");
        return -1;
    }
    
    int item = pQueue->items[pQueue->frontIndex];
    //pQueue->frontIndex++;

    if (pQueue->frontIndex == pQueue->rearIndex) // There is only one element which we will remove
    {
        pQueue->frontIndex = -1;
        pQueue->rearIndex = -1;
    }
    else 
    {
        pQueue->frontIndex = ( pQueue->frontIndex + 1 ) % MAX_SIZE;
    }
    
    return item;
}

int peek(Queue* pQueue)
{
    return pQueue->items[pQueue->frontIndex];
}

int main()
{
    Queue queue;
    initializeQueue(&queue);
    printQueue(queue);

    enqueue(&queue, 10);
    printQueue(queue);

    enqueue(&queue, 20);
    printQueue(queue);


    int item = dequeue(&queue);
    printf("\n Value removed from the queue is %d ", item);
    printQueue(queue);

    
    item = dequeue(&queue);
    printf("\n Value removed from the queue is %d ", item);
    printQueue(queue);

   
    item = dequeue(&queue);
    printf("\n Value removed from the queue is %d ", item);
    printQueue(queue);

    
}