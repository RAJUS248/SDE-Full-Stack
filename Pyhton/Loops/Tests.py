user_scores = {"Alice": 90, "Bob": 85}
for name, score in user_scores.items():
    print(f"{name} scored {score}")

# print only mahesh details
student_scores = {"mahesh": 1, "amit": 2, "sushil": 3, "mahesh": 4}
for name, score in student_scores.items():
    if name is not "mahesh":
        continue

    print(f"{name} scored {score}")


MAX_NUMBER = 10
for number in range(MAX_NUMBER+1):
    print(number)

for number in range(1, MAX_NUMBER+1):
    print(number)

for number in range(2, MAX_NUMBER+1, 2):
    print(number)

for number1 in range (1, 10000):
    for number2 in range (1, 10):
        #print(f"{number1} X {number2} = {number1*number2}")
        ans = number1 * number2


attempts = 0
MAX_ATTEMPTS = 3

while (attempts < MAX_ATTEMPTS):
    print(f"Trying to connect attempt num = {attempts}")
    attempts = attempts + 1

attempts = 0

while True:
    print(f"Trying to connect attempt num = {attempts}")
    attempts+=1
    if (attempts == 3):
        break


skills = ["coding", "problem solving", "CS fundamentals"]

for skill in skills:
    print(skill)

colors = {"red", "green", "blue"}
for color in colors:
    print(color)