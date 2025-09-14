
def printNumber(number):

    if (number == 0):
        return
    
    number = number - 1
    print(f"Before reursive call {number}")

    printNumber(number)

    print(f"After reursive call {number}")


printNumber(5)