#!/usr/bin/python3
"""returns the number of subscribers of a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers, allow_redirects=False)
        subscribers = response["data"]["subscribers"]
        return subscribers
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
