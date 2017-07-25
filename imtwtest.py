import json
from pprint import pprint
import tweepy
from tweepy import OAuthHandler
from nltk import tokenize
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition
from watson_developer_cloud import ConversationV1

visual_recognition = VisualRecognition('2016-05-20',
    api_key='561af6fbe99635bb0a7b15f0865de0f4b3f847fe')

 
def classify_image(url):
    #print(json.dumps(visual_recognition.classify(images_url=url, classifier_ids=["allowedvsnot_1765920808"]),indent=2))
    return json.dumps(visual_recognition.classify(images_url=url, classifier_ids=["allowedvsnot_1765920808"]),indent=2)

def find_intent(s):
    workspace_id='050f8ec3-55aa-4459-8e74-ede9346d745f'
    conversation = ConversationV1(
    username='d7d6863f-5b3b-4395-a866-2963d96ddbd2',
    password='LQdY0tHt0TIC',
    version='2017-05-26'
    )
    response = conversation.message(workspace_id=workspace_id, message_input={
    'text': s})
    #print(json.dumps(response, indent=2))
    return response['intents'][0]['intent']

def get_user_screen_name(tweet):
    user_screen_name=tweet['user']['screen_name']
    return user_screen_name

def get_tweetid(tweet):
    tweetid=tweet['id_str']
    return tweetid

def process_or_store(tweet):
    #print(json.dumps(tweet))

    #print(tweet)
    #api.update_status('My status update @whoIReplyTo',tweetId) 
    #get user
    #get tweetid
    tweetid=tweet['id']
    user_id=tweet['user']['id']
    user_screen_name=tweet['user']['screen_name']
    #print(user_id,user_screen_name)
    text = tweet['text']
    entity_dict = tweet['entities']
    media_url=entity_dict['media'][0]['media_url']
    print("Tweet = %s" % (text))
    #print("media_url %s" % (media_url))
    sentences=tokenize.sent_tokenize(text)
    print()
    print("Text = %s" % (sentences[0]))
    print("Image = %s" % (sentences[1]))
    print()
    print("Checking Intent from Watson Conversation Service")
    conv_resp=find_intent(sentences[0])
    print()
    print("Intent identified = %s" % (conv_resp))
    if conv_resp == 'ImageQuestion':
        print("Classifying image %s using Watson Visual Recognition" % (media_url))
        classification=json.loads(classify_image(media_url))
        objclass=classification['images'][0]['classifiers'][0]['classes'][0]['class']
        objscore=classification['images'][0]['classifiers'][0]['classes'][0]['score']
        objclassifier=classification['images'][0]['classifiers'][0]['name']
        decision=''
        if objclassifier=='allowedvsnot':
             decision='allowed'
        else:
             decision='not allowed'
        print()
        result = "From IBM Watson: This is identified in the class of "+objclass+" with confidence "+str(objscore)+" and is "+decision+"."
        return result
     

consumer_key = 'FvpYJ2wsoX1x4kX3diMJjOx7d'
consumer_secret = 'gt447sGzfSo2HGn5KqPdStsHfaOhHyoGgNKXsJkLY1WphEi1Co'
access_token = '543950424-Uyo9RjutpuAZ8CAZ8uacrxTXPttwDd2420uhRFGO'
access_secret = 'bc6MwYXnufgYOS0FVq6wmzxxQ2ExBI0KHei4S6PRcdTtr'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

print("-----------------LATEST MESSAGE---------------")
for tweet in tweepy.Cursor(api.user_timeline).items(1):
    result=process_or_store(tweet._json)
    print(result)
    user_screen_name=get_user_screen_name(tweet._json)
    tweetid=get_tweetid(tweet._json)
    
    reply='@'+user_screen_name+' '+result 
    print("Posting reply = %s to tweetid = %s" % (reply, tweetid))
    #api.update_status(status='@VijaiGandikota my status',tweetid) 
    api.update_status(status=reply,in_reply_to_status_id=tweetid) 
    print("Done!")
    print()
