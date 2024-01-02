#!/usr/bin/python3
""" Returns information about Employee TODO list progress """

import requests
import sys

id = sys.argv[1]

name = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}").json()["name"]

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
