#!/usr/bin/env python3
import sys
import requests

API_BASE = "https://jsonplaceholder.typicode.com"

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

try:
    user_id = int(sys.argv[1])
except ValueError:
    print("Employee ID must be an integer")
    sys.exit(1)

# Fetch user
user_url = "{}/users/{}".format(API_BASE, user_id)
r_user = requests.get(user_url)
if r_user.status_code != 200:
    print("Error: user not found")
    sys.exit(1)
user_data = r_user.json()
employee_name = user_data.get("name")

# Fetch todos
todos_url = "{}/todos".format(API_BASE)
r_todos = requests.get(todos_url, params={"userId": user_id})
todos = r_todos.json()

total_tasks = len(todos)
done_tasks = [t for t in todos if t.get("completed") is True]
done_count = len(done_tasks)

print("Employee {} is done with tasks({}/{}):".format(employee_name, done_count, total_tasks))

for task in done_tasks:
    print("\t {}".format(task.get("title")))

