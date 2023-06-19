#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
        if word_counts is None:
                    word_counts = {}
                        if after is None:
                                    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
                                        else:
                                                    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
                                                                headers = {"User-Agent": "My Reddit Scraper"}  # Set a custom User-Agent header

                                                                    response = requests.get(url, headers=headers, allow_redirects=False)
                                                                        if response.status_code == 200:
                                                                                    data = response.json()
                                                                                            posts = data["data"]["children"]
                                                                                                    for post in posts:
                                                                                                                    title = post["data"]["title"]
                                                                                                                                for word in word_list:
                                                                                                                                                    word = word.lower()
                                                                                                                                                                    if title.lower().count(word) > 0 and not title.endswith(('.', '!', '_')):
                                                                                                                                                                                            if word in word_counts:
                                                                                                                                                                                                                        word_counts[word] += title.lower().count(word)
                                                                                          else:
                                                                                                                      word_counts[word] = title.lower().count(word)

                                                                                                                              if data["data"]["after"] is not None:
                                                                                                                                              return count_words(subreddit, word_list, after=data["data"]["after"], word_counts=word_counts)
                                                                                                                                                  else:
                                                                                                  sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
                                                                                                              for word, count in sorted_counts:
                                                                                                                                  print(f"{word}: {count}")
                                                                                                                                      else:
                                                                                                                                   print("Invalid subreddit or no posts match.")

                                                                                                                                   # Example usage
                                                                                                                                   subreddit = "python"
                                                                                                                                   keywords = ["python", "java", "javascript"]
                                                                                                                                   count_words(subreddit, keywords)

