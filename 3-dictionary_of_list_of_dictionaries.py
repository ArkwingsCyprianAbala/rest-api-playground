#!/usr/bin/python3
import json
import requests

users_url = "http://jsonplaceholder.typicode.com/users"

users_response = requests.get(users_url)

users_data = users_response.json()
all_tasks = {}

for user in users_data:
    user_id = user.get("id")
    username = user.get("username")

    todos_url = "http://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    todos_response = requests.get(todos_url)

    todos_data = todos_response.json()
    task_list = []
    for task in todos_data:
        task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
                }
        task_list.append(task_dict)
    all_tasks[str(user_id)] = task_list

#Write to JSON file
filename = "todo_all_employees.json"

with open(filename, mode="w") as json_file:
    json.dump(all_tasks, json_file)
