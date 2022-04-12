import requests
from bs4 import BeautifulSoup as bs

def get_covid_data_from_worldometer():

    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    soup = bs(r.text, "html.parser")
    print(soup.title.text)

    #Countries: Hong Kong, Germany, India, USA

    # Focusing on Total cases per 1M Population

    #Step 1.) Use Inspect Element and top left corner mouse button to find the attributes for the countries
    #I noticed that the countries all have this:
    #a class = "mt_a"
    content = soup.find_all("a", attrs={"class", "mt_a"})
    #so we find the country row by using the above class attirbutes
    #if we go up a level from the country label i.e. find_parent. Then we find_siblings, 
    # we can get the rest of the data for the country e.g. total cases per 1m population
    # The total cases per 1m population is the 8th item/column in that row


    countryData = {}

    for country in content:
        if country.text == "Hong Kong":
            countryData["Hong Kong"] = country.find_parent().find_next_siblings()[8].text
        elif country.text == "Germany":
            countryData["Germany"] = country.find_parent().find_next_siblings()[8].text
        elif country.text == "India": 
            countryData["India"] = country.find_parent().find_next_siblings()[8].text
        elif country.text == "USA":
            countryData["USA"] = country.find_parent().find_next_siblings()[8].text

        if len(countryData) > 4:
            break

    print(countryData)

    for country, data in countryData.items():
        print(f"{country} has {data} total cases per 1M population")

    return countryData

def tweet(countryData):
    #Write comments explaining above
    #Twitter API Output
    #Tweepy is like a python wrapper for the Twitter API
    #making it easier to interact w/ the Twitter API
    import tweepy
    #Must authenticate the user, cuz request comes from an actual twitter user

    #The below keys and secret keys can be found in the 'Developer Keys' Twitter section
    CONSUMER_KEY = 'secret'
    CONSUMER_SECRET = 'secret'
    ACCESS_KEY = 'secret'
    ACCESS_SECRET = 'secret'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    #Add a time stamp
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    for country, data in countryData.items():
        api.update_status((f"{country} has {data} total cases per 1M population. Timestamp: {current_time}"))

tweet(get_covid_data_from_worldometer())


#TODO:Using Pandas/Matplotlib

#Decorators to measure time performance



