from CountryCovidScraper import get_covid_data_from_worldometer as countryCovidData
from indianCitiesCovidScraper import get_indian_cities_covidcases_data
from indianCitiesCovidScraper import get_indian_cities_covid_change_data
import json
#Tweepy is like a python wrapper for the Twitter API
#making it easier to interact w/ the Twitter API
import tweepy

def tweet(countryData, typeOfStat):

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

    #Add a time stamp
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    for country, data in countryData.items():
        api.update_status((f"{country} has {data} {typeOfStat}. Timestamp: {current_time}"))



tweet(countryCovidData(), "total cases per 1M population")
tweet(get_indian_cities_covidcases_data(), "total confirmed cases")
tweet(get_indian_cities_covid_change_data(), "change in cases")