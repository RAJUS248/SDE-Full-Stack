# Print the multiplication table from 2 to 10

# Loop through numbers 2 to 10
for i in range(2, 11):
    print(f"Multiplication table for {i}:")
    # Loop through numbers 1 to 10 to multiply with 'i'
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
        
    
