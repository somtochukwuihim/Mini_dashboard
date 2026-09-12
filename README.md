
# Welcome Stranger

## Why This Project

This project was created so as to demonstrate;

1. my ability to automate repetitive task and by proxy reduce time to ticket resolution.
1. to spot trends that can help prioritize tickets based on urgency
1. build little processes that helps during troubleshooting.
1. show my ability to write scripts and make them more efficient by finding and removing bugs and redundances.

## What Does This Script Do?

Polls support tickets by `open`, `close`, `high priority` and `most-open-customer`. 
This creates an overview, helps understand current status, spots ticket spike and zeros on customers with urgent need of attention.

## How to run it

```bash
python mini_dashboard.py ./mini_dashboard_practice_file.json
```

## Note on Changes Made Overtime to the Script

1. Initial commit
2. I refactored the code to only read the json file once(Do not repeat yourself principle).
   Then it passes it to the other function that needs it.
3. I made the code tie sensitive. It can now return more than one customer if there is a tie.
4. created the counter function to: loop through the tickets and compare; key to matching value condition.
5. Used the `.get()` to imbibe defensive programing incase a key returns an empty value. 
   This way it doesn't crash the script. 
   I also added the `sys.arg` command line tool to avoid hardcoding the file path into the script.

Thank you for reading.



