
student_list_empty = {}

# Syntax  variable_name_dictionary[ key ] = value
student_list_empty[1] = "Ramesh"

students_list = {'123' : "Mahesh", '124' : "Sanat" , '125': "Mahat"}

print(student_list_empty)
print(students_list)

name = students_list.get('124')
print(f" name of the student {name}")

student_name1 = students_list.pop("123")
print(student_name1)

print(students_list.keys())

print(students_list.values())

students_list.clear()

print(students_list)


student_directory = {
    101: {"name": "Alice", "branch": "Computer Science"},
    102: {"name": "Bob", "branch": "Electronics"},
    103: {"name": "Charlie", "branch": "Mechanical"}
}

student_1 = student_directory[101]
print(student_1)

student_1["name"] = "Mahesh"

print(student_1)