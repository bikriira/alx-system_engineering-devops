#!/usr/bin/python3
"""
Find the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    import requests

    headers = {'User-Agent': 'reddit-app/0.0.1'}
    response = requests.get(
                            f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return (data["data"]["subscribers"])
    else:
        return 0
