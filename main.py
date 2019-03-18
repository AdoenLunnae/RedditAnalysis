# !/bin/python
# -*- encoding: utf-8 -*-

import praw
import requests
import twitter
import random

import private


reddit = praw.Reddit(client_id=private.client_id,
                     client_secret=private.client_secret,
                     user_agent=private.user_agent)


# my_subreddits = [reddit.subreddit(x.name) for x in reddit.subreddits.search_by_name('memes') if not x.over18]

memereddit = reddit.subreddit('memes+')
api = twitter.Api(private.consumer_key,
                          private.consumer_secret,
                          private.access_token_key,
                          private.access_token_secret)
print(api.VerifyCredentials())
status = api.PostUpdate('Testing the bot #HackathonASL', media='https://i.redd.it/wqtbvzgm2sm21.jpg')


for submission in memereddit.hot(limit=200):
    response = requests.get(submission.url)
    if response.status_code == 200:
        name = submission.url.split('/')[3]
        with open("./images/{}".format(name), 'wb') as f:
            f.write(response.content)

