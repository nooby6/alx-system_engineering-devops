#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=""):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot articles
    for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): The list of titles collected so far (used in recursion).
    after (str): The parameter for pagination (used in recursion).

    Returns:
    list: A list of titles of hot articles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My User Agent 3"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        results = response.json().get("data", {})
        after = results.get("after")
        children = results.get("children", [])

        if not children and after is None:
            return None

        for child in children:
            title = child.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        if after:
            return recurse(subreddit, hot_list, after)
        else:
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

