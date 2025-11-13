#!/usr/bin/python3
"""
2-recurse.py
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALU-API-advanced/0.1"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Invalid subreddit
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])
        after = data.get("after")

        # Append current batch of titles
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Base case: no more pages
        if after is None:
            return hot_list

        # Recursive call
        return recurse(subreddit, hot_list, after)

    except Exception:
        return None
