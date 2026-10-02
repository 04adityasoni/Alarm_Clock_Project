# Python CLI Alarm Clock

A simple command-line alarm clock application built using Python's standard library.

This project was developed as a **30-minute coding exercise** with a focus on clean Python code, input validation, basic object-oriented design, and reliable time handling.

## Requirements

* Python 3.9+

The application uses only Python's standard library.

time and datetime libraries are used

## Usage

After starting the application, the following menu is displayed:

1. Set Alarm
2. View Alarm
3. Cancel Alarm
4. Start Clock
5. Exit

### 1. Set Alarm

Select option `1` and provide a time in `HH:MM` format.

Example:

Select an option: 1
Enter alarm time (HH:MM): 08:30

Alarm set for 08:30

The application uses 24-hour time.

Examples: 08:30, 13:45, 18:00

Invalid input is rejected:

Enter alarm time (HH:MM): 25:70

Invalid time format. Please use HH:MM.

### 2. View Alarm

Select option `2`:

Select an option: 2

Current alarm: 08:30

If no alarm is configured:

No alarm is currently set.

### 3. Cancel Alarm

Select option `3`:

Select an option: 3

Alarm 08:30 cancelled.

### 4. Start Clock

Select option `4` to start waiting for the alarm.

Example:

Current time: 08:29:50
Waiting for alarm: 08:30
Press Ctrl+C to stop the clock.

Current time: 08:29:51 | Alarm: 08:30
Current time: 08:29:52 | Alarm: 08:30
Current time: 08:29:53 | Alarm: 08:30

When the configured time is reached:

===================================
           ⏰ ALARM! ⏰
===================================
        Time to wake up!
===================================

The alarm is automatically cleared after it rings.

### 5. Exit

Select option `5`:

Goodbye!

## Interrupting the Clock

While the clock is waiting, the user can press:

Ctrl+C

The application catches `KeyboardInterrupt` and exits the waiting loop cleanly.

Example:

Current time: 08:29:50 | Alarm: 08:30
^C

Alarm clock stopped.

## Example Usage

$ python alarm.py

1. Set Alarm
2. View Alarm
3. Cancel Alarm
4. Start Clock
5. Exit

Select an option: 1

Enter alarm time (HH:MM): 08:30

Alarm set for 08:30

Select an option: 4

Current time: 08:29:57
Alarm: 08:30

⏰ ALARM! ⏰
Time to wake up!

Press Enter to continue...