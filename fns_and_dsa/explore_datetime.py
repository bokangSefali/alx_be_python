# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Displays the current date and time in YYYY-MM-DD HH:MM:SS format
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(current_date):
    """
    Prompts the user for number of days and calculates the future date
    """
    days = int(input("Enter number of days to add: "))
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))


def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
