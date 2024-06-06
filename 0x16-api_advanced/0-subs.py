#!/usr/bin/python3
"""
Reddit API Query Module

This module contains a function to query the Reddit API and retrieve the number
of subscribers for a given subreddit. It handles invalid subreddits by returning 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers, or 0 if the subreddit is invalid or an error occurs.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
            else:
                return 0
        else:
            return 0
    except requests.RequestException:
        return 0
