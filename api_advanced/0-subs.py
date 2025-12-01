#!/usr/bin/python3
"""
0-subs.py
Gives the number of subs for a given subreddit using Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for subreddit. Return 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "alu-scripting:v1.0 (by /u/yourusername)"
    }

    try:
        resp = requests.get(url, headers=headers, allow_redirects=False,
                            timeout=10)
    except requests.RequestException:
        return 0

    # If non-200 (including redirects) treat as invalid subreddit
    if resp.status_code != 200:
        return 0

    try:
        data = resp.json()
    except ValueError:
        return 0

    # Safely extract subscribers (int), default to 0 if missing
    subscribers = data.get("data", {}).get("subscribers")
    if isinstance(subscribers, int):
        return subscribers

    return 0


if __name__ == "__main__":
    # Quick manual check (optional)
    import sys
    if len(sys.argv) > 1:
        print(number_of_subscribers(sys.argv[1]))
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
