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
/* Learning struct */
#include<stdio.h>
#include<string.h>
#include<malloc.h>

struct Student {
    int Id;
    char Name[50];
    int Age;
};

typedef struct employee {
    int Id;
    char Name[50];
    int Age;
} Employee;

typedef int Age;

void DemoStructStudent()
{
     int number = 5;

    struct Student student1;
    student1.Id = 1;
    strcpy(student1.Name, "Mahesh");
    student1.Age = 40;

    printf("\n Student Id :%d", student1.Id);
    printf("\n Student Name :%s", student1.Name);
    printf("\n Student Age :%d", student1.Age);

    struct Student students[10];

    students[0].Id = 2;
    students[0].Age = 40;
    strcpy(students[0].Name, "Sushil");

    
    printf("\n From Array: Student Id :%d", students[0].Id );    
    printf("\n From Array: Student Age :%d", students[0].Age);
    printf("\n From Array: Student Name :%s", students[0].Name);

}

void DemoEmployee()
{
    Employee emp1;
    emp1.Age = 30;
    emp1.Id = 1;
    strcpy(emp1.Name, "Mahesh");
    printf("\n Employee Name :%s", emp1.Name);
}

void DynamicMemoryAllocationStruct()
{
    struct Student* pStudent1 = (struct Student*) malloc(sizeof(struct Student));
    pStudent1->Id = 1;
    strcpy(pStudent1->Name, "Sangeeta");
    pStudent1->Age = 30;
    printf("\n Student Name :%s", pStudent1->Name);
    

    Employee* pEmployee = (Employee*) malloc(sizeof(Employee));
    struct employee* pemp1 = (struct employee*) malloc(sizeof(struct employee));

    pEmployee->Id = 1;
    strcpy(pEmployee->Name, "Santosh");
    pEmployee->Age = 30;

    printf("\n Employee Name :%s", pEmployee->Name);

}


int main()
{
    //DemoStructStudent();
    // DemoEmployee();
    DynamicMemoryAllocationStruct();
}