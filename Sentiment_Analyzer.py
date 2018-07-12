import tweepy
from textblob import TextBlob 
import pandas as pd
import csv 


#Defining Consumer keys from Twitter 

consumer_key = 'Ex3WbnCCFx3w8hHuRTGhGlMkm'
consumer_secret = 'lYvL65QjI4FShzUemxOC23Xol5vxsAkxDKRy0nQi7an119OJqR'

#Defining Access Tokens

access_token = '3053458229-shVJH1Vd3IQtIKVDrz91tqw7Pi00zCpBoz6sXLp'
access_token_secret = 'iB4tDqeAFW4SK5WyGvFf5ABnuh5g5dFDvO1d1ivX7AnEK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Retrieve Tweets

public_tweets = api.search('Trump')

with open("/Users/shantanugarg/Documents/GitHub/Data-Science-Projects/Tweets.csv", "w" ) as output:
 writer = csv.writer(output, lineterminator='\n')


 output.write('tweet,sentiment_label\n')
 
 #Analyze the tweets
 for tweets in public_tweets: 
    analysis = TextBlob(tweets.text)
    sentiment = analysis.sentiment
    threshold = 0

    if sentiment[0]>threshold:
    	Sentiment_Label = 'Positive'
    else:
    	Sentiment_Label = 'Negative'



    #Save Each tweet in a CSV
    output.write('%s,%s\n' % (tweets.text.encode('utf8'), Sentiment_Label))


    
    
    


    



