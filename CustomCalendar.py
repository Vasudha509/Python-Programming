import calendar
from datetime import datetime

class CustomCalendar:
    def __init__(self, separator=" "):
        """Initialize the calendar with a default separator (space)."""
        self.separator = separator

    def set_separator(self):
        """Prompt the user to set a custom separator."""
        self.separator = input("Enter your desired separator (e.g., '-', '*', '|', etc.): ") or self.separator

    def display_month(self, year, month):
        """Return a string representation of a single month with the chosen separator."""
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(year, month)
        return cal_str.replace(" ", self.separator)

    def display_year_grid(self, year, rows, cols):
        """Display the calendar for an entire year in a specified grid format."""
        if rows * cols < 1 or rows * cols > 12:
            print("Invalid grid size. The grid must accommodate 1 to 12 months.")
            return

        month = 1
        while month <= 12:
            row_months = []
            for _ in range(cols):
                if month > 12:
                    break
                row_months.append(self.display_month(year, month))
                month += 1

            month_lines = [m.splitlines() for m in row_months]
            for lines in zip(*month_lines):
                print("   ".join(lines))
            print("\n" + "=" * 70)

    def get_day_of_week(self, date_str):
        """Get the day of the week for a specific date."""
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            day_of_week = date.strftime("%A")
            print(f"The day of the week for {date_str} is: {day_of_week}")
        except ValueError:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")

    def run(self):
        """Main method to interact with the user and display the calendar."""
        print("Welcome to the Custom Calendar Program!\n")
        self.set_separator()

        try:
            year = int(input("\nEnter the year (e.g., 2024): "))
            rows = int(input("\nEnter the number of rows for the grid (e.g., 2): ") or 3)
            cols = int(input("\nEnter the number of columns for the grid (e.g., 4): ") or 4)
            self.display_year_grid(year, rows, cols)
        except ValueError:
            print("\nInvalid input. Please enter valid integers for year, rows, and columns.")
            return

        while True:
            date_check = input("\nWould you like to check the day of a specific date? (y/n): ").lower()
            if date_check == 'y':
                date_str = input("\nEnter the date (YYYY-MM-DD): ")
                self.get_day_of_week(date_str)
            elif date_check == 'n':
                print("\nThank you for using the Custom Calendar Program!")
                break
            else:
                print("\nPlease enter 'y' or 'n'.")

if __name__ == "__main__":
    calendar_app = CustomCalendar()
    calendar_app.run()
