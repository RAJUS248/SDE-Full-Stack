from datetime import datetime

def find_day_of_week(date_str):
    """
    Find the day of the week for a given date.

    :param date_str: Date in 'YYYY-MM-DD' format.
    :return: Day of the week.
    """
    # Convert date_str to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Get the day of the week
    day_of_week = date.strftime('%A')
    
    return day_of_week

def main():
    # Read the date from user input
    date_str = input("Enter a date (YYYY-MM-DD): ")
    
    try:
        # Find the day of the week
        day = find_day_of_week(date_str)
        print(f"The day of the week for {date_str} is {day}.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")

if __name__ == '__main__':
    main()
