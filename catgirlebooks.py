#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import sys
import argparse
from random import randint
from markovgenerator import MarkovGenerator
from catgirlebookscreds import *

parser = argparse.ArgumentParser(description='Generate tweets using Markov chains and post them')
parser.add_argument('inputjson', metavar='J', type=str, help='a json file containing preprocessed data for the Markov generator')
parser.add_argument('-s', action='store_true', help='flag for whether or not the post is scheduled. ie. driven by crontab')

args = parser.parse_args()

num = randint(1,16)

if num > 3:
    print(u'Not now, we rolled ' + str(num)
    sys.exit(1)

markov = MarkovGenerator()
markov.json_load(args.inputjson)

tweet = markov.construct_tweet(suffix=(u'#unscheduledtweet','')[args.s])

auth = tweepy.OAuthHandler(cons_key, cons_secret)

try:
    auth.set_access_token(access_token, access_token_secret)
    apisession = tweepy.API(auth)
    apisession.update_status(tweet)
    print(u'Successfully tweeted: ' + tweet + u'\n')
    
except:
    print(u'TWITTER AUTH FAIL')