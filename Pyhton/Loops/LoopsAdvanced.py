def print_stars(maxCount):
    star_string = ""
    for count in range(maxCount):
        star_string = star_string + "*"

    print(star_string)

def print_stars_v2(maxCount):
    print(maxCount * "*")


def print_star_grid(gridSize):
    for count in range(gridSize):
        print(gridSize * "*")


def print_star_grid_concat(grindSize):    
    for rows in range(grindSize):
        printMsg = []
        
        for noOfStars in range(grindSize):
            printMsg.append("*")
        
        print("".join(printMsg))

def print_star_list(numbers):
    for number in numbers:
        print(number * "*")


def print_star_grid_skip_even(gridSize):    
    for rows in range(gridSize):
        printMsg = []
        
        for noOfStars in range(gridSize):
            printMsg.append("*")
        
        print("".join(printMsg))


def print_star_grid_borders_only(gridSize):    
    for row in range(1, gridSize+1, 1):
        printMsg = []
        
        for column in range(1, gridSize+1, 1):
            isStar = column == 1 or column == gridSize or row == 1 or row == gridSize
            printMsg.append( "*" if isStar else " ")
            #printMsg.append(str(row) + "," + str(column) + " ")
        
        print("".join(printMsg))

def print_star_pyramid(height):
    noOfStars = 1
    for level in range (1, height+1, 1):
        noOfSpaces = height - level
        print(noOfSpaces * " "  + noOfStars * "*") 
        noOfStars = noOfStars + 2


def print_inverted_star_pyramid(height):
    for level in range(1, height+1, 1):
        noOfSpaces = level - 1
        noOfStars = ( height - level ) * 2 + 1
        print(noOfSpaces * " " + noOfStars * "*")


print_inverted_star_pyramid(15)
print_star_pyramid(15)
#print_star_grid_borders_only(5)
#print_stars(1000)
#print_stars_v2(1000)
#print_star_grid(5)
#numbers = [2,3,4,3,2,10,11,12,10,12]

#numbers = [1,2,3,3,4,5,6,7]
#print_star_list(numbers)
 
#print_star_grid_concat(5)