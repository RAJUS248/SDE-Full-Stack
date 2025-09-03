import csv
import argparse

def calculate_min_platforms_needed(csv_file_path):
    # Lists to store arrival and departure times
    arrival_times = []
    departure_times = []

    # Read the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert arrival and departure times from string to integer
            arrival_time = int(row['Arrival'])
            departure_time = int(row['Departure'])
            arrival_times.append(arrival_time)
            departure_times.append(departure_time)

    # Sort arrival and departure times
    arrival_times.sort()
    departure_times.sort()

    # Initialize counters for platforms and the maximum number needed
    current_platforms_needed = 0
    max_platforms_needed = 0
    arrival_index = 0
    departure_index = 0
    total_buses = len(arrival_times)

    # Iterate through arrival and departure times to determine platform needs
    while arrival_index < total_buses and departure_index < total_buses:
        # If the next event is an arrival, increment the platform count
        if arrival_times[arrival_index] < departure_times[departure_index]:
            current_platforms_needed += 1
            arrival_index += 1
            # Update the maximum number of platforms needed
            max_platforms_needed = max(max_platforms_needed, current_platforms_needed)
        else:
            # If the next event is a departure, decrement the platform count
            current_platforms_needed -= 1
            departure_index += 1

    return max_platforms_needed

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Calculate the minimum number of platforms needed at a bus station.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file with bus arrival and departure times.')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function and print the result
    platforms_needed = calculate_min_platforms_needed(args.csv_file)
    print(f"Minimum number of platforms needed: {platforms_needed}")

if __name__ == '__main__':
    main()
