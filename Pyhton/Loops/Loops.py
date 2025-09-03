def search(find_name: str, names: list) -> bool:
    isFound = False

    for name in names:
        if (name == find_name):
            isFound = True
            break
    
    return isFound

def getNamesWithPrefix(prefix: str, names: list) -> bool:
    results = []

    for name in names:
        if not name.startswith(prefix):            
            continue

        results.append(name)
    return result

def getStatus(attempt: int)-> bool:
    if (attempt == 5):
        return True
    else:
        return False


def retryNeverGiveUp(data: str):
    status = False
    count = 0

    while True:
        # try to send the data and check status
        count += 1
        if (getStatus(count)):
            break
           
        



def retrySend(data: str, maxRetryCount: int):

    count = 0
    while count < maxRetryCount:
        # try to send the data         
        print(count)
        count+=1

def printMultiplicationTable(maxTable: int):
    for number in range (1, maxTable):
        for multiplyWith in range (1,11):
            print(f" {number} x {multiplyWith} = {number*multiplyWith}")
        print("-------")


printMultiplicationTable(3)

# range (start, max/min, step)
for number in range(1,6,1): # forwad gear 
    print(number * "*")

print("--------")

for number in range(5,0, -1): # reverse gear 
    print(number * "*")


for number in range(5):
    print(number * "*")

print("--------")

for number in range(0,5):
    print(number * "*")

print("--------")

for number in range(0,5,1):
    print(number * "*")


retryNeverGiveUp("data")

retrySend("data", 3)

names =  ["mahesh", "amit", "krishna", "santosh", "mahesh", "sangeeta"]

namesWithPrefix = getNamesWithPrefix("sa", names)
print(namesWithPrefix)


result = search("santosh", names)
print(f"Is Santosh present in the list  {result}")

count = 0
for name in names:
    if name == "mahesh":
        count+=1
    
    print(name)



print(f"Count of mahesh in the list {count}")



print("Printing names by using index value")
for index in range(6):
    print(names[index])


