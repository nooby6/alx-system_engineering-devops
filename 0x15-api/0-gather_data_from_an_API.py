#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    user_url = url + "users/{}".format(employee_id)
    user = requests.get(user_url).json()

    # Get the to-do list for the employee using the provided employee ID
    todos_url = url + "todos"
    params = {"userId": employee_id}
    todos = requests.get(todos_url, params=params).json()

    # Filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the employee's name and the number of completed tasks
    employee_name = user.get("name")
    total_tasks = len(todos)
    number_of_done_tasks = len(completed)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    # Print the completed tasks one by one with indentation
    for complete in completed:
        print("\t {}".format(complete))

