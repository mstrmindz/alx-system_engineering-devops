#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
            headers = {"User-Agent": "My Reddit Scraper"}  # Set a custom User-Agent header

                response = requests.get(url, headers=headers, allow_redirects=False)
                    if response.status_code == 200:
                                data = response.json()
                                        posts = data["data"]["children"]
                                                for post in posts:
                                                                title = post["data"]["title"]
                                                                            hot_list.append(title)

                                                                                    if data["data"]["after"] is not None:
                                                                                                    return recurse(subreddit, hot_list=hot_list)

                                                                                                    return hot_list if hot_list else None

                                                                                                # Example usage
                                                                                                subreddit = "python"
                                                                                                titles = recurse(subreddit)
                                                                                                if titles is None:
                                                                                                        print("No results found for the subreddit.")
                                                                                                    else:
                                                                                                            print("Titles of hot articles:")
                                                                                                                for title in titles:
                                                                                                                            print(title)

