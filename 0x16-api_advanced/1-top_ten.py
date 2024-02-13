#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {
        "User-Agent": "eu-dk3-t"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    resp_d = response.json()
    resp_d = resp_d.get('data', {})
    resp_l = resp_d.get('children', [])
    for post in resp_l:
        post_dict = post.get('data', {})
        title = post_dict.get('title')
        if title is not None:
            print(title)
