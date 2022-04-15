import requests
from bs4 import BeautifulSoup as bs

from timer_decorator import timer_decorator

@timer_decorator
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



#Create a similar web scrapping function but for a different website e.g. Indian covid website
#because this website is interactive hence I can use Selenium



#TODO:Using Pandas/Matplotlib/Plotly to present the data

#TODO: Store the data in a json/csv file

#TODO: Create a website with frontend and backend which stores/presents university memes 
# and people can like/comment on each meme
#automate downdloading pictures from Zulip PGDP Meme channel
#automate instagram bot to download pictures from insta tummemes
#build login/auth system maybe using Google OAuth






