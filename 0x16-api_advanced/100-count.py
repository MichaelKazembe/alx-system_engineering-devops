#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count
as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, results=None, after=None):
    """ recursive function that queries the Reddit API """
    if results is None:
        results = {}

    if subreddit is None or not isinstance(subreddit, str):
        return
    if not word_list:
        return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for keyword in word_list:
                if title.count(keyword) > 0:
                    results[keyword] = results.get(keyword, 0) +\
                                title.count(keyword)
            return count_words(subreddit, word_list, results,
                               data['data']['after'])
    else:
        return
