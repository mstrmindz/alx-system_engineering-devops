#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
            headers = {"User-Agent": "My Reddit Scraper"}  # Set a custom User-Agent header

                response = requests.get(url, headers=headers, allow_redirects=False)
                    if response.status_code == 200:
                                data = response.json()
                                        subscribers = data["data"]["subscribers"]
                                                return subscribers
                                                else:
                                                            return 0
