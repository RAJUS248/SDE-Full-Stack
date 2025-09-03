#include "Student.h"
#include <iostream>


using namespace std;

int main()
{
    // Create a student object
    Student student1("John Doe", 20, 85.5);

    // Display student info
    student1.displayInfo();

    // Check if the student passed
    if (student1.isPassed()) {
        std::cout << "The student has passed." << std::endl;
    } else {
        std::cout << "The student has not passed." << std::endl;
    }

    return 0;
}
