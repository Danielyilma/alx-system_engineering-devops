#!/usr/bin/python3
'''using rest api'''
import requests
from sys import argv

url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
url2 = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
totalTask = 0
taskCompleted = 0

response = requests.get(url)
name = response.json().get('name', None)

response = requests.get(url2)

for task in response.json():
    if task.get('completed'):
        taskCompleted += 1
    totalTask += 1

print(f'Employee {name} is done with tasks({taskCompleted}/{totalTask}):')
for task in response.json():
    if task.get('completed'):
        print(f'\t {task.get("title")}')
