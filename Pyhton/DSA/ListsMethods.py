"""
* -----------------------------------------------------------------------------
* 
* Copyright <2024> <algorithms365>
* 
* Professional Coding Skills Workshops
* 
* Licensed under the MIT License:
*  
* https://opensource.org/licenses/MIT
* 
* For more information about algorithms365:
* Visit Our Skills Website: https://skills.algorithms365.com/
* Our Company Website: https://algorithms365.com/
*
* For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
* Instagram: https://www.instagram.com/algorithms365/
* YouTube: https://www.youtube.com/@algorithms365
* Facebook: https://www.facebook.com/algorithms365 
* Twitter(X): https://x.com/algorithms365
* LinkedIn: https://www.linkedin.com/company/algorithms365-technologies-llp/
* 
* Join Our Communities:
* WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
* Telegram: https://t.me/+hyVHXek9WM0zNWQ1
* 
* -----------------------------------------------------------------------------
"""

numbers = [1,4,9]

numbers.append(5)
numbers.append(11)
numbers.append(6)

print(numbers)

numbers.sort()

print(numbers)

numbers.insert(2,100)

print(numbers)

numbers.remove(11)

print(numbers)

numbers.reverse()

print(numbers)

value = numbers.pop()

print(value)

print(numbers)

for number in numbers:
    print(number)

print(numbers[3])
print(numbers[2])

matrix = [
    [1,2,3],
    [4,5,6]
]

print(matrix)

matrix[0][0] = 100
matrix[0][1] = 200

print(matrix)
