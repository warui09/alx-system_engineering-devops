#!/usr/bin/python3
"""Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1]:
        user_id = sys.argv[1]

        url = "https://jsonplaceholder.typicode.com/"

        user_name = requests.get(f"{url}users/{user_id}").json()["username"]

        url_tasks = f"{url}users/{user_id}/todos"

        all_tasks = requests.get(url_tasks).json()

        user_tasks = {
            user_id: [
                {"task": task["title"], "completed": task["completed"], "username": user_name}
                for task in all_tasks
            ]
        }

        with open(f'{user_id}.json', 'w') as json_file:
            json.dump(user_tasks, json_file, indent=2)
