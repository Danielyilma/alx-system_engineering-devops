#!/usr/bin/python3
"""
The function retrieves and displays the completed tasks
of a specific employee from a JSON API.
"""
from sys import argv
import csv
import requests


def main():
    '''getting data for an api'''
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        argv[1]
    )
    url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1]
    )
    response = requests.get(url)
    name = response.json().get('username', None)
    csv_dict = []
    response = requests.get(url2)

    for task in response.json():
        dic = {}
        dic['userId'] = task.get('userId')
        dic['username'] = name
        dic['completed'] = task.get('completed')
        dic['title'] = task.get('title')
        csv_dict.append(dic)

    fields = ['userId', 'username', 'completed', 'title']
    filename = argv[1] + '.csv'

    with open(filename, 'w', encoding='utf-8') as f:
        write = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        write.writerows(csv_dict)


if __name__ == '__main__':
    main()
