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

typedef struct node
{
    int data;
    struct node* next;
    struct node* prev;
}Node;

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
    newNode->prev = NULL;
    return newNode;
}

void InsertAtStart(Node** head, int data)
{
    Node* newNode = CreateNewNode(data);
    //Case 1 - List is empty
    if (*head == NULL) 
    {
        //Make the newNode as a head node
        *head = newNode;
        return;
    }

    //Case 2 - List has some nodes
    newNode->next = *head;
    (*head)->prev = newNode;
    *head = newNode; // newNode now becomes head
}

void PrintDoublyLinkedList(Node* head)
{
    if (head == NULL)
    {
        printf("\n List is empty");
        return;
    }

    Node* currentNode = head;
    printf("\n");
    printf("head-->");
    while (currentNode != NULL)
    {
        printf(" %d <--> ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("NULL\n");
}

void InsertAtEnd(Node** head, int data)
{
    Node* newNode = CreateNewNode(data);
    //Case 1 - List is empty
    if (*head == NULL)
    {
        *head = newNode;
        return;
    }

    //Case 2 - List has one or more nodes
    // Travese and reach the last node in the list.
    Node* currentNode = *head;
    while(currentNode->next != NULL)
    {
        currentNode = currentNode->next;
    }
    newNode->prev = currentNode;
    currentNode->next = newNode;
}

void InsertAtGivenPosition(Node** head, int targetPosition, int data)
{
    // Case 1 - invalid target position
    if (targetPosition <= 0)
    {
        printf("\n Invalid position");
        return;
    }

    // Case 2 - insert at start or position 1
    if (targetPosition == 1)
    {
        InsertAtStart(head, data);
        printf("\n Insert a node with value %d at position %d", data, targetPosition);
        return;
    }

    // Find if we can insert element at the given position
    Node* currentNode = *head;
    int count = 1;

    while ( (count < targetPosition-1) && currentNode!=NULL)
    {
        currentNode = currentNode->next;
        count++;
    }

    if (currentNode == NULL)
    {
        printf("\n Invalid target position");
        return;
    }

    Node* newNode = CreateNewNode(data);
    newNode->next = currentNode->next;
    newNode->prev = currentNode;
    
    // If we are inserting in the last position, then we have to do this check
    // to prevent a crash because in that case currentNode->next will be NULL
    if (currentNode->next != NULL)
    {
        currentNode->next->prev = newNode; 
    }
    currentNode->next = newNode;
    printf("\n Insert a node with value %d at position %d", data, targetPosition);
}

void DeleteAtStart(Node** head)
{
    printf("\n Deleting the node at start");
    if (*head == NULL)
    {
        printf("List is empty");
        return;
    }

    // List has only one node
    if ((*head)->next == NULL)
    {
        free(*head);
        *head = NULL;
        return;
    }

    // List has more than one node, 
    // delete the first node, make 2nd node as head
    Node* prevHead = *head;
    *head = (*head)->next;
    (*head)->prev = NULL;

    free(prevHead);
}

void DeleteAtEnd(Node** head)
{
    printf("\n Deleting the node at end");
    if (*head == NULL)
    {
        printf("List is empty");
        return;
    }

    // List has only one node
    if ((*head)->next == NULL)
    {
        free(*head);
        *head = NULL;
        return;
    }

    Node* currentNode = *head;
    while (currentNode->next != NULL)
    {
        currentNode = currentNode->next;
    }
    currentNode->prev->next = NULL;
    free(currentNode);
}

void DeleteAtTargetPosition(Node** head, int targetPosition)
{
    printf("\n Deleting the node at %d position", targetPosition);
    if (*head == NULL)
    {
        printf("List is empty");
        return;
    }

    if (targetPosition <= 0)
    {
        printf("Invalid target position");
        return;
    }

    if (targetPosition==1)
    {
        DeleteAtStart(head);
        return;
    }

    Node* currentNode = *head;
    int count = 1;
    while(count < targetPosition-1 && currentNode != NULL)
    {
        currentNode = currentNode->next;
        count++;
    }

    if (currentNode == NULL)
    {
        printf("Invalid target position");
        return;
    }

    Node* toBeDeletedNode = currentNode->next;
    currentNode->next = toBeDeletedNode->next;
    if (toBeDeletedNode-> next != NULL)
    {
        toBeDeletedNode->next->prev = currentNode;
    }
    free(toBeDeletedNode);
    toBeDeletedNode=NULL;

}

int main()
{
    Node* head = NULL;
    InsertAtStart(&head, 3);
    InsertAtStart(&head, 2);
    InsertAtStart(&head, 1);
    PrintDoublyLinkedList(head);
    InsertAtEnd(&head, 4);
    PrintDoublyLinkedList(head);
    InsertAtGivenPosition(&head, 3, 100);
    PrintDoublyLinkedList(head);
    InsertAtGivenPosition(&head, 1, 0);
    PrintDoublyLinkedList(head);
    InsertAtGivenPosition(&head,7 , 700);
    PrintDoublyLinkedList(head);

    DeleteAtStart(&head);
    PrintDoublyLinkedList(head);

    DeleteAtEnd(&head);
    PrintDoublyLinkedList(head);

    DeleteAtTargetPosition(&head,1);
    PrintDoublyLinkedList(head);
    DeleteAtTargetPosition(&head,-1);
    PrintDoublyLinkedList(head);
    DeleteAtTargetPosition(&head,3);
    PrintDoublyLinkedList(head);
    DeleteAtTargetPosition(&head,3);
    PrintDoublyLinkedList(head);
}