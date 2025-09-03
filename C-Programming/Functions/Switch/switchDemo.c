#include <stdio.h>

const char* get_Month_Str(int month) {
    switch(month) {
        case 1:
            return "January";
        case 2:
            return "Feb";
        case 3:
            return "Mar";
        case 4:
            return "April";
        case 5:
            return "May";
        case 6:
            return "June";
        case 7:
            return "July";
        case 8:
            return "Aug";
        case 9:
            return "Sept";
        case 10:
            return "Oct";
        case 11:
            return "Nov";
        case 12:
            return "Dec";
        default:
            return "Invalid month";
    }
}

int main() {
    printf("%s\n", get_Month_Str(-1)); // Output: Invalid month
    printf("%s\n", get_Month_Str(1));  // Output: January
    printf("%s\n", get_Month_Str(5));  // Output: May
}
