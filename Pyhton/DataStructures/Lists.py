
# List (array list)

students = ["mahesh", "sangeeta", "amit", "santosh"]
employee = [] # empty list 

students.append("ram")
count = students.count("mahesh")
print(f"Number of mahesh's in the class {count}")

students.remove("mahesh")
print(students)

students.sort()
print(students)

students.sort(reverse=True)
print(students)