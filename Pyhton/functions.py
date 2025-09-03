
# def name_of_the_function(function arguments) -> return type
sum1=10

def getSum(numbers) -> int:
    sum1=1
    print(sum1)
    sum = 0
    for number in numbers:
        sum = sum + number 
    
    return sum

def search(numbers, key) -> bool:
    isFound = False

    for number in numbers:
        if (number == key):
            isFound = True
    
    return isFound

if __name__ == "__main__":
    numbers = [1,5,10,15]

    print(sum1)

    sum = getSum(numbers)
    print("Sum of the numbers ", sum)
    print(sum1)

    if (search(numbers, 10)):
        print("Key is found")
    else:
        print("Key is not found")