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

/* Dynamic memory allocation*/

#include<stdio.h>
#include<windows.h>

int data = 5; 

void dma_demo()
{
    int number = 5; // Static memory allocation  
    int numbersStatic[3]; // Static memory allocation

    int* dynamicArray;

   // dynamicArray = (int*) malloc(sizeof(int)*3); // Dynamic memory allocation
    dynamicArray = (int*) calloc (sizeof(int), 3); // Dynamic memory allocation

    // DMA - head segment , it will be there till freed. 

    if (dynamicArray != NULL)
    {
        dynamicArray[0] = 1;
        dynamicArray[1] = 2;
        dynamicArray[2] = 3;

    }

    free(dynamicArray);
    // Now dynamicArray is dangling pointer 
    dynamicArray[0] = 10;

    // Best practice, after freeing the memory set pointer to NULL
    dynamicArray = NULL;
    dynamicArray[0] = 10;
}

void demoMemoryLeak()
{
    int count = 1;

    while(count<10000)
    {
        char* pString = (char*) malloc (10 * 1024);

        Sleep(100);
        if (pString != NULL)
        {
            printf("\n Memory allocated count=%d", count);
        }
        else
        {
            printf("\n Failed to allocate memory");
        }

       // free(pString);  you have to uncomment this and run to see that memory leak is stopped
        count++;
    }

}

int main()
{
    demoMemoryLeak();
}