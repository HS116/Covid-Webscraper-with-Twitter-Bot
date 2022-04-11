import requests
from bs4 import BeautifulSoup as bs

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
#scraping text
#if we go up a level from the country label i.e. find_parent. Then we find_siblings, 
# we can get the total cases per 1m population for the countries we wanted

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

