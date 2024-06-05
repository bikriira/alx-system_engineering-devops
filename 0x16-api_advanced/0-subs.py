#!/usr/bin/python3
"""
Find the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    headers = {'User-Agent': 'reddit-app/0.1'}  # Updated User-Agent
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers=headers,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        print("OK")  # Print "OK" on success
        return data["data"]["subscribers"]
    else:
        print("Subreddit not found")  # Print message for invalid subreddit
        return 0
