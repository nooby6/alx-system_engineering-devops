#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "My User Agent 3"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 404:
            return None
        
        results = response.json().get("data", {})
        after = results.get("after")
        count += results.get("dist", 0)
        for c in results.get("children", []):
            hot_list.append(c.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except requests.RequestException:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        titles = recurse(sys.argv[1])
        if titles:
            for title in titles:
                print(title)
        else:
            print(None)
