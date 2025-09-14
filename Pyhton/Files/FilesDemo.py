import os

# Creates the file
def create_file(file_name):
    with open(file_name, "w") as file_Handle:
        file_Handle.close()

def append_contents(file_name, content):
    with open(file_name, "a") as file_Handle:
        file_Handle.write(content)
        file_Handle.write(content)
        file_Handle.write(content)
        file_Handle.close()

def read_print_content(file_name):
    with open(file_name, "r") as file_handle:
        content = file_handle.read()
        print(content)
        file_handle.close()


def delete_file(file_name):

    if os.path.exists(file_name):
        os.remove(file_name)
        print("file got deleted")
    else:
        print("file doesn't exist")




file_name = 'mynotes.txt'
content = "Namaskara Karnatka! \n"

create_file(file_name)
append_contents(file_name, content)
read_print_content(file_name)
delete_file(file_name)