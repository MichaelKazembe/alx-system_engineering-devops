#!/usr/bin/python3
"""
Recursive function that queries the Reddit API 
and returns a list containing the titles of all hot articles
for a given subreddit. 
If no results are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list
    of hot articles' titles for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params,
                              allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return(hot_list)
        else:
            for post in posts:
                hot_list.append(post['data']['title'])
            return recurse(subreddit, hot_list, data['data']['after'])
    
    else:
                                                                                                                                                                                return(None)
