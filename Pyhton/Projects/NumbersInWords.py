def number_to_words(number):
    """Convert a number into words."""
    if number == 0:
        return "zero"

    # Define word representations for numbers
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    def get_words(n):
        """Helper function to convert a number less than 1000 to words."""
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else "-" + units[n % 10])
        else:
            return units[n // 100] + " hundred" + ("" if n % 100 == 0 else " and " + get_words(n % 100))

    # Process the number in chunks of 1000
    if number < 1000:
        return get_words(number)
    
    result = ""
    if number >= 1000:
        result = get_words(number // 1000) + " thousand"
        remainder = number % 1000
        if remainder:
            result += " " + get_words(remainder)
    
    return result.strip()

def main():
    # Read number from user input
    number_str = input("Enter a number: ")
    
    try:
        # Convert the input to an integer
        number = int(number_str)
        
        # Ensure the number is within a reasonable range (0-9999)
        if 0 <= number <= 9999:
            words = number_to_words(number)
            print(f"The number {number} in words is: {words}.")
        else:
            print("Please enter a number between 0 and 9999.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
