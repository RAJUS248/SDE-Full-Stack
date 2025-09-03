import os

def explore_directories(root_directory):
    # Use a stack to store directories to be explored
    stack = [root_directory]

    while stack:
        current_directory = stack.pop()
        try:
            entries = os.listdir(current_directory)
            for entry in entries:
                path = os.path.join(current_directory, entry)
                if os.path.isdir(path):
                    print(path)
                    stack.append(path)
        except PermissionError:
            # Handle the case where the program doesn't have permission to access a directory
            print(f"Permission denied: {current_directory}")
        except FileNotFoundError:
            # Handle the case where a directory was not found
            print(f"Directory not found: {current_directory}")

# Example usage
root_directory = "C:\\RecurssionDemo"  # Replace with the root directory path you want to explore
explore_directories(root_directory)
