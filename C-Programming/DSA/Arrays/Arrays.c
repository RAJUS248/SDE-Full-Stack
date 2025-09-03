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

void demonstate_1D_arrays()
{
    // Collection of homogenious items or variables 

    // Declaration of the array and also initialization
    // Hardcoding / hardcode
    int numbers[5] = {1,2,3,4,5, 6, 7, 8};
    char name[4] = "alg" ;
    float prices[3] = {1.1, 1.2, 1.3};

    
    numbers[0] = 100;
    printf("\n %d", numbers[0]);
    printf("\n %d", numbers[1]);
    printf("\n %d", numbers[2]);
    printf("\n %d", numbers[3]);
    printf("\n %d", numbers[4]);
    printf("\n %d", numbers[5]);
    printf("\n %d", numbers[6]);
    


    name[0] = 'A';
    printf("\n %c", name[0]);
    printf("\n %c", name[1]);
    printf("\n %c", name[2]);
    printf("\n %c", name[3]);
    printf("\n %c", name[4]);


    prices[0] = 0.1;
    printf("\n %f", prices[0]);
    printf("\n %f", prices[1]);
    printf("\n %f", prices[2]);
    printf("\n %f", prices[3]);
    printf("\n %f", prices[4]);

    printf("\n generating index values");

    for (int index=0; index < 5 ; index++)
    {
        printf("\n Index value is = %d", index);
        printf("\n Element at index is = %d", numbers[index]);
    }

    for (int index=0; index < 5 ; index++)
    {
       numbers[index] = numbers[index] + 100;
        printf("\n Element at index is = %d", numbers[index]);
    }


    for (int index=4; index >= 0 ; index--)
    {
        printf("\n Element at index is = %d", numbers[index]);
    }
    
}

void demonstate_2D_arrays()
{
    int numbers[3][3] = {
        {11,12,13},
        {21,22,23},
        {31,32,33}
    };

    // This is for generating rows from 0 to 2
    for (int row=0; row<3; row++) 
    {
        printf("\n");

        // For generating column values from 0 to 2
        for (int column=0; column<3; column++)
        {
            printf(" %d%d ", row, column);
            numbers[row][column] = numbers[row][column] + 100;
        }
    }

     // This is for generating rows from 0 to 2
    for (int row=0; row<3; row++) 
    {
        printf("\n");

        // For generating column values from 0 to 2
        for (int column=0; column<3; column++)
        {
            printf(" %d", numbers[row][column]);
        }
    }

}

void IncrementOperations()
{
    int num = 10 ;
    ++num;
    ++num;
   // printf("\n Prefix %d", ++num);
  //  printf("\n Postfix %d", num++);
  //  printf("\n CurrentValue %d", num);

    for (int index=0; ++index < 5; )
    {
        printf("\n Index -> %d ", index);
    }

}

void fibonacciSeriesSequential(int max)
{

}

void fibonacciSeries(int follow, int lead, int count)
{
    if (count == 0) // Condition to stop the loop
        return;

    int sum = follow + lead;
    follow = lead;
    lead = sum;
    count--;

    printf("\n  Before %d", lead);
    demoRecursion(follow, lead, count);
    printf("\n  After %d", lead);
}

int main() {
    int count = 5;
    printf("\n  0");
    printf("\n  1");
    fibonacciSeries(0,1, count-2);
    return 0;
}

