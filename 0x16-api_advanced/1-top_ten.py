#!/usr/bin/python3
"""
Reddit APIs

This module contains a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    If not a valid subreddit, print None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 2'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json().get('data', {})
        children = data.get('children', [])
        if not children:
            print(None)
            return

        for child in children:
            title = child.get('data', {}).get('title')
            if title:
                print(title)
            else:
                print(None)

    except requests.RequestException:
        print(None)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
