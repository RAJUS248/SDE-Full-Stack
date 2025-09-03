
# Syntax 

# def name_of_the_function (parameters) -> returntype:
#print("Hello World")


# Defined the functions
def print_my_messages(message): 
    print(message)

# def name_of_the_function (parameters) -> returntype:
def get_my_message(message) -> str:
    new_string = message + " How are you?"
    return new_string

def append_messages(message1: str, message2: str, message3: str) -> str:
    final_message = message1 + message2 + message3
    return final_message


def swap_two_numbers(value1: int, value2: int):
    #temp = number1
    #number1 = number2
    #number1 = temp
    return value2, value1

def explode(count: int):
    print(f"{count}: Stack level deep")
    explode(count+1)

#def greet_guest(name: str) -> None: This would have problem 

def greet_guest(name: str = "guest") -> None:
    print("Hello " + name)

# Function invocation / call the function 
#print_my_messages("My message - hello")

def get_sum(*numbers: int) ->int:
    sum_of_all_numbers = sum(numbers)
    return sum_of_all_numbers


def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b

if __name__ == "__main__":
    print("I am in main block now!")

    print_my_messages("Hello World!")

    new_message = get_my_message("Mahesh ")
    print(new_message)

    message1 = "India "
    message2 = "is "
    message3 = "great! "
    combined_msg = append_messages(message1, message2, message3)
    print(combined_msg)

    

    number1 = 10
    number2 = 20
    number1, number2 = swap_two_numbers(number1, number2)
    print(f"number1 {number2} number2 {number2}")

    # explode(1)


    greet_guest("Sangeeta")
    greet_guest("")

    ans1 = get_sum(1,2,3)
    print(f"ans1 = {ans1}")

    ans2 = get_sum(1,2,3,4,5)
    print(f"ans2 = {ans2}")

    sum_of_two_numbers = add()