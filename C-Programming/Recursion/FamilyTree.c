#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a Node structure
typedef struct Node {
    char name[50];
    struct Node *father;
} Node;

// Function to create a new node
Node* createNode(const char* name) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    strcpy(newNode->name, name);
    newNode->father = NULL;
    return newNode;
}

// Function to create the hardcoded family tree
Node* create_family_tree_hardcoded() {
    // Hardcoded family tree names
    const char* names[] = {"Pralhad", "Hiranyakashapa", "Kashayapa Brahma", "Chaturmukha Brahma", "I don't know"};
    int n = sizeof(names) / sizeof(names[0]);

    // Create an array of nodes
    Node *nodes[n - 1];  // Exclude the last "I don't know"

    // Create nodes from the names list
    for (int i = 0; i < n - 1; i++) {
        nodes[i] = createNode(names[i]);
    }

    // Link nodes to form the tree
    for (int i = 0; i < n - 2; i++) {
        nodes[i]->father = nodes[i + 1];
    }

    // Return the root of the tree (the last generation individual)
    return nodes[0];
}

// Function to print the family tree
void print_family_tree(Node *node) {
    if (node != NULL) {
        printf("%s\n", node->name);
        print_family_tree(node->father);
    }
}

// Main function
int main() {
    Node *root = create_family_tree_hardcoded();
    printf("Family Tree:\n");
    print_family_tree(root);

    // Free allocated memory
    Node *current = root;
    while (current != NULL) {
        Node *temp = current;
        current = current->father;
        free(temp);
    }

    return 0;
}
