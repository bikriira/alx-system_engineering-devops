#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""


from pprint import pprint


def top_ten(subreddit):
    """
    Return top 10 posts of a given subreddit
    """
    import requests

    headers = {'User-Agent': 'reddit-app/0.0.1'}
    params = {'limit': 10}
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        pprint(data)
        for count in range(0, 10):
            print(data["data"]["children"][count]["data"]["title"])
    else:
        return None
