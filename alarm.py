from datetime import datetime, timedelta
import time

class AlarmClock:
    def __init__(self):
        self.alarm_time = None
        
    def set_alarm(self, alarm_time):
        try:
            parsed_time = datetime.strptime(alarm_time, "%H:%M")
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
            return
        self.alarm_time = parsed_time.strftime("%H:%M")
        print(f"\nAlarm set for {self.alarm_time}.")
        return True

    def view_alarm(self):
        if self.alarm_time is None:
            print("\nNo alarm is set.")
        else:
            print(f"\nAlarm is set for {self.alarm_time}.")

    def cancel_alarm(self):
        if self.alarm_time is None:
            print("\nNo alarm is set.")
            return
        print(f"\nAlarm for {self.alarm_time} has been canceled.")
        self.alarm_time = None

    def ring_alarm(self):
        print("\n\n" + "=" * 35)
        print("ALARM! ALARM! ALARM!")
        print("=" * 35)
        print("Time to wake up!")
        print("=" * 35 + "\n\n")
        print("\a")
        self.alarm_time = None
    
    def wait_for_alarm(self):
        if self.alarm_time is None:
            print("\nNo alarm is set.")
            return
        now=datetime.now()
        alarm_hour, alarm_minute = map(int, self.alarm_time.split(':'))
        alarm_datetime = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
        if alarm_datetime < now:
            alarm_datetime += datetime.timedelta(days=1)
        print((f"\nCurrent time: {now.strftime('%H:%M')}. Waiting for alarm at {self.alarm_time}..."))
        print("Press Ctrl+C to stop the clock.\n")
        
        try:
            while True:
                now=datetime.now()
                remaining_time = alarm_datetime - now
                if remaining_time.total_seconds()<=0:
                    print("\nAlarm ringing!")
                    self.ring_alarm()
                    break
                print(f"\nCurrent time: {now.strftime('%H:%M:%S')}. Time left for alarm: {remaining_time}.", end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nClock stopped. Returning to menu.")

def print_menu():
    print("\nAlarm Clock Menu:")
    print("1. Set Alarm")
    print("2. View Alarm")
    print("3. Cancel Alarm")
    print("4. Wait for Alarm")
    print("5. Exit")

def main():
    clock = AlarmClock()
    print("Welcome to the Alarm Clock!")
    
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            alarm_time = input("Enter the alarm time (HH:MM): ").strip()
            clock.set_alarm(alarm_time)
        elif choice == '2':
            clock.view_alarm()
        elif choice == '3':
            clock.cancel_alarm()
        elif choice == '4':
            clock.wait_for_alarm()
        elif choice == '5':
            print("Exiting the Alarm Clock. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()