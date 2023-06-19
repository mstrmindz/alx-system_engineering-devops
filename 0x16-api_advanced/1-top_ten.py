import requests

def top_ten(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
            headers = {"User-Agent": "My Reddit Scraper"}  # Set a custom User-Agent header

                response = requests.get(url, headers=headers, allow_redirects=False)
                    if response.status_code == 200:
                                data = response.json()
                                        posts = data["data"]["children"]
                                                for post in posts:
                                                                title = post["data"]["title"]
                                                                            print(title)
                                                                                else:
                                                                                            print("None")

                                                                                            # Example usage
                                                                                            subreddit = "python"
                                                                                            top_ten(subreddit)

