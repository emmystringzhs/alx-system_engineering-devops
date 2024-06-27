#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        print("None")
        return
    
    try:
        results = response.json().get("data")
        if results is None:
            print("None")
            return
    except ValueError:
        print("Error: Unable to decode JSON response")
        print(f"Response content: {response.text}")
        return
    
    for child in results.get("children", []):
        title = child.get("data", {}).get("title")
        if title:
            print(title)
