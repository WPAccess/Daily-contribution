import os
import datetime
import sys
import subprocess
from datetime import timezone

FILE_NAME = "daily_log.txt"

def make_git_commit(message):
    """Make a git commit with the given message."""
    try:
        # Add the log file to git
        subprocess.run(["git", "add", FILE_NAME], check=True, capture_output=True)
        
        # Make the commit
        subprocess.run(["git", "commit", "-m", message], check=True, capture_output=True)
        
        # Push to remote (optional, can be commented out if not needed)
        # subprocess.run(["git", "push"], check=True, capture_output=True)
        
        print(f"Git commit successful: {message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git commit failed: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Git error: {str(e)}", file=sys.stderr)
        return False

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
        
        # Make a git commit
        commit_message = f"Daily contribution #{contribution_count} - {current_date}"
        if not make_git_commit(commit_message):
            print("Error: log updated but git commit failed", file=sys.stderr)
            sys.exit(1)
        
    except Exception as e:
        print(f"Error updating log: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    update_log()
