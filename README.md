# 0-gather_data_from_an_API

## Project Description
This project contains a Python script that fetches and displays the TODO list progress of an employee using the JSONPlaceholder REST API.  
Given an employee ID, the script shows the number of completed tasks, total tasks, and the titles of completed tasks.

## Files
- `api/0-gather_data_from_an_API.py`: Main Python script for fetching and displaying TODO list progress.

## Requirements
- Python 3.4
- `requests` library
- Ubuntu 14.04 LTS compatible
- All files are executable and PEP 8 compliant

## Usage
```bash
# Run the script with an employee ID
python3 api/0-gather_data_from_an_API.py <employee_id>

# Example:
python3 api/0-gather_data_from_an_API.py 2
```

Output format:

```
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
     TASK_TITLE_1
     TASK_TITLE_2
     ...
```

## Notes
- The script uses `dict.get()` for safe dictionary key access.
- The code is protected against execution on import using `if __name__ == "__main__":`.
- Compatible with Python 3.4 and Ubuntu 14.04 LTS.

