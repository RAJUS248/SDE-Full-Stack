

def return_student_marks(name):
    # dummy code or logic 
    return 90,99,100,75


student_marks = return_student_marks("mahesh")
print(student_marks)

#student = ("Mahesh Arali", "SDE full stack", "20 years industry exp", 42)

student = "Mahesh Arali", "SDE full stack", "20 years industry exp", 42  # packing



print(student)

print(student[0])
print(student[1])
print(student[2])
print(student[3])

college = "algorithms365", student

print(college)

tuple_single_data = "algorithms" ,

student1 = "Mahesh Arali", "SDE full stack", "20 years industry exp"

name, course, experience = student1  # un-packing

print(name)
print(course)
print(experience)

# student.count()  it takes 1 argument 
# student.index("mahesh")

colleges = "SVIT", "REC" , "PES", "RV", "SVIT", "KLE", "SVIT"

count = colleges.count("SVIT")
print(f"Number of students from SVIT =  {count}")