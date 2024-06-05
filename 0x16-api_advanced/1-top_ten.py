#!/usr/bin/python3
"""
Find the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""


from pprint import pprint


def recurse(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    import requests

    hot_list = []
    headers = {'User-Agent': 'reddit-app/0.0.1'}
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for count in range(0, 10):
            hot_list.append(data["data"]["children"][count]["data"]["title"])
        return hot_list

    else:
        return None
