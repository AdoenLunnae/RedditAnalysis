# !/bin/python
# -*- encoding: utf-8 -*-

import json
import praw
import requests

import private


def scan(reddit, limit, subreddit_name):
    with open('reddit.json', 'r') as f:
        subreddits = json.load(f)

    subreddit = reddit.subreddit(subreddit_name)

    if subreddit not in subreddits:
        subreddits.update({subreddit.display_name: []})
    for submission in subreddit.hot(limit=int(limit)):
        response = requests.get(submission.url)
        if response.status_code == 200:
            subreddits[subreddit.display_name].append(submission.url)
    print(subreddits)
    with open('reddit.json', 'w') as f:
        json.dump(subreddits, f)


if __name__ == '__main__':
    reddit_agent = praw.Reddit(client_id=private.client_id,
                               client_secret=private.client_secret,
                               user_agent=private.user_agent)
    target_limit = input('Introduce number of posts    ')
    target_subreddit = input('Introduce subreddit    ')
    scan(reddit_agent, target_limit, target_subreddit)
