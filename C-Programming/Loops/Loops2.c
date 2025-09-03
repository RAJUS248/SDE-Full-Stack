#include <stdio.h>

int main()
{
    int count = 0;

    while(count <= 10)
    {
        count = count+1;

         if (count == 5)
            continue;
        
        printf("\n%d", count);
    }

   /* do 
    {
        printf("\n%d", count);
        count = count -1;
    } while(count >= 0);
    */
}