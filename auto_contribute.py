   import os
   import datetime
   import sys
   from datetime import timezone, datetime

   FILE_NAME = "daily_log.txt"

   def update_log():
       try:
           # Debug: Print current time
           print("Starting update_log function...")
           
           # Get current time in UTC
           now = datetime.now(timezone.utc)
           print(f"Current UTC time: {now}")
           
           current_date = now.strftime("%Y-%m-%d")
           print(f"Formatted date: {current_date}")
           
           # Check if we already have an entry for today
           if os.path.exists(FILE_NAME):
               print(f"Found existing {FILE_NAME}")
               with open(FILE_NAME, "r") as file:
                   lines = [line for line in file.readlines() if line.strip() and not line.startswith('#')]
                   print(f"Found {len(lines)} existing entries")
                   if lines and current_date in lines[-1]:
                       print(f"Already contributed for {current_date}")
                       return
               contribution_count = len(lines) + 1
           else:
               print(f"Creating new {FILE_NAME}")
               contribution_count = 1

           # Create or update the log file
           current_time = now.strftime("%H:%M:%S")
           log_entry = f"Contribution Day {contribution_count} - {current_date} {current_time} UTC\n"
           print(f"Writing entry: {log_entry.strip()}")
           
           with open(FILE_NAME, "a") as file:
               file.write(log_entry)
           print(f"Successfully added contribution for {current_date}")
           
       except Exception as e:
           print(f"Error updating log: {str(e)}", file=sys.stderr)
           print(f"Error type: {type(e)}", file=sys.stderr)
           import traceback
           print(f"Traceback: {traceback.format_exc()}", file=sys.stderr)
           sys.exit(1)

   if __name__ == "__main__":
       update_log()
