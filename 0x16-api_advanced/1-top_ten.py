#!/usr/bin/python3
"""Function that queries the reddit api and prints the  \
     top 10 hot posts in a specific subreddit"""

import requests
import sys


def top_ten(subreddit):

    headers = {'User-Agent': 'unk'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
