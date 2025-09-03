

#include <string>  // Required for using std::string

class Student {
private:
    std::string name;
    int age;
    float grade;

public:
    // Constructor
    Student(std::string studentName, int studentAge, float studentGrade);

    // Methods
    void displayInfo();
    bool isPassed();
};
