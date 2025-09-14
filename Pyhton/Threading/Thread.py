import threading
import time


def calculate_square(number: int) -> None:
    """
    Dummy function to simulate a calculation.
    Prints the square of the given number after a short delay.
    """
    print(f"[Worker] Starting calculation for {number}...")
    time.sleep(1)  # simulate some time-consuming work
    result = number * number
    print(f"[Worker] Finished! The square of {number} is {result}")


def main():
    print("[Main] Program started")

    calculate_square(5)

    # Create a thread that will run our dummy function
    worker_thread = threading.Thread(target=calculate_square, args=(7,))

    print("[Main] Starting worker thread...")
    worker_thread.start()

    # Main thread can continue doing its own work
    print("[Main] While worker is busy, main thread can do other things...")

    # Wait for worker to finish before exiting
    worker_thread.join()
    print("[Main] Worker thread has finished. Program ending.")


if __name__ == "__main__":
    main()
