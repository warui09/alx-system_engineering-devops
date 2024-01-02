#!/usr/bin/python3
"""Returns information about Employee TODO list progress in the following
    format:

First line: Employee EMPLOYEE_NAME is done with
    tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
    and non-completed tasks

Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
import sys

if __name__ == "__main__":
    if sys.argv[1]:
        id = sys.argv[1]

    name = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}").json()[
        "name"
    ]

    completed_tasks = []

    url_str = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    all_tasks = requests.get(url_str).json()

    for _, todo in enumerate(all_tasks):
        if todo["completed"]:
            completed_tasks.append(todo)

    done = len(completed_tasks)
    all_tasks = len(all_tasks)

    print(f"Employee {name} is done with tasks({done}/{all_tasks})")
    for todo in completed_tasks:
        print(f"\t{todo['title']}")
