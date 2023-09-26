#!/usr/bin/python3
"""
Gets information about an employee by ID and
returns their TODO progress in Dict
"""

import json
from collections import OrderedDict
import requests
import sys


def get_users_dict():
    """" Get information to dict """
    employ = requests.get('https://jsonplaceholder.typicode.com/users')
    users = {}
    last = OrderedDict()
    filename = "todo_all_employees.json"

    for item in employ.json():
        users[item['id']] = item['username']

    with open(filename, 'w+') as f:
        for user in users:
            tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(user))
            tasks = tasks.json()
            result = []
            for task in tasks:
                final = OrderedDict()
                final['username'] = users[user]
                final['task'] = task['title']
                final['completed'] = task['completed']
                result.append(final)
            last[user] = result
        json.dump(last, f)


if __name__ == "__main__":
    get_users_dict()
