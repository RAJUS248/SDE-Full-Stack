 # who is the topper 
#  maths
# which grade ?
# 5th grade
# which school 
# Jnv
# name of the student 
#input grade, school, subject 
# output name of the student 

from typing import Tuple


def get_topper_name(schoolName: str, grade: int, subject: str) -> str:
    # Dummy implmentation 
    return "Ram"

def get_school_name(schoolId: int) -> str:
    return "navodaya"

def get_boys_girls_count_for_grade_in_school(schoolId: int, grade: int) -> Tuple[int, int]:
    # Actual code to connect to DB or file or API goes here
    return 100,100

def get_boys_girls_count_for_grade_in_school_raw(schoolId, grade):
    # Actual code to connect to DB or file or API goes here
    return 100,100

def get_count_of_total_students(schoolId: int, totalStudents: int) -> None:
    totalStudents = 1000

student_name = get_topper_name("Navodaya", 5, "Maths")
print("Topper student name ", student_name)

boyscount, girls_count = get_boys_girls_count_for_grade_in_school(5, 10)
print("Count of boys and girls ", girls_count, boyscount)

totalStudents = 0
get_count_of_total_students(1, totalStudents)
print("Total students ", totalStudents)