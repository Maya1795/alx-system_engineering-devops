#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            results = response.json().get("data", {}).get("children", [])
            if not results:
                print("None")
            else:
                for post in results:
                    print(post.get("data", {}).get("title", "None"))
        else:
            print("None")
    except requests.RequestException:
        print("None")
    except ValueError:
        print("None")

