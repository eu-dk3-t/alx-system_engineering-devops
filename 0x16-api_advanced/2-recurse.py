#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after='', tposts=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=100"
    headers = {
        "User-Agent": "eu-dk3-t"
    }
    lim = {
        'after': after
    }
    response = requests.get(url, headers=headers, params=lim,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    posts = results.get("dist")
    tposts += posts
    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, tposts)
    return hot_list
