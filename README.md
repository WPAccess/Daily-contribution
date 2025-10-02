# Daily Contribution Automation

This project automates the process of contributing to a GitHub repository every day. The script adds a commit with a timestamp and a message indicating the day of contribution, making it easier to track daily contributions and maintain a consistent GitHub activity streak.

## Features
- ✅ Automatically adds daily commits with UTC timestamp
- ✅ Commits a message indicating the day number (e.g., "Contribution Day 1")
- ✅ Prevents duplicate entries for the same day
- ✅ Git integration for automatic commits
- ✅ Works with GitHub Actions for seamless automation
- ✅ Can be configured to run periodically using cron jobs or GitHub Actions

## Usage

### Manual Execution
```bash
python3 auto_contribute.py
```

### Automated Execution
You can set up this script to run automatically using:

#### Cron Job (Linux/macOS)
```bash
# Add to crontab to run daily at 12:00 UTC
0 12 * * * cd /path/to/Daily-contribution && python3 auto_contribute.py
```

#### GitHub Actions
Create `.github/workflows/daily-contribution.yml`:
```yaml
name: Daily Contribution
on:
  schedule:
    - cron: '0 12 * * *'  # Run daily at 12:00 UTC
  workflow_dispatch:  # Allow manual trigger

jobs:
  contribute:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run daily contribution
        run: python3 auto_contribute.py
      - name: Push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git push
```

## How It Works

1. The script checks if a contribution has already been made for the current UTC date
2. If not, it adds a new entry to `daily_log.txt` with:
   - Contribution day number
   - Current UTC date and time
3. Makes a git commit with the changes
4. Optionally pushes to remote repository

## File Structure

- `auto_contribute.py` - Main script for daily contributions
- `daily_log.txt` - Log file containing all contribution entries
- `requirements.txt` - Python dependencies (none required)
- `README.md` - This documentation

## Requirements

- Python 3.6+
- Git repository initialized
- No external dependencies required

## Notes

- The script uses UTC time to ensure consistency across time zones
- Duplicate entries for the same day are automatically prevented
- The script will exit gracefully if git operations fail
- All timestamps are recorded in UTC format
