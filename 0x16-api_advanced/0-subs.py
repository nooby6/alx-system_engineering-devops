#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit to query.
    
    Returns:
    int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

# Example usage
if __name__ == "__main__":
    print(number_of_subscribers('learnpython'))  # Example valid subreddit
    print(number_of_subscribers('thissubredditdoesnotexist123'))  # Example invalid subreddit
