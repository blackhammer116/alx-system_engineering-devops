#!/usr/bin/python3

"""
  These are fundamental modules for this task
"""
import json
import requests
from sys import argv


if __name__ == ('__main__'):
    """
    This script gets all information from each
    employee and dumps it in a .JSON file
    """
    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    response = requests.get(url[:-9])
    users = response.json()
    total_users = len(users)
    list_all = {}
    for i in range(1, total_users + 1):
        response1 = requests.get(url[:-6].format(i))
        response2 = requests.get(url.format(i))
        todos = response2.json()
        user = response1.json()
        employee_name = user["username"]
        employee_id = user["id"]
        small = []
        for todo in todos:
            small_dict = {}
            small_dict.update({"username": employee_name, "task": todo.get(
                "title"), "completed": todo.get("completed")})
            small.append(small_dict)
        list_all.update({employee_id: small})
    with open("todo_all_employees.json", "w") as f:
        json.dump(list_all, f)
