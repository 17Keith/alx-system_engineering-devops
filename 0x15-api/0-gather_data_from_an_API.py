#!/usr/bin/python3
"""This returns informatoon about an employee's todo list"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')

    todo = requests.get("https://jsonplaceholder.typicode.com/todos/")
    totalTasks = 0
    completed = 0

    for task in todo.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["     " + task.get('title') for task in todo.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
