# Scraping various COVID-19 Data to create comparisons and tweeting the findings

There are 3 components to this project:

## 1.) Beautiful soup webscraper of country specific covid data
Used Beautiful Soup to obtain information from (https://www.worldometers.info/coronavirus/) about the "Total cases per 1M Population" for the following countries: Hong Kong, Germany, India, USA\
Searched for elements with the class attribute of "mt_a" as they represented the country names\
Filtered out the countries I was interested in, by looking at the .text attribute\
Used find_parent() to get the whole row data of the country, and used find_siblings() to get all statistics\
The 8th index of find_siblings() was the "Total cases per 1M Population" information\
Stored the information in a dictionary and returned this dictionary in the function 

## 2.) Selenium webscraper of indian city specific covid data
Used Selenium and Chrome webdriver to obtain information from a dynamic website (https://www.incovid19.org/) about total confirmed cases and daily change in cases for the following cities/states:
Chennai, Bangalore (Urban), Delhi, Mumbai\
WARNING: The chromedriver on this repo is for Linux\
Found all relevant elements to click and scrape data from using the full XPath \
General process\
1.) click on relevant element to sort the states by alphabetical order\
2.) click on the state\
3.) click on relevant element to sort the districts/cities of the state by alphabetical order\
4.) scrape the relevant data from the particular district/city\
5.) store this data in a dictionary\
Returned the dictionary of total confirmed cases in respective function, and also returned daily change in cases for respective function

## 3.) Tweeting the result
Retrieved my twitter developer keys/tokens from local JSON file (not on Github because of Gitignore)\
Used Tweepy library and my keys/tokens to make it easier to create the "auth" using the OAuthHandler, set the access_token of auth, and finally create my API\
Used the result dictionaries from above functions to output the relevant data in a tweet by updating status

## Extra
Also used time decorators to measure the time taken for each particular data scraping function\
Applied some Python unit testing on 12th April 2022 for one of the data scraping functions


## Bot in action
https://twitter.com/LilRengsayeed

## Future plans for project:
1.) Write cleaner code e.g. break down the large functions into many smaller functions, maybe better variable/function names, reduce comments, add type annotations\
2.) Automate storing the data in a JSON or CSV\
3.) Automate the bot running in the background, so I don't have to press run\
4.) Generate a plotly graph as well, and display this through the twitter update
