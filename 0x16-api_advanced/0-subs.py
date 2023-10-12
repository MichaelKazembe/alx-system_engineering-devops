#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ functions that returns the number of subscribers """
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        date = response.json()

        subscribers = date['data'] ['subscribers']
        return subscribers
    
    else:
        return 0
