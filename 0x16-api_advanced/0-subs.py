#!/usr/bin/python3
''' fetching subreddit data'''
import requests

def number_of_subscribers(subreddit):
    response = requests.get('https://reddit.com/subreddits/search.json', params={'q':subreddit})

    if response.json().get('data').get('children') == []:
        return 0

    response = requests.get(f'https://reddit.com/r/{subreddit}/about.json')

    return response.json().get('data').get('subscribers')
