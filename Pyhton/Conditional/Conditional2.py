
# Definition
def getClassForPercentage(percentage: float) -> str:
    if (percentage >= 75):
        return "Distinction"
    elif (percentage >= 60):
        return "First class"
    elif (percentage >= 50):
        return "Second class"
    elif (percentage >= 35):
        return "Third class"
    else:
        return "Failed"

student1_percentage = 30
result = getClassForPercentage(student1_percentage)
print(result)