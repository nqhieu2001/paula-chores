import tweepy
from time import sleep
from config import *

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
cur = tweepy.Cursor(api.user_timeline,id="quihieu")
for page in cur.pages():
	for tweet in page:
		