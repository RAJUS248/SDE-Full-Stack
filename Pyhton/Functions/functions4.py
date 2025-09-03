def print_student_details(name: str, age: int, cgpa: float) -> int:
    print("Student details ")
    print("name ", name)
    print("age ", age)
    print("CGPA ", cgpa) 
    return age   
    

def print_student_details_simple(name, age, cgpa):
    print("Student details ")
    print("name ", name)
    print("age ", age)
    print("CGPA ", cgpa)
    return age, name   

def printa(n,a,c):
    print(n)
    print(a)
    print(c)
    

student_age = print_student_details("Mahesh", 40, 8.9)
print("Student age returned is = ", student_age)

student_age_2, student_name = print_student_details_simple("Ramesh", 50, 9.1)
print("Student age returned is = ", student_age_2)
print("Student name returned is = ", student_name)

