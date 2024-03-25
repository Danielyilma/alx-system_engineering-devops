#!/usr/bin/python3
"""
The function retrieves and displays the completed tasks
of a specific employee from a JSON API.
"""
import json
import requests
from sys import argv


def main():
    '''getting data for an api'''
    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    url2 = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'

    response = requests.get(url2)

    filename = argv[1] + '.json'

    with open(filename, 'w') as f:
        json.dump({argv[1]: response.json()}, f)


if __name__ == '__main__':
    main()
