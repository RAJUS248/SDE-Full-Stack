from datetime import datetime

def calculate_days_since_birth(date_of_birth_str):
    """
    Calculate the number of days since the given date of birth up to the current date and time.

    :param date_of_birth_str: Date of birth in 'YYYY-MM-DD' format.
    :return: Number of days since birth.
    """
    # Convert date_of_birth_str to a datetime object
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')
    
    # Get the current date and time
    current_date = datetime.now()
    
    # Calculate the difference in days
    delta = current_date - date_of_birth
    days_since_birth = delta.days
    
    return days_since_birth

def main():
    # Read the date of birth from user input
    date_of_birth_str = input("Enter your date of birth (YYYY-MM-DD): ")
    
    try:
        # Calculate days since birth
        days = calculate_days_since_birth(date_of_birth_str)
        print(f"Number of days since birth: {days}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")

if __name__ == '__main__':
    main()
