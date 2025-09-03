#include <stdio.h>
#include <stdbool.h>

int sum = 0; // Global variable

// Function getSum to get Sum of two numbers
int getSum(int number1, int number2) 
{
    // sum is a local variable 
    // Scope is till end of the function
    int sum = number1 + number2;
    return sum;
}
// Pass by value
void getSum_V2(int number1, int number2) 
{
    // sum is a local variable 
    // Scope is till end of the function
    sum = number1 + number2;    
}

void getSumInvoke()
{
    int n1, n2; // Variable declare 
    n1 = 10; // Variable initialization 
    n2 = 20;

    // getSum(n1, n2);  // Function invocation

    // printf("Sum = %d", getSum(n1, n2));

    //printf("Sum of two number = %d is this correct? ", answer);

   // getSum_V2(100, 200);

    //printf("Sum of two number = %d", sum);
}

//Pass by reference (address)
void swapNumbers(int *number1, int *number2)
{
    int tempNum = *number1 ;
    *number1 = *number2;
    *number2 = tempNum;
}

void invoke_swapNumbers()
{
    int number1 = 10;
    int number2 = 20;

    printf("Before : Num1 = %d Num2 = %d", number1, number2);
    swapNumbers(&number1, &number2);
    printf("After : Num1 = %d Num2 = %d", number1, number2);

}

bool isEven(int number)
{
    if (number % 2 == 0)
    {
        return true;
    }
    else 
    {
        return false;
    }
}

void invoke_isEven()
{
    int number = 11;
    bool result = isEven(number);

    if (result == true)
        printf("%d is even number", number);
    else
        printf("%d is odd number", number);
}


// Workshop demo of good coding skill 

bool function1(char *n) {
    for(int i = 0; n[i]; i++)
        if(n[i] < '0' || n[i] > '9') return 0;
    return 1;
}

























bool isNumber_v1(char number[])
{
    bool isNumber = true;

    for(int index = 0; number[index] != '\0'; index++)
    {
        if (number[index] >= '0' && number[index] <= '9')
            continue;
        else
        {
            isNumber = false;
            break;
        }
    }
    return isNumber;
}












//Function isNumber to return true if it is a number
bool isNumber(char number[])
{
    bool isNumber = true; // Make assumption that input is a number

    for(int index = 0; number[index] != '\0'; index++)
    {
        // Check whether each character is between 0 to 9
        if (number[index] >= '0' && number[index] <= '9')
            continue;
        else
        {
            // We have a char which is not between 0 and 9
            isNumber = false;
            break;
        }

    }

    return isNumber;
}

bool isNumberWhile(char number[])
{
    bool isNumber = true; // Make assumption that input is a number
    int index = 0;

    while(number[index] != '\0')
    {
        //printf("\n %c", number[index]);
        // Check whether each character is between 0 to 9
        if (number[index] >= '0' && number[index] <= '9')
        {
            index++;
            continue;
        }
        else
        {
            // We have a char which is not between 0 and 9
            isNumber = false;
            break;
        }

        index++;
    }

    return isNumber;
}


void invoke_isNumber()
{
    char number[] = "a123";
    int number_int = 123;

    //bool result = isNumber(number);

    bool result = isNumber(number);

    if (result)
        printf("This is a proper number");
    else
        printf("This is a invalid number");
}

// Function  simpleGreetings to accept name as input and print simple greetings Namaskara name
void greetingsToUser()
{
    char name[2];

    printf("\n Please enter your name: ");
    scanf("%s", name);

    printf("\nNamaskara %s", name);

}

void printASCII(char string[])
{
    for(int index=0; string[index] != '\0'; index++)
    {
        printf("\n %c --> %d", string[index],string[index]);
    }
}

void invoke_printASCII()
{
    printASCII("1234abcdABCD*+-");
}

//Function to get string length
// This function counts number of characters in the string. 
int getStringLength(char* string)
{
    int length = 0;

    while (string[length] != '\0')
    {
        length++;
    }

    return length;
}

void invoke_stringLength()
{
    char str[] = "algorithms" ;
    int len = getStringLength(str);
    printf("String length %s = %d", str, len);
}


// Count number of vowels in a string 
// a e i o u A E I O U

int getCountVowels(char string[])
{
    int countVowels = 0;
    int index = 0;

    while(string[index] != '\0')
    {
        if (string[index] == 'a'
        || string[index] == 'e'
        || string[index] == 'i'
        || string[index] == 'o'
        || string[index] == 'u'
        || string[index] == 'A'
        || string[index] == 'E'
        || string[index] == 'I'
        || string[index] == 'O'
        || string[index] == 'U')
        {
            countVowels++;
        }

        index++;
    }

    return countVowels;
}

int getCountVowelsV2(char string[])
{
    int countVowels = 0;
    char vowels[] = "aeiouAEIOU";

    // Iterate over each character from the input to the function
    for(int index=0; string[index] != '\0' ; index++)
    {
        // Iterate over list of vowels 
        for(int vowelsIndex=0; vowels[vowelsIndex] != '\0'; vowelsIndex++)
        {
            // If you see a match , increase the count
            if (string[index] == vowels[vowelsIndex])
                countVowels++;
        }
    }

    return countVowels;
}

void invoke_countOfVowels()
{
    char name[] = "algo";
    int count = getCountVowels(name);
    printf("\nCount of vowels in %s = %d", name, count);

    count = getCountVowelsV2(name);
    printf("\nCount of vowels in %s = %d", name, count);
}


// Reversing the string in memory
void reverseString(char string[])
{
    // Input : abcd  output: dcba  - even number 
    // input:  abc  output:  cba - odd characters 
    int endIndex = getStringLength(string) - 1;
    int startIndex = 0;

    for (; startIndex < endIndex; startIndex++, endIndex-- )
    {
        char tempChar = string[startIndex];
        string[startIndex] = string[endIndex];
        string[endIndex] = tempChar;
    }

}

void invoke_reverseString()
{
    char name[] = "algor";
    printf("\nBefore reversing %s", name);
    reverseString(name);
    printf("\nAfter reversing %s", name);

}

//Function to get sum of all elements in the integer array getSum

// get sum -> return interer
// from -> function arguments interger array

int getSumForArray(int numbers[], int count)
{
    int sum=0;

    for (int index=0; index < count; index++)
    {
        sum = sum + numbers[index];
        //sum += numbers[index];
    }

    return sum;
}

int getSumForArray_Bug(int numbers[])
{
    int sum=0;
    //int count = sizeof(numbers) / sizeof(numbers[0]);
    int count = 5;
    for (int index=0; index < count; index++)
    {
        sum = sum + numbers[index];
        //sum += numbers[index];
    }

    return sum;
}


void invoke_getSumArray()
{
    int numbers[] =  {1, 2, 3, 10, 11};
    // int size = 3;

    int size = sizeof(numbers) / sizeof(numbers[0]);

    int sum = getSumForArray(numbers, size);

    printf("Sum of the elements in array = %d", sum);

}

//Function to find given string is Palindrome, function isPalidrome returns true if string is palindrome

bool isPalindrome(char str[])
{
    int length = 0;
    while (str[length]!= '\0')
        length++;
    
    int fromStartIndex = 0;
    int fromEndIndex = length -1;
    bool result = true;

    while (fromStartIndex < fromEndIndex)
    {
        if (str[fromStartIndex] != str[fromEndIndex])
        {
            result = false;
            break;
        }
        fromStartIndex++; // fromStartIndex = fromStartIndex + 1
        fromEndIndex--;
    }

    return result;
}

void invoke_isPalindrome()
{
    char oddStr[] = "abcba";
    char evenStr[] = "abba";
    char oddStrNotPalindrome[] =  "abcde";
    char evenStrNotPalindrome[] =  "abcdef";

    //bool result = isPalindrome(oddStr);
    //bool result = isPalindrome(evenStr);
    bool result = isPalindrome(oddStrNotPalindrome);
    //bool result = isPalindrome(evenStrNotPalindrome);

    if (result) //  if (result == true)
    {
        printf("Given string is palindrome");
    }
    else
    {
        printf("Given string is NOT palindrome");
    }
}

//Function to print max and min value from an integer array ,  printMaxMin

void printMaxMinValues(int numbers[], int size)
{
    int max = numbers[0];
    int min = numbers[0];

    for(int index = 1; index < size; index++)
    {
        if (numbers[index] > max)
            max = numbers[index];
        
        if (numbers[index] < min)
            min = numbers[index];
    }

    printf("\nMaxium value in the array is %d ", max);
    printf("\nMinimum value in the array is %d ", min);

}

void invoke_maxmin()
{
     int numbers[] = {2, -5, 4 ,8, 6}; // Max 8, Min -5
    //int numbers[] = {-2, -5, -4 ,-8, -6}; // Max -2, Min -8
    
    int count = sizeof(numbers) / sizeof(numbers[0]);
    printMaxMinValues(numbers, count);
}

//Function to search in an sorted integer array in asending order
// return the index in which key is found
// If not found then return -1

int search(int numbers[], int key, int size)
{
    int keyIndex = -1;
    int left = 0;
    int right = size -1;
    int mid = 0;

    while (left <= right)
    {
        mid = left + (right - left ) / 2;

        // This is when key is found
        if (numbers[mid] == key)
        {
            keyIndex = mid;
            break;
        }

        // Most likely key can be found on the right side part of the array
        // Adjust the left index
        if (numbers[mid] < key)
        {
            left = mid+1;
        }
        else 
        {
            // Most likely key can be found on the left side of the array
            right = mid-1;
        }
    }

    return keyIndex;
}

// a.k.a Binary Search 

void invoke_search()
{
    int numbers[] = {1, 2, 5, 10, 11, 13};
    int key = 2;
    int size = sizeof(numbers) / sizeof(numbers[0]);

    int indexFound = search(numbers, key, size);

    if (indexFound == -1)
    {
        printf("\nKey is not found");
    }
    else
    {
        printf("\nKey %d is found at index %d", key, indexFound);
        printf("\nElement at that index %d", numbers[indexFound]);
    }
}

//Function to merge two arrays and return combined output in first array
// Input -> two integer arrays, sizes, 
// ouput -> void

void printElementsInArray(int numbers[], int size)
{
    printf("\n[");
    for( int index=0; index < size; index++)
    {
        if (index != 0)
            printf(",%d ", numbers[index]);
        else
            printf("%d ", numbers[index]);
    }
    printf("]\n");
}

void appendElementsOrginalArray(int numbers[], int numbersCount, 
        int additionalNumbers[], int additionalNumbersCount)
{
    for (int index=0; index < additionalNumbersCount; index++, numbersCount++)
    {
        numbers[numbersCount] = additionalNumbers[index];
    }
}

void invokeMergeArray()
{
    int numbers[] = {1, 2, 3, 0, 0, 0};
    int additionalNumbers[] = {4, 5, 6};

    int numbersCount = sizeof(numbers)/ sizeof(numbers[0]);
    int additionalNumbersCount = sizeof(additionalNumbers)/ sizeof(additionalNumbers[0]);

    printElementsInArray(numbers, numbersCount);
    printElementsInArray(additionalNumbers, additionalNumbersCount);

    int orgArraySize = numbersCount-additionalNumbersCount;
    appendElementsOrginalArray(numbers, orgArraySize, additionalNumbers, additionalNumbersCount);

    printElementsInArray(numbers, numbersCount);
}

//Function get second largest element in an integer array  getSecondLargest
// Input array
// ouput second largest element

int getSecondLargest(int numbers[], int size)
{
    int maxLarge = numbers[0];
    int maxSmall = numbers[0];

    for (int index=1; index<size; index++)
    {
        if (numbers[index] < maxSmall)
            continue;
        else if (numbers[index] > maxLarge)
            {
                maxSmall = maxLarge;
                maxLarge = numbers[index];
            }
        else if (numbers[index] > maxSmall && numbers[index] != maxLarge )
            maxSmall = numbers[index];
    }

    return maxSmall;
}

void invoke_secondLargest()
{
    //int numbers[] = {9,11,1,24,8,1,25};
    int numbers[] = {5,4,3,2,1};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    int result = getSecondLargest(numbers, size);

    printf("\nSecond largest element is %d ", result);

}


//Function to print unique elements in an integer array   printUniqueElements

void printUniqueElements(int numbers[], int size)
{
    // This loop is to iterate over elements one by one
    for (int selectIndex=0; selectIndex < size; selectIndex++)
    {
        bool isDuplicate = false; // red, edu duplicate ella
        // This is for comparing with all the other elements in the array
        for (int compareIndex=selectIndex+1; compareIndex< size; compareIndex++)
        {
            if (selectIndex == compareIndex)
                continue;

            if (numbers[selectIndex] == numbers[compareIndex] )
            {
                // If duplicate is found, set state and terminate inner loop / comparing loop
                isDuplicate = true; // duplicate ede
                break;
            }
        }

        if (!isDuplicate) // (isDuplicate == false)
            printf("\n Unique element %d ", numbers[selectIndex]);

    }
}

void invoke_printUniqueElements()
{
    int numbers[] = {1,2,3,4,5,6,7};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    printUniqueElements(numbers, size);
}


//Function to print intersection or common elements of two integer arrays  getCommonElements
void printCommonFriendsIds(int user1[], int user1Count, int user2[], int user2Count)
{
    // Loop to go over all IDs for user1
    for (int user1Index = 0; user1Index < user1Count; user1Index++)
    {
        for (int user2Index = 0; user2Index < user2Count; user2Index++)
        {
            if (user1[user1Index] == user2[user2Index])
            {
                // There is common friend
                printf("\n common friend ID is %d ", user1[user1Index]);
            }
        }
    }
}

void invoke_commonFriends()
{
    int user1[] = { 4, 8, 11, 9};
    int user2[] = { 8, 13, 5, 4};

    int user1Count = sizeof(user1) / sizeof(user1[0]);
    int user2Count = sizeof(user2) / sizeof(user2[0]);

    printCommonFriendsIds(user1, user1Count, user2, user2Count);

}

//Function to get count of words in the string  getCountOfWords

int getCountOfWords(char string[])
{
    int countOfWords = 0;
    int index = 0;

    if (string == NULL || string[0] == '\0')
        return countOfWords;
    
    // There is atleast one word
    countOfWords = 1;
    while(string[index] != '\0')
    {
        if (string[index] == ' ' || string[index] == '\t' || string[index] =='\n')
        {
            countOfWords++;
        }

        index++;
    }

    return countOfWords;
}

void invoke_getCountOfWords()
{
       //char string[] = "India is a great country";

    char string[] = "India";
    
    int count = getCountOfWords(string);
    printf("\nCount of words is = %d", count);
}

void printBinaryOfInteger(int number)
{
    unsigned int mask = 1;  // 00000000000001
    int countOfBits = sizeof(number) * 8 ;

    printf("\n");
    mask = mask << countOfBits - 1;
    for (int times=0; times< countOfBits; times++)
    {
        if (number & mask)
        {
            printf("1 ");
        }
        else
        {
            printf("0 "); 
        }
        mask = mask >> 1;
    }
}


void invoke_printBinaryOfInteger()
{
    printBinaryOfInteger(-1);
    printBinaryOfInteger(-2);
    printBinaryOfInteger(-4);
    printBinaryOfInteger(-8);
    printBinaryOfInteger(16);
    printBinaryOfInteger(32);
    printBinaryOfInteger(64);
    printBinaryOfInteger(128);
    printBinaryOfInteger(256);
    printBinaryOfInteger(512);
    printBinaryOfInteger(1024);
}

void printBinaryOfChar(char input)
{
    unsigned int mask = 1;  // 00000000000001
    int countOfBits = sizeof(char) * 8 ;

    printf("\n");
    mask = mask << countOfBits - 1;
    for (int times=0; times< countOfBits; times++)
    {
        if (input & mask)
        {
            printf("1");
        }
        else
        {
            printf("0"); 
        }
        mask = mask >> 1;
    }
}

void BitwiseShiftOperations(int number, int shiftCount, bool isRightShift)
{
    printf("\nBefore the operation value is %d \n", number);
    printBinaryOfInteger(number);

    if (isRightShift)
    {
        number = number >> shiftCount;
        printf("\nAfter the right shift operation value is %d \n", number);
    }
    else
    {
        number = number << shiftCount;
        printf("\nAfter the ;eft shift operation value is %d \n", number);
    }
    printBinaryOfInteger(number);
}

void invoke_bitwiseOperations()
{
    int number = 1;
    BitwiseShiftOperations(number,1, false);
    BitwiseShiftOperations(number,5, false);

    number = 32;
    BitwiseShiftOperations(number,1, true);
}

//Function to remove spaces from the string  removeSpaces

void removeSpaces(char string[])
{
    int readIndex =0, writeIndex =0;

    printf("\nBefore removing spaces %s ", string);
    // Read one character at a time from the string till the end of the string
    while(string[readIndex] != '\0') 
    {
        // If we do not encounter a space then copy it (in-memory)
        if (string[readIndex] != ' ') 
        {
            string[writeIndex] = string[readIndex];
            writeIndex++;
        }
        readIndex++;
    }
    string[writeIndex] = '\0';
    printf("\nAfter removing spaces %s ", string);
}


void invoke_removeSpaces()
{
    char string[] = "a b c d e";
    removeSpaces(string);
}

// Implementation of the function or definition or defining the function
int main()
{
   // invoke_secondLargest();
   invoke_isNumber();
}