#!/usr/bin/python3
""" Get top ten subreddit post"""

import requests


def top_ten(subreddit):
    """ Get top ten hot posts """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Ayo User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    posts = response.json.get('data').get('children')
    for post on posts[:10]:
        print(post.get('data').get('title'))
