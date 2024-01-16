#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=None):
    """queries the Reddit API and returns a list containing the titles of all
    hot articles"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-agent": "Mozilla/5.0"}

    params = {}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        response.raise_for_status()

        data = response.json()

        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            for post in posts:
                hot_list.append(post["data"]["title"])

        if data.get("data", {}).get("after"):
            recurse(subreddit, hot_list, after=data["data"]["after"])
    except requests.RequestException as e:
        if (
            isinstance(e, requests.exceptions.HTTPError)
            and e.response.status_code == 302
        ):
            print(f"Invalid subreddit: {subreddit}")
            return None
        else:
            print(f"Error fetching data: {e}")
            return None

    return hot_list
