#include <stdio.h>
#include <stdbool.h>

int main() {
    int number = 5;
    char* result;
    
    result = (number >= 0) ? "Greater than or equal to zero" :  "Less than zero" ;

    printf("%s", result);

}