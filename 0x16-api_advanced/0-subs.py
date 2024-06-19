#!/usr/bin/python3
"function to query subcribation"
import requests

def number_of_subscribers(subreddit):
    """return total of subscribtion"""
    url = "https://www.reddit.com/r/{}/about.joson".format(subreddit)
    headers = {
            "user-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")
