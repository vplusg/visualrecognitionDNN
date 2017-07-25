import json
import tweepy
from tweepy import OAuthHandler
 
def process_or_store(tweet):
    print(json.dumps(tweet))

consumer_key = 'FvpYJ2wsoX1x4kX3diMJjOx7d'
consumer_secret = 'gt447sGzfSo2HGn5KqPdStsHfaOhHyoGgNKXsJkLY1WphEi1Co'
access_token = '543950424-Uyo9RjutpuAZ8CAZ8uacrxTXPttwDd2420uhRFGO'
access_secret = 'bc6MwYXnufgYOS0FVq6wmzxxQ2ExBI0KHei4S6PRcdTtr'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text) 

print("-----------------HOME TIMELINE---------------")
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

print("-----------------FRIENDS---------------")
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)


print("-----------------USER TIMELINE---------------")
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)



