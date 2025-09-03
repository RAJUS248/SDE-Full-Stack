#include <stdio.h>

int main() {
    int num1, num2, sum;

    // Prompt the user to enter two numbers
    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    // Calculate the sum of the two numbers
    sum = num1 + num2;

    // Print the sum
    printf("The sum of %d and %d is %d\n", num1, num2, sum);

    return 0;
}
