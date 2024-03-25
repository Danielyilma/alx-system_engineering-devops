#!/usr/bin/python3
"""
The function retrieves and displays the completed tasks
of a specific employee from a JSON API.
"""
import csv
import requests
from sys import argv


def main():
    '''getting data for an api'''
    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    url2 = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    response = requests.get(url)
    name = response.json().get('name', None)
    csv_dict = []
    response = requests.get(url2)

    for task in response.json():
        dic = {}
        dic['id'] = task.get('id')
        dic['name'] = name
        dic['completed'] = task.get('completed')
        dic['title'] = task.get('title')
        csv_dict.append(dic)

    fields = ['id', 'name', 'completed', 'title']
    filename = argv[1] + '.csv'

    with open(filename, 'w') as f:
        write = csv.DictWriter(f, fieldnames=fields)
        write.writerows(csv_dict)


if __name__ == '__main__':
    main()
