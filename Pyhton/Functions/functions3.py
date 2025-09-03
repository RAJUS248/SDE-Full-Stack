
# Function definition
def nanuFirst() -> None:
    print("Nanu first function")
    nanuSecondFunction()
    

def nanuSecondFunction() -> None:
    print("Nanu second function")
    nanuFirst()

# Function invocation / calling
nanuFirst()


