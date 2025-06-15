import os
import datetime
import sys
from datetime import timezone

FILE_NAME = "daily_log.txt"

def update_log():
    try:
        # Get current UTC time
        current_utc = datetime.datetime.now(timezone.utc)
        current_date = current_utc.strftime("%Y-%m-%d")
        
        # Check if we already have an entry for today
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                lines = [line for line in file.readlines() if line.strip() and not line.startswith('#')]
                if lines and current_date in lines[-1]:
                    print(f"Already contributed for {current_date}")
                    return
            contribution_count = len(lines) + 1
        else:
            contribution_count = 1

        # Create or update the log file
        current_time = current_utc.strftime("%H:%M:%S")
        log_entry = f"Contribution Day {contribution_count} - {current_date} {current_time} UTC\n"
        
        with open(FILE_NAME, "a") as file:
            file.write(log_entry)
        print(f"Successfully added contribution for {current_date}")
        
    except Exception as e:
        print(f"Error updating log: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    update_log()
