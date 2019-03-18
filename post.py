# !/bin/python
# -*- encoding: utf-8 -*-

import json
import twitter
import random
import time

import private


def poster():
    api = twitter.Api(private.consumer_key,
                      private.consumer_secret,
                      private.access_token_key,
                      private.access_token_secret)
    with open('reddit.json', 'r') as f:
        subreddits = json.load(f)
    chosen_subreddit = random.choice(list(subreddits.keys()))
    chosen_image = random.choice(subreddits[chosen_subreddit])
    api.PostUpdate('From: /r/{}'.format(chosen_subreddit), media=chosen_image)
    subreddits[chosen_subreddit].remove(chosen_image)
    with open('reddit.json', 'w') as f:
        json.dump(subreddits, f)


if __name__ == '__main__':
    times = input('Number of tweets:    ')
    for x in range(int(times)):
        try:
            poster()
            time.sleep(5)
        except:
            print('Error')
