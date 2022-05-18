#Tweepy is like a python wrapper for the Twitter API
#making it easier to interact w/ the Twitter API
import tweepy
import json
from datetime import datetime


#Must authenticate the user, cuz request comes from an actual twitter user
#The below keys and secret keys can be found in the 'Developer Keys' Twitter section
with open ("twitterTokensKeys.json", "r") as f:
    TokensKeys = json.load(f)

CONSUMER_KEY = TokensKeys["CONSUMER_KEY"]
CONSUMER_SECRET = TokensKeys["CONSUMER_SECRET"]
ACCESS_KEY = TokensKeys["ACCESS_KEY"]
ACCESS_SECRET = TokensKeys["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet(covid_data, typeOfStat):

    #Add a time stamp
    now = datetime.now()

    current_time = now.strftime("%d-%m-%Y %H:%M:%S")

    for country, data in covid_data.items():
        api.update_status((f"{country} has {data} {typeOfStat}. Timestamp: {current_time}"))

def tweetGraph(filepath, description):

    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")

    api.update_status_with_media(f"{description} \nTimestamp: {current_time}", filepath)
    
