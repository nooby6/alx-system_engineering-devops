#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.

This script takes a user ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then writes the tasks to a CSV file named <user_id>.csv.
"""

import csv
import requests
import sys


def fetch_user_info(user_id):
    """Fetches user information from JSONPlaceholder API."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    return response.json()


def fetch_todo_list(user_id):
    """Fetches to-do list items associated with the user ID."""
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    return response.json()


def export_to_csv(user_id, username, todos):
    """Exports to-do list items to a CSV file."""
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["User ID", "Username", "Completed", "Title"])
        for todo in todos:
            writer.writerow([user_id, username, todo["completed"], todo["title"]])
    print(f"Export to CSV completed successfully: {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("User ID must be an integer")
        sys.exit(1)

    user = fetch_user_info(user_id)
    if not user:
        print(f"User with ID {user_id} not found.")
        sys.exit(1)

    username = user.get("username")
    todos = fetch_todo_list(user_id)
    if not todos:
        print(f"No to-do items found for user with ID {user_id}.")
        sys.exit(1)

    export_to_csv(user_id, username, todos)

