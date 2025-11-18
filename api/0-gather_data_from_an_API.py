#!/usr/bin/env python3
"""0-gather_data_from_an_API.py
Fetch employee TODO progress from a REST API and print it in the required format.

Usage:
    python3 0-gather_data_from_an_API.py <EMPLOYEE_ID>
"""

import sys
import requests

API_BASE = "https://jsonplaceholder.typicode.com"

def fetch_user(user_id):
    url = f"{API_BASE}/users/{user_id}"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        return r.json()
    return None

def fetch_todos(user_id):
    url = f"{API_BASE}/todos"
    params = {"userId": user_id}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer", file=sys.stderr)
        sys.exit(1)

    user = fetch_user(user_id)
    if user is None:
        # If user not found, exit quietly with code 1 (could also print an error)
        print(f"User with id {user_id} not found", file=sys.stderr)
        sys.exit(1)

    todos = fetch_todos(user_id)

    total = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    done_count = len(done_tasks)

    # First line
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), done_count, total))

    # Then titles of completed tasks, each preceded by one tab and one space
    for task in done_tasks:
        title = task.get("title", "")
        print("\t {}".format(title))

if __name__ == "__main__":
    main()

