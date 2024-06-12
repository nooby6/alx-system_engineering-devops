#!/usr/bin/python3
"""
Python script that, using the JSONPlaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display TODO list progress for a given employee."""
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found")
        return
    employee = response.json()

    # Fetch employee's TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee ID {employee_id}")
        return
    todos = response.json()

    # Employee name
    employee_name = employee.get("name")

    # Number of completed tasks and total tasks
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

