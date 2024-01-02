#!/usr/bin/python3
"""Records all tasks that are owned by all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(f"{url}users").json()

    all_tasks = {}

    for user in users:
        user_id = user["id"]
        tasks = requests.get(f"{url}users/{user_id}/todos").json()

        user_tasks = [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in tasks
        ]

        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=2)
