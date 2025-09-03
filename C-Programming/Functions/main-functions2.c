#include<stdio.h>

void printCompanyName(); // Function declaration
int printMessage(char message[]); // Function declaration

int main()
{
    // Function invocation
    printCompanyName();

    int totalCount = printMessage("How are you?");
    printf("Value returned by function is = %d", totalCount);

    return 0;
}

// Function definition
void printCompanyName()
{
    printf("Welcome to algorithms365!"); // Function invocation
}

// Function definition
int printMessage(char message[])
{
    int count = 0;
    count = printf("\n Message is %s", message);
    return count;
}
