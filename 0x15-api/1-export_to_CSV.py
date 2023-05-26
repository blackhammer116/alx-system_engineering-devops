#!/usr/bin/python3

"""
  These are fundamental modules for this task
"""
from csv import DictWriter, QUOTE_ALL
import requests
from sys import argv


if __name__ == ('__main__'):
    """
    This block gets the id from command line then
    gets the data from url using get api method
    then writes it to a .CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    employee_id = int(argv[1])
    response = requests.get(url.format(employee_id))
    todos = response.json()
    response2 = requests.get(url[:-6].format(employee_id))
    list1 = response2.json()
    employee_name = list1["username"]
    info_list = []
    for todo in todos:
        info = {}
        info.update({
            "user_id": employee_id,
            "username": employee_name,
            "status": todo.get("completed"),
            "task": todo.get("title")
            })
        info_list.append(info)
    with open(f"{employee_id}.csv", "w") as f:
        header = ["user_id", "username", "status", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(info_list)
