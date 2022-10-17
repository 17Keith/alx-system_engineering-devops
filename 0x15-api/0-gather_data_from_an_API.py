#!/usr/bin/python3
"""This returns informatoon about an employee's todo list"""

import requests
import sys

if __name__ == "__main__":

    employeeId = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employeeId))

    name = employee.json().get('name')

    todo = requests.get("https://jsonplaceholder.typicode.com/todos/")
    totalTasks = 0
    completed = 0

    for task in todo.json():
        if task.get('employeeId') == int(employeeId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todo.json()
          if task.get('employeeId') == int(employeeId) and task.get('completed')]))
