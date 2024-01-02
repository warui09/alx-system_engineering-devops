#!/usr/bin/python3
"""Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1]:
        user_id = sys.argv[1]

        url = "https://jsonplaceholder.typicode.com/"

        user_name = requests.get(f"{url}users/{user_id}").json()["username"]

        url_tasks = f"{url}users/{user_id}/todos"

        all_tasks = requests.get(url_tasks).json()

        with open(f"{user_id}.csv", "w") as csv_file:
            my_writer = csv.writer(csv_file, quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
            for task in all_tasks:
                my_writer.writerow([user_id, user_name, task["completed"],
                task["title"]])
