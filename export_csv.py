#!/usr/bin/python3

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
                ])

