
def check_age(age):
    if (age < 18):
        raise ValueError("Age is less than the allowed limit")
    
    # happy path code 
    # more line of code 
    print("Eligible for the voting")


def check_englibility_for_voting():
    try:
        check_age(16)
        #check_duplicate(voterepic)
        #check_address(address)
        #check_citizenship(document)
        #check_birthcertificate(document)
        # happy path code here 
        # business logic 
        print("person is eligible for voting")

    except ValueError as e:
        print(e)

def read_and_print_file(file_path):
    file_handle = None
    try:
        file_handle = open(file_path)
        content = file_handle.read()

    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    except PermissionError:
        print("Error: You do not have permission to access this file.")

    finally:
        print("Clean-up in progress")
        try:
            if file_handle is not None:
                file_handle.close()
        except Exception:
            # swallow the exception
            pass

#read_and_print_file("file-ella.txt")
check_voting()
