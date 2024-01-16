#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            if "data" in data and "children" in data["data"]:
                posts = data["data"]["children"]
                for post in posts:
                    print(post["data"]["title"])
        elif response.status_code == 302:
            print("Invalid subreddit. Redirects to search results.")
        else:
            print("Error: Unable to fetch data.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
