#!/usr/bin/python3
"""
Exports all TODO tasks of a given employee to a CSV file.
"""

import csv
import requests
import sys


def fetch_employee_todos(employee_id):
    """Fetches employee info and all TODOs, returns (employee_name, todos)."""
    api_base = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_url = "{}/users/{}".format(api_base, employee_id)
    r_user = requests.get(user_url)
    if r_user.status_code != 200:
        return None, None
    user_data = r_user.json()
    employee_name = user_data.get("username")  # username for CSV

    # Fetch todos
    todos_url = "{}/todos".format(api_base)
    r_todos = requests.get(todos_url, params={"userId": employee_id})
    todos = r_todos.json()

    return employee_name, todos


def export_to_csv(employee_id, employee_name, todos):
    """Exports all tasks to CSV file USER_ID.csv."""
    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    username, todos = fetch_employee_todos(emp_id)
    if username is None:
        print("Employee not found")
        sys.exit(1)

    export_to_csv(emp_id, username, todos)


