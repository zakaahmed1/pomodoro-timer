from datetime import datetime, timedelta

def work_day_simulator():
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("17:00", "%H:%M")
    current_time = start_time
    work_interval = timedelta(minutes=25)

    total_work_time = timedelta()
    total_break_time = timedelta()

    print("Workday started at 9:00 AM.")
    
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

        break_duration = timedelta(minutes=break_minutes)
        current_time += break_duration
        total_break_time += break_duration

    print("\nWorkday ended.")
    print(f"Total work time: {total_work_time}")
    print(f"Total break time: {total_break_time}")

if __name__ == "__main__":
    work_day_simulator()
