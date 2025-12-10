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



Node* CreateNewNode(int data)
{
    // Stack
    Node mynode; 
    mynode.data = 10;
    mynode.next = NULL;

    // Heap
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = 10;
    newNode->next = NULL;

    if (newNode == NULL)
    {
        printf("Failed to allocate memory!");
        return NULL;
    }

    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert operations 

//1 - Insert at start

void InsertAtStart(int data, Node** head)
{
    Node* newNode = CreateNewNode(data);

    // Case 1 - List is empty
    if (*head == NULL)
    {
        *head = newNode;
        return;
    }

    // Case 2 - List has some elements 
    newNode->next = *head;
    *head = newNode;
}

void PrintList(Node* head)
{
    Node* currentNode = head;

    // Case 1 - list is empty
    if (head == NULL)
    {
        printf("\n List is empty");
        return;
    }

    //Case 2 - There are some nodes, we have to traverse one node at a time
    printf("\n head-->");
    //while (currentNode->next != NULL)   //This will skip last node and it is not correct
    while (currentNode != NULL)
    {
        printf(" %d --> ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("NULL\n");
}

void SearchKey(Node* head, int key)
{
    if (head == NULL)
    {
        printf("\n List is empty");
        return;
    }

    Node* currentNode = head;
    while(currentNode != NULL)
    {
        if (currentNode->data == key)
        {
            printf("\n Key is present in the node ");
            return;
        }
        currentNode = currentNode->next;
    }

    printf("\n Key is not found in the list");
}

void InsertAtEnd(int data, Node** head)
{
    Node* newNode = CreateNewNode(data);

    // Case 1 - List is empty
    if (*head == NULL)
    {
        *head = newNode;
    }

    // Case 2 - List has some nodes 
     Node* currentNode = *head;
    while(currentNode->next != NULL)
    {
        currentNode = currentNode->next;
    }
    currentNode->next = newNode;
}

void insertAtPosition(Node** head, int data, int position)
{
    printf("\n Insert %d at position %d ", data, position);
    // Case 1 - list is emtpy
    if (*head == NULL)
    {
        printf("\n List is empty");
        return;
    }
    // Case 2 - insert at first position 
    if (position == 1)
    {
        InsertAtStart(data, head);
        return;
    }

    // Case 3 - Insert at position greater than 1
    Node* currentNode = *head;
    int currrentPosition = 1;

    while ((currrentPosition < position -1) && currentNode != NULL)
    {
        currrentPosition++;
        currentNode = currentNode->next;
    }

    // Handle the invalid input
    if (currentNode == NULL)
    {
        printf("Can't insert at this position, there are less nodes");
        return;
    }

    Node* newNode = CreateNewNode(data);
    newNode->next = currentNode->next;
    currentNode->next = newNode;
}

void DeleteAtStart(Node** head)
{
    if (*head == NULL)
    {
        printf("\n List is empty");
        return;
    }

    Node* temp = *head;
    *head = (*head)->next;
    free(temp);
    printf("\nDeleted the first node");
}

void DeleteAtEnd(Node** head)
{
    //Case 1 - Empty list
    if (*head == NULL)
    {
        printf("\n List is empty");
        return;
    }

    // Case 2 - single node 
    if ((*head)->next == NULL)
    {
        free(*head);
        *head = NULL;
    }

    //Case 3 - two or more nodes in the list 
    Node* currntNode = *head;
    while (currntNode->next->next != NULL)
    {
        currntNode = currntNode->next;
    }
    free(currntNode->next);
    currntNode->next = NULL;
    printf("\n Node at the start has been deleted");

}

void DeleteAtPosition(Node** head, int position)
{
    //Case 1 - Empty list
    if (*head == NULL)
    {
        printf("\n List is empty");
        return;
    }

    // Case 2 - delete at position 1
    if (position == 1)
    {
        DeleteAtStart(head);
        return;
    }

    //Case 3 - Del at position greater than or equal to 2

    int currentPosition = 1;
    Node* currentNode = *head;

    while((currentPosition < position-1) && currentNode != NULL )
    {
        currentNode = currentNode->next;
        currentPosition++;
    }

    if (currentNode == NULL)
    {
        printf("\n Can't perform this operation");
        return;
    }

    Node* temp= currentNode->next;
    currentNode->next = temp->next;
    free(temp);
    printf("Deleted node at position %d ", position);
}

void DeleteFirstOccurance(Node** head, int data)
{
    
    printf("\n Delete the first occurance of node with value %d", data);
    //Case 1 - Empty list
    if (*head == NULL)
    {
        printf("\n List is empty");
        return;
    }

    // case 2 - If node to delete is the first node
    // This will handle single node and multi node senario
    if ((*head)->data == data)
    {
        Node* temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }

    // Case 3 - Only one node is present
    if ((*head)->next == NULL)
    {
        printf("Node doesn't exist with value %d to delete", data);
        return;
    }

    // Case 4 - 2 or more nodes exist, we need search in the list
    Node* finder = *head;
    Node* follower = NULL;

    while(finder->next != NULL)
    {
        follower = finder;
        finder = finder->next;

        if (finder->data == data)
        {
            // perform the operation to delete and terminate the loop
            follower->next = finder->next;
            free(finder);
            finder = NULL;
            printf("\n Deleted the node with value %d ", data);
            return;
        }
    }
    printf("Node doesn't exist with value %d to delete", data);
}

int main()
{
    printf("\nSingly linked list demo!\n");
    Node* head = NULL;

    // Part 1 & 2
    head = CreateNewNode(4);

    InsertAtStart(3, &head);
    InsertAtStart(2, &head);
    InsertAtStart(1, &head);

    PrintList(head);

    SearchKey(head, 3);

    InsertAtEnd(5,&head);
    PrintList(head);

    //Part 3
    insertAtPosition(&head, 100, 3);
    PrintList(head);

    insertAtPosition(&head, 200, 1);
    PrintList(head);

    insertAtPosition(&head, 700, 7);
    PrintList(head);

    insertAtPosition(&head, 900, 9);
    PrintList(head);

    insertAtPosition(&head, 1500, 15);
    PrintList(head);

    DeleteAtStart(&head);
    PrintList(head);

    DeleteAtEnd(&head);
    PrintList(head);

    DeleteAtPosition(&head, 3);
    PrintList(head);

    DeleteAtPosition(&head, 1);
    PrintList(head);

    DeleteAtPosition(&head, 10);
    PrintList(head);

    DeleteAtPosition(&head, 5);
    PrintList(head);

    DeleteFirstOccurance(&head, 2);
    PrintList(head);

    DeleteFirstOccurance(&head, 900);
    PrintList(head);

    DeleteFirstOccurance(&head, 700);
    PrintList(head);
}