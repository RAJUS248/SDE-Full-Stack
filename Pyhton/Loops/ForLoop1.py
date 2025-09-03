
numbers = [ 2, 3, 5, 6]

for number in numbers:
    print(number)
    if (number == 3):
        print("3 is found so breaking!!")
        break
else:
    print("3 is not found")

squares = [number ** 2 for number in range(6)]
print(squares)

students = ['mahesh', 'sangeeta', 'amit', 'sushil']

for student in students:
    if (student == 'mahesh'):
        continue
    
    print(student)



for number in range(5):
    if number == 2:
        continue
    print(number)


for number in range(10):
    if number == 5:
        print("Breaking loop at 5")
        break

    print(number)


students = ['mahesh', 'sangeeta', 'amit', 'sushil']

for student in students:
    print(student)
    

values = range(10)

# for(int index; index < 10; index++)

for item in range(10):
    print(item)

for item in range(0,10,1):
    print(item)
    

for item in range(1,10,2):
    print(item)

# for (int index=10, index > 1; index--)
for item in range(10,1,-1):
    print(item)