import sys

def print_greet_user(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print_greet_user(sys.argv[1])
        print_greet_user(sys.argv[2])
    else:
        print("Please two names to the  script!")