from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

driver = webdriver.Chrome()

url = "https://www.incovid19.org/"

driver.get(url)
driver.implicitly_wait(3)
#Use the "full X-path" rather than the normal one, otherwise Selenium driver cannot find it
#Click on the element to sort the states by alphabetical order
driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[1]/div[1]').click()
driver.implicitly_wait(1)
#Click on Tamilnadu
driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[32]/div[1]').click()
driver.implicitly_wait(1)
#Click on the element to sort the districts by alphabetical order
driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[34]/div[1]').click()
driver.implicitly_wait(1)
chennai_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[37]/div[2]/div[2]').text
chennai_new_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[37]/div[2]/div[1]').text

#Click on Karnataka
driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[17]/div[1]').click()
#Click on the element to sort the districts by alphabetical order
driver.implicitly_wait(1)
driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[19]/div[1]').click()
bangalore_urban_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[24]/div[2]/div[2]').text
bangalore_urban_new_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[24]/div[2]/div[1]').text


#Click on Maharastra 
driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[54]/div[1]').click()
#Click on the element to sort the districts by alphabetical order
driver.implicitly_wait(1)
driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[56]/div[1]').click()
driver.implicitly_wait(1)
mumbai_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[41]/div[2]/div[2]').text
mumbai_new_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[73]/div[2]/div[1]').text

#Scrap data directly from Delhi since it is a state
dehli_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[10]/div[2]/div[2]').text
dehli_new_covid_cases = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[10]/div[2]/div[1]').text


print("\n\n\n\n\n")
#Add time stamp
now = datetime.now()
current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Current time in my local timezone: {current_date}")
print(f"Chennai current confirmed covid cases: {chennai_covid_cases}")
print(f"Chennai new covid cases: {chennai_new_covid_cases}")
print(f"Bangalore (Urban) current confirmed covid cases: {bangalore_urban_covid_cases}")
print(f"Bangalore Urban new covid cases: {bangalore_urban_new_covid_cases}")
#BUG w/ Mumbai covid cases
#print(f"Mumabi current confirmed cases: {mumbai_covid_cases}")
print(f"Mumbai new covid cases: {mumbai_new_covid_cases}")
print(f"Delhi current confirmed cases: {dehli_covid_cases}")
print(f"Delhi new covid cases: {dehli_new_covid_cases}")

driver.quit()







