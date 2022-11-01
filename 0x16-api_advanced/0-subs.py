#!/usr/bin/python3
"""Function that queries the reddit api and returns the number of \
     subscribers in a specific subreddit"""


import requests


def number_of_subscribers(subreddit):

    headers = {'User-Agent': 'unk'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
