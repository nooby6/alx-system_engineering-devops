#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""

import requests


def count_words(subreddit, word_list, after="", counts=None):
    """Recursively queries the Reddit API and counts occurrences of keywords."""
    if counts is None:
        counts = {}
    if not after:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data")
        if not data:
            return

        articles = data.get("children", [])
        for article in articles:
            title = article.get("data", {}).get("title", "").lower()
            for word in word_list:
                if word.lower() in title.split():
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            if counts:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
            return

    except requests.RequestException as e:
        return


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: ./count_words.py <subreddit> <word_list>")
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
