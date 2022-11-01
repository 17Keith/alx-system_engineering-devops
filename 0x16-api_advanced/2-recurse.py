#!/usr/bin/python3
"""Function that queries the reddit api and prints the  \
     all hot posts in a specific subreddit"""

from symbol import parameters
import requests
next = None


def recurse(subreddit, hot_list=[]):

    global next
    headers = {'User-Agent': 'unk'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'next': next}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=parameters)

    if response.status_code == 200:
        after_ = response.json().get('data').get('next')
        if after_ is not None:
            next = after_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
