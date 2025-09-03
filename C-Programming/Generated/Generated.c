#include <stdio.h>
#include <stdbool.h>

// Function to get the sum of numbers in an array
int getSum(int numbers[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += numbers[i];
    }
    return sum;
}

// Function to swap two variable values
void swapNumbers(int *number1, int *number2) {
    int temp = *number1;
    *number1 = *number2;
    *number2 = temp;
}

// Function to check if a number is even
bool isEven(int number) {
    return (number % 2 == 0);
}

// Function to check if a character is a digit
bool isDigit(char character) {
    return (character >= '0' && character <= '9');
}

// Function to print simple greetings with a given name
void simpleGreetings(const char *name) {
    printf("Namaskara %s\n", name);
}



int getStringLength(char* str)
{
    int length = 0;

    while(str[length] != '\0')
        length++;
    
    return length;
}

// Function to get the length of a string
int getStrLength(const char *str) {
    int length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}

// Function to count the number of vowels in a string
int getCountOfVowels(const char *str) {
    int count = 0;
    while (*str) {
        char ch = *str;
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            count++;
        }
        str++;
    }
    return count;
}

// Function to reverse a string
void reverseString(char *str) {
    int length = getStrLength(str);
    for (int i = 0; i < length / 2; i++) {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
}

// Function to reverse the elements of an array
void reverseElements(int arr[], int size) {
    for (int i = 0; i < size / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - i - 1];
        arr[size - i - 1] = temp;
    }
}

// Function to check if a string is a palindrome
bool isPalindrome(const char *str) {
    int length = getStrLength(str);
    for (int i = 0; i < length / 2; i++) {
        if (str[i] != str[length - i - 1]) {
            return false;
        }
    }
    return true;
}

// Function to print the maximum and minimum values from an integer array
void printMaxMin(int arr[], int size) {
    int max = arr[0];
    int min = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    printf("Max: %d, Min: %d\n", max, min);
}

// Function to get the sum of all elements in an integer array
int getSumOfArray(int arr[], int size) {
    return getSum(arr, size);
}

// Function to merge two arrays into the first array
void mergeArrays(int arr1[], int size1, int arr2[], int size2) {
    for (int i = 0; i < size2; i++) {
        arr1[size1 + i] = arr2[i];
    }
}

// Function to get the second largest element in an integer array
int getSecondLargest(int arr[], int size) {
    int max = arr[0];
    int secondMax = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            secondMax = max;
            max = arr[i];
        } else if (arr[i] > secondMax && arr[i] != max) {
            secondMax = arr[i];
        }
    }
    return secondMax;
}

// Function to get unique elements in an integer array
void getUniqueElements(int arr[], int size) {
    int unique[size];
    int k = 0;
    for (int i = 0; i < size; i++) {
        int found = 0;
        for (int j = 0; j < k; j++) {
            if (arr[i] == unique[j]) {
                found = 1;
                break;
            }
        }
        if (!found) {
            unique[k++] = arr[i];
        }
    }
    printf("Unique elements: ");
    for (int i = 0; i < k; i++) {
        printf("%d ", unique[i]);
    }
    printf("\n");
}

// Function to get the intersection of two integer arrays
void getCommonElements(int arr1[], int size1, int arr2[], int size2) {
    printf("Common elements: ");
    for (int i = 0; i < size1; i++) {
        for (int j = 0; j < size2; j++) {
            if (arr1[i] == arr2[j]) {
                printf("%d ", arr1[i]);
                break;
            }
        }
    }
    printf("\n");
}

// Function to get the count of words in a string
int getCountOfWords(const char *str) {
    int count = 0, inWord = 0;
    while (*str) {
        if (*str == ' ' || *str == '\n' || *str == '\t') {
            inWord = 0;
        } else if (!inWord) {
            inWord = 1;
            count++;
        }
        str++;
    }
    return count;
}

// Function to get the count of positive and negative numbers in an array
void getPositiveNegativeNumbersCount(int arr[], int size) {
    int positiveCount = 0, negativeCount = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] > 0) {
            positiveCount++;
        } else if (arr[i] < 0) {
            negativeCount++;
        }
    }
    printf("Positive: %d, Negative: %d\n", positiveCount, negativeCount);
}

// Function to remove spaces from a string
void removeSpaces(char *str) {
    int i, j = 0;
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] != ' ') {
            str[j++] = str[i];
        }
    }
    str[j] = '\0';
}


// Function to print binary representation of an integer
void printBinaryOfInteger(int integerValue) {
    unsigned int mask = 1 << (sizeof(int) * 8 - 1); // Mask to extract each bit
    printf("Binary representation of %d: ", integerValue);
    for (int i = 0; i < sizeof(int) * 8; i++) {
        if (integerValue & mask) {
            printf("1");
        } else {
            printf("0");
        }
        mask >>= 1;
    }
    printf("\n");
}

// Function to print binary representation of a character
void printBinaryOfCharacter(char charValue) {
    unsigned int mask = 1 << (sizeof(char) * 8 - 1); // Mask to extract each bit
    printf("Binary representation of '%c': ", charValue);
    for (int i = 0; i < sizeof(char) * 8; i++) {
        if (charValue & mask) {
            printf("1");
        } else {
            printf("0");
        }
        mask >>= 1;
    }
    printf("\n");
}

// Function to perform left shift operation on an integer
void performLeftShiftOperation(int integerValue, int shiftCount) {
    int result = integerValue << shiftCount;
    printf("Left shift %d by %d positions: %d\n", integerValue, shiftCount, result);
}

// Function to perform right shift operation on an integer
void performRightShiftOperation(int integerValue, int shiftCount) {
    int result = integerValue >> shiftCount;
    printf("Right shift %d by %d positions: %d\n", integerValue, shiftCount, result);
}


int main()
{
    printBinaryOfInteger(-1);
    printBinaryOfInteger(-2);
    printBinaryOfInteger(-4);
    printBinaryOfInteger(-8);
}

int test() {
    // Sample inputs
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {6, 7, 8};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int size2 = sizeof(arr2) / sizeof(arr2[0]);

    int number = 10;
    int a = 5, b = 10;

    char name[] = "Alice";
    char str[] = "Hello World";
    char palindrome[] = "madam";
    char strToRemoveSpaces[] = "Remove spaces here";

    // Invoke and test functions
    printf("Sum of numbers in arr1: %d\n", getSum(arr1, size1));
    
    // Swap numbers
    printf("Before swapping: a = %d, b = %d\n", a, b);
    swapNumbers(&a, &b);
    printf("After swapping: a = %d, b = %d\n", a, b);
    
    // Check if number is even
    printf("Is %d even? %s\n", number, isEven(number) ? "Yes" : "No");
    
    // Check if character is a digit
    printf("Is '5' a digit? %s\n", isDigit('5') ? "Yes" : "No");
    
    // Simple greetings
    simpleGreetings(name);
    
    // Print ASCII values
    //printAsciiValues(str);
    
    // Get string length
    printf("Length of \"%s\": %d\n", str, getStrLength(str));
    
    // Count vowels
    printf("Number of vowels in \"%s\": %d\n", str, getCountOfVowels(str));
    
    // Reverse string
    char reversedStr[] = "Hello World";
    reverseString(reversedStr);
    printf("Reversed string: %s\n", reversedStr);
    
    // Reverse array
    int arr1Reversed[] = {1, 2, 3, 4, 5};
    reverseElements(arr1Reversed, size1);
    printf("Reversed arr1: ");
    for (int i = 0; i < size1; i++) {
        printf("%d ", arr1Reversed[i]);
    }
    printf("\n");
    
    // Check if palindrome
    printf("Is \"%s\" a palindrome? %s\n", palindrome, isPalindrome(palindrome) ? "Yes" : "No");
    
    // Print max and min values
    printMaxMin(arr1, size1);
    
    // Get sum of array elements
    printf("Sum of array elements in arr1: %d\n", getSumOfArray(arr1, size1));
    
    // Merge arrays
    int mergedArr[12];
    for (int i = 0; i < size1; i++) {
        mergedArr[i] = arr1[i];
    }
    mergeArrays(mergedArr, size1, arr2, size2);
    printf("Merged array: ");
    for (int i = 0; i < size1 + size2; i++) {
        printf("%d ", mergedArr[i]);
    }
    printf("\n");
    
    // Get second largest element
    printf("Second largest element in arr1: %d\n", getSecondLargest(arr1, size1));
    
    // Get unique elements
    int uniqueArr[] = {1, 2, 2, 3, 4, 4, 5};
    printf("Unique elements: ");
    getUniqueElements(uniqueArr, sizeof(uniqueArr) / sizeof(uniqueArr[0]));
    
    // Get common elements
    printf("Common elements between arr1 and arr2: ");
    getCommonElements(arr1, size1, arr2, size2);
    
    // Get count of words
    printf("Word count in \"%s\": %d\n", str, getCountOfWords(str));
    
    // Get count of positive and negative numbers
    int positiveNegativeArr[] = {-1, 2, -3, 4, -5, 6};
    getPositiveNegativeNumbersCount(positiveNegativeArr, sizeof(positiveNegativeArr) / sizeof(positiveNegativeArr[0]));
    
    // Remove spaces
    removeSpaces(strToRemoveSpaces);
    printf("String after removing spaces: \"%s\"\n", strToRemoveSpaces);
    
    // Bitwise operators

    int integerValue = 29;
    char charValue = 'A';
    int shiftCount = 2;

    // Print binary representation of integer
    printBinaryOfInteger(integerValue);

    // Print binary representation of character
    printBinaryOfCharacter(charValue);

    // Perform left shift operation on integer
    performLeftShiftOperation(integerValue, shiftCount);

    // Perform right shift operation on integer
    performRightShiftOperation(integerValue, shiftCount);

    
    return 0;
}
