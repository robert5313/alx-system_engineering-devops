#!/usr/bin/python3
""" Function for the Reddit API and returns the
 number of subscibers"""
import requests


def number_of_subscribers(subreddit):
    """Returns all the list of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
