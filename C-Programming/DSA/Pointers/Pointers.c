/* Pointers: One of the most important concepts in programming */
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

void doubleTheValue(int value)
{
    value = value * 2;
}

void doubleTheValueWorks(int* pValue)
{
    int data = *pValue;
    data = data * 2;
    *pValue = data;
}

// Pass variables by reference 
// Pointers - reference types 
void swapValues(int* pNumber1, int* pNumber2)
{
    int temp = *pNumber2;
    *pNumber2 = *pNumber1;
    *pNumber1 = temp;
}

void swapValuesDemo()
{
    int number1=10, number2=20;
    printf("\n Before swapping number 1 = %d , number2 = %d ", &number1, &number2);
    swapValues(&number1, &number2);
    printf("\n After swapping number 1 = %d , number2 = %d ", &number1, &number2);
}

void SinglePointerDemo()
{
    int number = 10;      // Variable
    int* pNumber = &number; // Single pointer: Special variable which stores address of other variable
    int** ppNumber = &pNumber; // Double pointer: Store address of pointer 
    int*** pppNumber = &ppNumber;

    // Variable - mahesh
    // Home address - Single pointer 
    // Sushil knows where mahesh stays - double pointer 

    printf("\n value of number %d", number);
    printf("\n address of number %p", &number);
    printf("\n value of pNumber %p", pNumber);
    printf("\n value of ppNumber %p", ppNumber);
    printf("\n value of pppNumber %p", pppNumber);

    printf("\n value of number before change %d", number);
    doubleTheValue(number);
    printf("\n value of number after change %d", number);

    printf("\n value of number before change %d", number);
    doubleTheValueWorks(&number);
    printf("\n value of number after change %d", number);

}

// Pointers can be incremented and decremented 
void DemoPointersInArray()
{
    int numbers[] = {1,2,3};
    int *pNumbers = &numbers;

    printf("\n Value of %p ", numbers);
    printf("\n Value of %p ", &numbers);
    printf("\n Value of %p ", pNumbers);

    printf("\n Value of %d ", *pNumbers);
    pNumbers++; // When you do ++ for a pointer, it goes to the next address.

    printf("\n Value of %d ", *pNumbers);
}

void DemoDoublePointer(int** ppReference, int* pNumber)
{
    *ppReference = pNumber;
}

void InvokeDemoDoublePointer()
{
    int maheshAge = 40;
    int sushilAge = 41;

    int* pFounderAge = &maheshAge;

    printf("\n Before Mahesh age = %d, Sushil age = %d ", maheshAge, sushilAge);
    printf("\n Before founder age = %d ", *pFounderAge);
    DemoDoublePointer(&pFounderAge, &sushilAge);
    printf("\n After Mahesh age = %d, Sushil age = %d ", maheshAge, sushilAge);
    printf("\n After founder age = %d ", *pFounderAge);
}


int main()
{
    //SinglePointerDemo();
    //swapValuesDemo();
    // DemoPointersInArray();
    // InvokeDemoDoublePointer();

    int count = 0;
    printf("\n Before value of count = %d ", count);
    printf("\n Enter the value for count \n");
    scanf("%d", &count);
    printf("\n After value of count = %d ", count);

}

