import json
from twitter import TwitterStream, OAuth

'''
CONSUMER_KEY = raw_input('FvpYJ2wsoX1x4kX3diMJjOx7d')
CONSUMER_SECRET = raw_input('gt447sGzfSo2HGn5KqPdStsHfaOhHyoGgNKXsJkLY1WphEi1Co')
ACCESS_TOKEN = raw_input('543950424-Uyo9RjutpuAZ8CAZ8uacrxTXPttwDd2420uhRFGO')
ACCESS_SECRET = raw_input('bc6MwYXnufgYOS0FVq6wmzxxQ2ExBI0KHei4S6PRcdTtr')
'''
CONSUMER_KEY = 'FvpYJ2wsoX1x4kX3diMJjOx7d'
CONSUMER_SECRET = 'gt447sGzfSo2HGn5KqPdStsHfaOhHyoGgNKXsJkLY1WphEi1Co'
ACCESS_TOKEN = '543950424-Uyo9RjutpuAZ8CAZ8uacrxTXPttwDd2420uhRFGO'
ACCESS_SECRET = 'bc6MwYXnufgYOS0FVq6wmzxxQ2ExBI0KHei4S6PRcdTtr'
 
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.filter(follow="VijaiGandikota")

i = 50
    #
    # the number of tweets to read
    # a small number so that the code runs faster
    #
tweets = open("./static/tweets.json", "w")
    #
    # write to the static folder so that the file persists
    #
for tweet in iterator:
    tweet_raw = json.dumps(tweet)
    print >> tweets, tweet_raw
        #
        # write the entire tweet to a file, for use later
        #
    tweet_text = json.loads(tweet_raw.strip())
    if 'text' in tweet_text:
        print(tweet['text'].encode('utf-8'))
        #
        # so that only the text of the tweet
        # is displayed on the console
        # no need to see everything
        #
    i -= 1
    if i == 0:
        break
 
tweets.close()
