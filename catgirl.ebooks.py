#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, sys
from markovgenerator import MarkovGenerator
from catgirlebookscreds import *

argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
apisession = tweepy.API(auth)

openfile = open(argfile, r)
file = openfile.readlines()
openfile.close()

apisession.update_status()

# import os
# dirname = os.path.dirname(os.path.abspath(__file__))
# book = os.path.join(dirname, 'storyofheavens.txt')
# tweetbot.read(book)
# tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
# tweetbot.twitter_tweeting_start(days=0, hours=8, keywords=None, prefix=None, suffix=None)
