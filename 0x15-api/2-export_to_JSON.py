#!/usr/bin/python3
"""
Gets information about an employee by ID and
returns their TODO progress in Json
"""

import json
from collections import OrderedDict
import requests
import sys


def get_user_json():
    """ Get user todo in json """
    employ = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(sys.argv[1]))
    name = employ.json().get('username')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))
    tasks = tasks.json()
    result = []
    last_id = OrderedDict()
    filename = sys.argv[1] + ".json"

    with open(filename, 'w+') as f:
        for task in tasks:
            last = OrderedDict()
            last['task'] = task['title']
            last['completed'] = task['completed']
            last['username'] = name
            result.append(last)
        last_id[sys.argv[1]] = result
        json.dump(last_id, f)


if __name__ == "__main__":
    get_user_json()
