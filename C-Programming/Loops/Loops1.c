#include <stdio.h>

int main()
{
    //for (start ; stop; change)
    for (int number=1; number <= 10 ; number++)
    {
        // outer loop 
        printf("hello");
        for(int value=1; value <= 10; value++)
            {
                int answer = number * value;
                printf(" %d", answer);      
            }
    }
}