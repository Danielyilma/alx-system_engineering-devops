#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """prints the titles of the top ten hot posts for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
    r = requests.get(
        'http://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    )

    if r.status_code == 200:
        r = r.json().get('data', None)
        for i in r.get('children', None):
            print(i.get("data").get('title', None))
    else:
        print(None)
