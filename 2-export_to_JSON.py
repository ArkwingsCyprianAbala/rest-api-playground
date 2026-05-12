#!/usr/bin/python3
import json
import requests
import sys

employee_id = sys.argv[1]

user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
user_response = requests.get(user_url)
user_data = user_response.json()
username = user_data.get("username")
todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
todos_response = requests.get(todos_url)
todos_data = todos_response.json()

tasks_list = []
for task in todos_data:
        task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                }
        tasks_list.append(task_dict)
# Create final dictionary
json_data = {
            employee_id: tasks_list
            }
# Create JSON file
filename = "{}.json".format(employee_id)

with open(filename, mode="w") as json_file:
        json.dump(json_data, json_file, indent=4)
