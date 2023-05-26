#!/usr/bin/python3

import requests
from sys import argv
"""
  These are funcdamental modules for this task
"""


if __name__ == ('__main__'):
    """
    This block gets the id from command line then
    gets the data from url using get api method
    then displays the data.
    """
    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    employee_id = int(argv[1])
    response = requests.get(url.format(employee_id))
    todos = response.json()
    response2 = requests.get(url[:-9])
    list1 = response2.json()
    completed = sum(1 for todo in todos if todo["completed"])
    employee_name = list1[employee_id]["name"]
    total = len(todos)
    print("Employee {} is done with \
            tasks({}/{}):".format(employee_name, completed, total))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
