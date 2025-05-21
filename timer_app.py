# datetime handles clock time, timedelta handles time differences
from datetime import datetime, timedelta

# function to keep track of the amount of hours worked and total break time
def work_day_simulator():
     # strptime converts a string ("09:00") to datetime using the format specificied ("%H:%M")
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("17:00", "%H:%M")
    current_time = start_time # initialise current_time as we need to keep track of the current time throughout the day
    work_interval = timedelta(minutes=25) # assumes each work session to be 25 minutes (standard for Pomodoro technique)

    # Initialise tracking
    total_work_time = timedelta()
    total_break_time = timedelta()

    print("Workday started at 9:00 AM.")
    
    # Main loop of function that keeps going until we have gone past end_time defined at the beginning of the function
    while current_time + work_interval <= end_time:
        # Do work
        current_time += work_interval
        total_work_time += work_interval

        # Show current time and ask for break
        print(f"\nFinished 25 minutes of work. Current time: {current_time.strftime('%I:%M %p')}")
        try:
            break_minutes = int(input("How long is your break (in minutes)? "))
        except ValueError:
            print("Invalid input. Assuming 0 minutes break.")
            break_minutes = 0

        # Add break duration to total break time and append current time by the break duration
        break_duration = timedelta(minutes=break_minutes)
        current_time += break_duration
        total_break_time += break_duration
        
    # Once the loop ends, it means we have gone past the end_time. Now show the total work and break time
    print("\nWorkday ended.")
    print(f"Total work time: {total_work_time}")
    print(f"Total break time: {total_break_time}")

if __name__ == "__main__":
    work_day_simulator()
