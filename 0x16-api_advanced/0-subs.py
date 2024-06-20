#!/usr/bin/python3
"function to query subcribation"
import requests

def number_of_subscribers(subreddit):
    """return total of subscribtion"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            results = response.json()
            return results.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
    except ValueError:
        return 0
