# !/bin/python
# -*- encoding: utf-8 -*-

import praw
import re

import private


reddit = praw.Reddit(client_id=private.client_id,
                     client_secret=private.client_secret,
                     user_agent=private.user_agent)


listing = reddit.subreddits.search_by_name('memes', exact=False)

for item in listing:
    print(item)
