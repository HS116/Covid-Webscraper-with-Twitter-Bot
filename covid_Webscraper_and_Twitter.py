import requests
from bs4 import BeautifulSoup as bs

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
print(f"Status code: {r.status_code}")
soup = bs(r.text, "html.parser")
print(soup.title.text)

#I initialized a Git repository by clicking on the 3 circle branch in left side bar
#Use the git Bash
