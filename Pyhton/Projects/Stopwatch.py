import time
import sys

def stopwatch(duration):
    start_time = time.time()  # Record the start time

    try:
        while True:
            # Calculate elapsed time
            elapsed_time = time.time() - start_time
            seconds = int(elapsed_time)
            milliseconds = int((elapsed_time - seconds) * 1000)
            
            # Print time in seconds and milliseconds on the same line
            sys.stdout.write(f"\rElapsed time: {seconds} seconds {milliseconds} milliseconds")
            sys.stdout.flush()
            
            # Exit the loop if the duration has passed
            if elapsed_time >= duration:
                break

            time.sleep(0.01)  # Sleep a bit to reduce CPU usage

    except KeyboardInterrupt:
        # Handle Ctrl+C to stop the stopwatch if needed
        print("\nStopwatch stopped.")
        elapsed_time = time.time() - start_time
        seconds = int(elapsed_time)
        milliseconds = int((elapsed_time - seconds) * 1000)
        print(f"Elapsed time: {seconds} seconds {milliseconds} milliseconds")

# Run the stopwatch function for 100 seconds
stopwatch(100)
