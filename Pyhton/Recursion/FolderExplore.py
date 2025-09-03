import os

def explore_directories(root_directory):
    try:
        # List all the entries in the directory
        entries = os.listdir(root_directory)
        for entry in entries:
            path = os.path.join(root_directory, entry)
            if os.path.isdir(path):
                print(path)
                # Recursively explore the sub-directory
                explore_directories(path)
    except PermissionError:
        # Handle the case where the program doesn't have permission to access a directory
        print(f"Permission denied: {root_directory}")
    except FileNotFoundError:
        # Handle the case where a directory was not found
        print(f"Directory not found: {root_directory}")

# Example usage
root_directory = "C://RecurssionDemo"  # Replace with the root directory path you want to explore
explore_directories(root_directory)
