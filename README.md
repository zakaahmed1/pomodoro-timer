Workday Timer Script

This Python script helps to simulate a typical 9am-5pm workday and helps you stay productive by keeping track of the total amount of hours you spent working and taking breaks.

The script assumes you are working using the Pomodoro technique. The Pomodoro technique is a time management method that splits your workday into regular intervals, usually **25 minutes**, followed by a 5-minute break.

Normally, a person would work for 3 or 4 sprints at a time, followed by a longer break of 15-20 minutes. Remember to take your lunch break too! The script performs the following actions:

- Displays the current time
- Asks how long of a break you'd like to take
- Tracks total work and break time throughout the day

## Purpose

To help stay productive during the workday and avoid burnout!

## How to Run

1. Make sure you have Python 3 installed.
2. Clone the repository or download the Python file.
3. Open a terminal in the project directory.
4. Run the script using:

```bash
python workday_timer.py
```

You’ll be prompted to enter break durations after each 25-minute work session.

## Example

Finished 25 minutes of work. Current time: 09:25 AM  
How long is your break (in minutes)? 5

## Features

- Custom break input after each session
- Real-time clock tracking using Python's datetime module
- Simple and terminal-based

## Requirements

- Python 3
- No external packages required

## License

- MIT License

## Future Features

- [Adjustable start/end times](https://github.com/zakaahmed1/pomodoro-timer/issues/1)
- Visual progress tracker 
- Multi-person mode
- Real-time 25-minute timer with countdown
- Sound or desktop notification after each work/break period
- Daily summary export to CSV or text file
- Smart break suggestions based on productivity
- GUI version using Tkinter or a web framework like Flask

Made by Zaka Ahmed
