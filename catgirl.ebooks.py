import os
from markovbot import MarkovBot
from catgirlebookscreds import *

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'storyofheavens.txt')

tweetbot.read(book)

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

tweetbot.twitter_tweeting_start(days=0, hours=8, keywords=None, prefix=None, suffix=None)
