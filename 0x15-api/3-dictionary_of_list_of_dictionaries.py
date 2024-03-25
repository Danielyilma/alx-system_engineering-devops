#!/usr/bin/python3
"""
The function retrieves and displays the completed tasks
of a specific employee from a JSON API.
"""
import json
import requests


def main():
    '''getting data for an api'''
    url = f'https://jsonplaceholder.typicode.com/users/'
    url2 = f'https://jsonplaceholder.typicode.com/todos'
    response1 = requests.get(url)
    response2 = requests.get(url2)
    task = response2.json()
    result = {}

    i = 0
    for user in response1.json():
        id = user.get('id')
        task_list = []
        for i in range(i, len(task)):
            if id != task[i].get('userId'):
                break
            dic = {}
            dic['username'] = user.get('username')
            dic['task'] = task[i].get('title')
            dic['completed'] = task[i].get('completed')
            task_list.append(dic)
        result[id] = task_list

    filename = 'todo_all_employees.json'

    with open(filename, 'w') as f:
        json.dump(result, f)


if __name__ == '__main__':
    main()
