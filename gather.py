#!/usr/bin/python3

import requests
import sys

if __name__=="__main__":
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = 0
    completed_tasks = []
    for task in todos_data:
        if task.get("completed") is True:
            done_tasks += 1
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
            employee_name, done_tasks, total_tasks))

    for title in completed_tasks:
            print("\t {}".format(title))

