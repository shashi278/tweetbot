import tweepy
from time import sleep
from random import randint
import re

#credentials
consumer_key= ''
consumer_secret_key= ''
access_token=''
access_token_secret=''

auth= tweepy.OAuthHandler(consumer_key, consumer_secret_key)

auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

user= api.me()
print(user.name)



search= ''

no_of_tweets=30
count=0

#get only non-retwitted tweets
tweets= [x for x in tweepy.Cursor(api.search, search, tweet_mode= 'extended').items(no_of_tweets) if not re.search('RT', x.full_text)]

for tweet in tweets:
	try:
		
		#for debugging purpose
		#print(tweet)
		tweet_id= tweet.id
		tweet_user= tweet.user.screen_name
		tweet_username= tweet.user.name
		print('_'*10)
		print(tweet.id)
		print(tweet.user.screen_name)
		print(tweet_username)
		print(tweet.full_text)
		print('_'*10)
		
		#extract only the full text of tweet
				api.update_status(tweet.full_text)
		print('updated: {}'.format(count+1))
		count+=1
		sleep(5)
	
	except tweepy.TweepError as e:
		print(e.reason)
