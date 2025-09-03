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

typedef struct node {
    int data;
    struct node* next;
}Node;

typedef struct queue {
    struct node* rear;
    struct node* front;
} Queue;

void initializeQueue(Queue* pQueue)
{
    pQueue->front = NULL;
    pQueue->rear = NULL;
}

Node* CreateNewNode(int data)
{
    Node* newNode = (Node*) malloc(sizeof(Node));

    if (newNode == NULL)
    {
        printf("Failed to allocate memory!");
        return NULL;
    }

    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}


void enqueue(Queue* pQueue, int data)
{
    Node* newNode = CreateNewNode(data);

    if (newNode == NULL)
    {
        printf("\n Memory is full");
        return;
    }

    if (pQueue->rear == NULL)
    {
        pQueue->rear = newNode;
        pQueue->front = newNode;
    }
    else 
    {
        pQueue->rear->next = newNode;
        pQueue->rear = newNode;
    }
    printf(" \n Value %d added to the queue ", data);
}

int peek(Queue* pQueue)
{
    if (pQueue->front == NULL)
    {
        printf("Queue is empty");
        return -1;
    }

    return pQueue->front->data;
}

int dequeue(Queue* pQueue)
{
    if (pQueue->front == NULL)
    {
        printf("\n Queue is empty!");
        return -1;
    }

    int data = pQueue->front->data;
    Node* temp = pQueue->front;
    pQueue->front = pQueue->front->next;
    free(temp);
    return data;
}

void printQueue(Queue* pQueue)
{
    Node* pNode = pQueue->front;

    printf("\n elements in the queue ..");
    while (pNode != NULL)
    {
        printf(" %d --> ", pNode->data);
        pNode = pNode->next;
    }
}

int main()
{
   Queue queue;
   initializeQueue(&queue);

   enqueue(&queue, 10);
   enqueue(&queue, 20);
   enqueue(&queue, 30);

   printQueue(&queue);

   int data = peek(&queue);
   printf("\n Value at the top of the queue  is %d ", data);

   data = dequeue(&queue);
   printf("\n Value removed is %d ", data);

   printQueue(&queue);

   data = dequeue(&queue);
   printf("\n Value removed is %d ", data);

   data = dequeue(&queue);
   printf("\n Value removed is %d ", data);

   data = dequeue(&queue);
   printf("\n Value removed is %d ", data);
    

    
}