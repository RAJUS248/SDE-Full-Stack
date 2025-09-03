def increment_and_print(counter: int):
    if (counter >= 2):
        return    
    
    counter = counter + 1
    
    print(f"{counter}")
    increment_and_print(counter)
    print(f"{counter}")
    

increment_and_print(0)
