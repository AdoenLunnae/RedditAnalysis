# !/bin/python
# -*- encoding: utf-8 -*-

import praw
import requests
import twitter
import random
import json

import private


reddit = praw.Reddit(client_id=private.client_id,
                     client_secret=private.client_secret,
                     user_agent=private.user_agent)


my_subreddits = [reddit.subreddit(x.name) for x in reddit.subreddits.search_by_name('memes') if not x.over18]

memereddit = reddit.subreddit('memes+')
api = twitter.Api(private.consumer_key,
                          private.consumer_secret,
                          private.access_token_key,
                          private.access_token_secret)




#Lee del JSON
with open('reddit.json', "r") as f:
    subreddit = json.load(f)
    for url in subreddit:
        if response.status_code == 200:
        status = api.PostUpdate('Testing the bot', media=url)