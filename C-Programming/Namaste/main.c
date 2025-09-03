#include <stdio.h>
#include <stdlib.h>

int getHihgestElementFromArray(int numbers[]);
int fun(int a[]);

int fun(int a[])
{
    int s = sizeof(a)/sizeof(a[0]);
    int m=0;
    for(int i=0;i<s;i)
        if (a[i]>m) m=a[i];        
    return m;
}

int getSum(int number1, int number2);

int getSum(int number1, int number2)
{
    int sum = number1 + number2;
    return sum;
}

int getHihgestElementFromArray(int numbers[])
{
    int size = sizeof(numbers) / sizeof(numbers[0]) ;

    if (numbers == NULL)
        return INT_MIN;

    if (size == 0)
        return INT_MIN;

    int max = numbers[0];
    for (int i=1; i<size; i++)
    {
        if (numbers[i] > max)
        {
            max = numbers[i];
        }
    }

    return max;
}

void printInputArguments(int argc, char *argv)
{
    int count = printf("Namaskara\n");

   printf("Value of count %d", count);

     printf("Number of arguments: %d\n", argc);
    
    for (int i = 0; i < argc; i++) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }
}

int main(int argc, char *argv[])
{
   //printInputArguments(argc, argv);

    int numbers[] = {5, 10,34, 99, 345, 999};

   // int size = sizeof(numbers) / sizeof(numbers[0]) ;
  //  int highest = getMax(numbers, size);

    int highest = getHihgestElementFromArray(numbers);
    printf("Highest value in the array is %d", highest);

    return 0;
}
