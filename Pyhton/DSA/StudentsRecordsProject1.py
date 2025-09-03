students_db = []

def add():
    id = int(input("Enter the id: "))
    name = input("enter the name: ")

    student_record = (id, name)
    students_db.append(student_record)

def print_all():
    for student_record in students_db:
        print(student_record)


if __name__ == "__main__":
    add()
    add()
    add()

    print_all()

