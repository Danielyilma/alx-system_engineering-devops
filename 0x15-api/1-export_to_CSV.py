#!/usr/bin/python3
"""exporting api from third party to a csv file"""
import csv
import requests
from sys import argv


"""
The code block starting with `if __name__ == '__main__':`
is the main entry point of the script. It is executed when
the script is run directly (not imported as a module).
"""
if __name__ == '__main__':
    url = F"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    to_do = "/todos"
    name = ""
    with requests.get(url) as response:
        name = response.json()['username']
    url = url + to_do
    task_completed = 0
    with requests.get(url) as response:
        response = response.json()
        for i in response:
            if i['completed'] is True:
                task_completed += 1
        with open(str(argv[1]) + ".csv", "w", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for i in response:
                line = [argv[1], name, i['completed'], i['title']]
                csv_writer.writerow(line)
