#!/usr/bin/python3
"""Module listing the title of top 10 hot post in the subreddit"""
import requests


def top_ten(subreddit):
    """list the title of top 10 hot post in the subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    user = {'User-Agent': 'Test123'}
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    for post in response.json().get('data').get('children'):
        print(post.get('data').get('title'))