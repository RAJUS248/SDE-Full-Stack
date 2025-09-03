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
} Node;

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

void InsertAtStart(Node** tail, int data)
{
      Node* newNode = CreateNewNode(data);
    //Case 1 - List is emtpy
    if (*tail == NULL)
    {
        newNode->next = newNode;
        *tail = newNode;
        return;
    }
    
    // Case 2 - There are one or more nodes
    newNode->next = (*tail)->next;
    (*tail)->next = newNode;
    return;
}

void InsertAtTail(Node** tail, int data)
{
    Node* newNode = CreateNewNode(data);
    //Case 1 - List is emtpy
    if (*tail == NULL)
    {
        newNode->next = newNode;
        *tail = newNode;
        return;
    }
    
    // Case 2 - There are one or more nodes
    newNode->next = (*tail)->next;  // New node to be linked to first node
    (*tail)->next = newNode; // Node at tail is linked to the new node 
    *tail = newNode; // Newly added node becomes a new tail node
    return;
}

void PrintCicularList(Node* tail)
{
    if (tail == NULL)
    {
        printf("\n List is emtpy");
        return;
    }

    printf("\n"); 
    Node* currentNode = tail->next; // Set the currentNode to the first node in the list or head of the list
    
    do
    {
        printf("%d --> ", currentNode->data);
        currentNode = currentNode->next;
    } while( currentNode != tail->next);

}

Node* DeleteAtStart(Node* tail)
{
    //Case 1 - List is empty
    if (tail == NULL)
    {
        return NULL;
    }

    //Case 2 - Only one node is present 
    if (tail->next == tail)
    {
        free(tail);
        return NULL;
    }

    // Case 3 - More than one node exist 
    Node* head = tail->next;
    tail->next = head->next;
    free(head);
    head = NULL;
    return tail;
}

Node* DeleteAtEnd(Node* tail)
{
    // Case 1 - List is emtpy
    if (tail == NULL)
    {
        return NULL;
    }

    //Case 2 - Only one node is present 
    if (tail->next == tail)
    {
        free(tail);
        return NULL;
    }

    // Case 3 - More than one node is present 
    Node* currentNode = tail->next;
    while(currentNode->next != tail)
    {
        currentNode = currentNode->next;
    }
    currentNode->next = tail->next;
    free(tail);
    return currentNode;
}

int main()
{
    Node* tail = NULL;
    InsertAtTail(&tail, 1);
    PrintCicularList(tail);

    InsertAtTail(&tail, 2);
    InsertAtTail(&tail, 3);
    InsertAtTail(&tail, 4);
    PrintCicularList(tail);


    InsertAtStart(&tail, 0);
    InsertAtStart(&tail, -1);
    PrintCicularList(tail);

    tail = DeleteAtStart(tail);
    PrintCicularList(tail);

    tail = DeleteAtStart(tail);
    PrintCicularList(tail);

    tail = DeleteAtEnd(tail);
    PrintCicularList(tail);

    tail = DeleteAtEnd(tail);
    PrintCicularList(tail);

    tail = DeleteAtEnd(tail);
    PrintCicularList(tail);

}