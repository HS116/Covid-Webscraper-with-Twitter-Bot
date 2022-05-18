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

    content = soup.find_all("a", attrs={"class", "mt_a"})

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


