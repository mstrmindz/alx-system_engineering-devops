#!/usr/bin/python3

import requests
import sys

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'CustomUserAgent'}
    
    # Construct the URL for the subreddit's information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            # Subreddit not found
            return 0
        else:
            # Other error occurred
            print(f"Error: {response.status_code} - {response.text}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return 0

# Test the function
subreddit_name = 'python'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The number of subscribers in r/{subreddit_name}: {subscribers_count}")
