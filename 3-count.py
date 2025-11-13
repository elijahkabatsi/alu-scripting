#!/usr/bin/python3
"""
3-count.py
Recursively queries the Reddit API, parses titles of hot articles,
and prints a sorted count of given keywords (case-insensitive).
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
        """Recursively count occurrences of keywords in hot article titles."""
            if counts is None:
                        # Normalize word list: lowercase and combine duplicates
                                counts = {}
                                        for word in word_list:
                                                        key = word.lower()
                                                                    counts[key] = counts.get(key, 0) + 0  # initialize

                                                                        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                                                                            headers = {"User-Agent": "ALU-API-advanced/0.1"}
                                                                                params = {"limit": 100, "after": after}

                                                                                    try:
                                                                                                response = requests.get(url, headers=headers,
                                                                                                                                        params=params, allow_redirects=False)

                                                                                                        if response.status_code != 200:
                                                                                                                        return

                                                                                                                            data = response.json().get("data", {})
                                                                                                                                    posts = data.get("children", [])
                                                                                                                                            after = data.get("after")

                                                                                                                                                    # Count occurrences of each word in post titles
                                                                                                                                                            for post in posts:
                                                                                                                                                                            title = post["data"]["title"].lower().split()
                                                                                                                                                                                        for word in word_list:
                                                                                                                                                                                                            w = word.lower()
                                                                                                                                                                                                                            counts[w] = counts.get(w, 0) + title.count(w)

                                                                                                                                                                                                                                    # Base case: no more pages
                                                                                                                                                                                                                                            if after is None:
                                                                                                                                                                                                                                                            # Filter out words with zero counts
                                                                                                                                                                                                                                                                        filtered = {k: v for k, v in counts.items() if v > 0}
                                                                                                                                                                                                                                                                                    # Sort by count (desc), then alphabetically (asc)
                                                                                                                                                                                                                                                                                                for k, v in sorted(filtered.items(),
                                                                                                                                                                                                                                                                                                                                       key=lambda x: (-x[1], x[0])):
                                                                                                                                                                                                                                                                                                                    print(f"{k}: {v}")
                                                                                                                                                                                                                                                                                                                                return

                                                                                                                                                                                                                                                                                                                                    # Recursive call
                                                                                                                                                                                                                                                                                                                                            count_words(subreddit, word_list, after, counts)

                                                                                                                                                                                                                                                                                                                                                except Exception:
                                                                                                                                                                                                                                                                                                                                                            return

