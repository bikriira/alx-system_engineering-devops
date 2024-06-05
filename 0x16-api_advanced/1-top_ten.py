#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Return top 10 posts of a given subreddit
    """

    headers = {'User-Agent': 'reddit-app/0.0.1'}
    params = {'limit': 10}
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code == 200:
        all_data = response.json()
        wanted_data = all_data["data"]["children"]
        for data in wanted_data:
            if not data.get("data").get("stickied") or data["data"].get("pinned"):
                print(data.get("data").get("title"))
    else:
        print("None")
