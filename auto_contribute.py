import os
import datetime

FILE_NAME = "daily_log.txt"

def update_log():
    # Determine the number of contributions by counting lines in the log file
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        contribution_count = len(lines) + 1
    else:
        contribution_count = 1

    # Create or update the log file
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Contribution Day {contribution_count} - {current_date}\n"
    with open(FILE_NAME, "a") as file:
        file.write(log_entry)

if __name__ == "__main__":
    update_log()
