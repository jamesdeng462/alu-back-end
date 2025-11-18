#!/usr/bin/python3
"""
Script that returns TODO list information for a given employee ID
using the JSONPlaceholder REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    done_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done, total_tasks))

    for title in done_tasks:
        print("\t {}".format(title))

