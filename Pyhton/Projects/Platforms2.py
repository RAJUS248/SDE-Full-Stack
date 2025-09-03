import random
from datetime import datetime, timedelta

def time_to_minutes(time_str):
    """Convert time in 'HHMM' format to minutes since midnight."""
    hours = int(time_str[:2])
    minutes = int(time_str[2:])
    return hours * 60 + minutes

def minutes_to_time(minutes):
    """Convert minutes since midnight to 'HHMM' format."""
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02d}{minutes:02d}"

def generate_schedule(num_buses, start_time_str, end_time_str):
    """Generate a schedule for buses given the number of buses and time constraints."""
    # Convert input times to minutes
    start_time_minutes = time_to_minutes(start_time_str)
    end_time_minutes = time_to_minutes(end_time_str)

    # Define minimum and maximum stay times in minutes
    min_stay = 10
    max_stay = 30

    # Initialize variables for scheduling
    schedule = []
    current_time = start_time_minutes

    for bus_id in range(1, num_buses + 1):
        # Ensure buses do not arrive after the end time
        if current_time + min_stay > end_time_minutes:
            print(f"Unable to schedule bus {bus_id} due to time constraints.")
            break

        # Schedule arrival and departure times
        arrival_time_minutes = current_time
        stay_duration = random.randint(min_stay, max_stay)
        departure_time_minutes = arrival_time_minutes + stay_duration

        # Ensure departure is before end time
        if departure_time_minutes > end_time_minutes:
            departure_time_minutes = end_time_minutes

        # Format times for output
        arrival_time_str = minutes_to_time(arrival_time_minutes)
        departure_time_str = minutes_to_time(departure_time_minutes)

        # Add to schedule
        schedule.append((bus_id, arrival_time_str, departure_time_str))

        # Update current time for next bus arrival
        current_time = departure_time_minutes

    return schedule

def print_schedule(schedule):
    """Print the bus schedule."""
    print("BusID  Arrival  Departure")
    for bus_id, arrival, departure in schedule:
        print(f"{bus_id:4d}  {arrival}     {departure}")

def main():
    # Read user input
    num_buses = int(input("Enter the number of buses: "))
    start_time_str = input("Enter the start time (HHMM): ")
    end_time_str = input("Enter the end time (HHMM): ")

    # Validate input
    try:
        datetime.strptime(start_time_str, "%H%M")
        datetime.strptime(end_time_str, "%H%M")
    except ValueError:
        print("Invalid time format. Please use HHMM format.")
        return

    if not (0 <= num_buses <= 50):
        print("Number of buses should be between 1 and 50.")
        return

    # Generate and print schedule
    schedule = generate_schedule(num_buses, start_time_str, end_time_str)
    print_schedule(schedule)

if __name__ == '__main__':
    main()
