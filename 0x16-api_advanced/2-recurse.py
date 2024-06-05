#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of
all hot articles for a given subreddit. If no results are found for
the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    headers = {'User-Agent': 'reddit-app/0.0.1'}
    params = {"count": 100, "after": after},
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_posts = data.get("data", {}).get("children", [])
        hot_list.extend([post["data"]["title"] for post in hot_posts])
        after = data.get("data", {}).get("after")

        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
