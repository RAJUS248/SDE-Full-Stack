#include<stdio.h>

// Function declarations
char* getSchoolName(int schoolId);
int getTotalStudentsCount(int schoolId);
void getTotalBoysAndGirls(int schoolId,
                          int* boysCount,
                          int* girlsCount);

char* getTopperInMaths(int schoolId, int grade);

char* getTopperInForSubject(int schoolId,
                             int grade,
                             char subject[]);


int main()
{
   int schoolId = 1;
   int grade = 5;
   printf(getSchoolName(schoolId));

   printf("\n ----- \n ");
   printf(" Total students %d", getTotalStudentsCount(schoolId));
   printf("\n ----- \n ");
   printf("Topper for grade %d is %s ", grade, getTopperInMaths(schoolId, grade));

   return 0;
}

char* getSchoolName(int schoolId)
{
    // Implementation goes here
    static char schoolName[] = "Navodaya School";
    return schoolName;
}
int getTotalStudentsCount(int schoolId)
{
    // Dummy code
    int totalCount = 100;
    return totalCount;
}
void getTotalBoysAndGirls(int schoolId,
                          int *boysCount,
                          int *girlsCount)
                          {
                              *boysCount = 100;
                              *girlsCount = 100;
                          }

char* getTopperInMaths(int schoolId, int grade)
{
    static char topperName[] = "Bharat";
    return topperName;
}

char* getTopperInForSubject(
        int schoolId,
        int grade,
        char subject[])
        {
            static char topperName[] = "Bharat";
            return topperName;
        }




