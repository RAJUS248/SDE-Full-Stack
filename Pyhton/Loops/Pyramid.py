
def print_pyramid(height: int):
    countOfStars = 1
    for spaces in range (height, 0, -1):
        levelSpaces =  spaces * " " 
        levelStars = countOfStars * "*"
        print(levelSpaces + levelStars)
        countOfStars+=2

def print_inverted_pyramid(height: int):
    countOfStars = height * 2 - 1

    for currentLevel in range (0, height+1, 1):
        levelSpaces =  currentLevel * " " 
        levelStars = countOfStars * "*"
        print(levelSpaces + levelStars)
        countOfStars-=2

print_pyramid(5)
print(" ")
print(" ")
print_inverted_pyramid(5)
        
