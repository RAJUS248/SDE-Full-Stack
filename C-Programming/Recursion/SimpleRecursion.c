#include <stdio.h>

void printNumbers(int count) {
    // Increment the count
    count = count + 1;
    // Print the current count
    printf("%d\n", count);
    // Recursively call the function with the new count
    printNumbers(count);
}

int main() {
    // Start the recursion with initial value 1
    printNumbers(1);
    return 0;
}
