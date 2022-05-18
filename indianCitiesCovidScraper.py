from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from timer_decorator import timer_decorator

@timer_decorator
def get_indian_cities_covidcases_data():

    indian_cities_covidcases = {}


    driver = webdriver.Chrome('/home/neilalb116/repos/Python-Files/Covid-Webscraper-with-Twitter-Bot/chromedriver')

    url = "https://www.incovid19.org/"

    driver.get(url)
    driver.implicitly_wait(3)
    #Click on the element to sort the states by alphabetical order
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[1]/div[1]').click()
    driver.implicitly_wait(1)
    #Click on Tamilnadu
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[32]/div[1]').click()
    driver.implicitly_wait(1)
    #Click on the element to sort the districts by alphabetical order
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[34]/div[1]').click()
    driver.implicitly_wait(1)
    indian_cities_covidcases["Chennai"] = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[37]/div[2]/div[2]').text
    

    #Click on Karnataka
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[17]/div[1]').click()
    #Click on the element to sort the districts by alphabetical order
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[19]/div[1]').click()
    indian_cities_covidcases["Bangalore (Urban)"] = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[24]/div[2]/div[2]').text


    #Scrape data directly from Delhi since it is a state
    indian_cities_covidcases["Delhi"] = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[10]/div[2]/div[2]').text


    driver.quit()
    return indian_cities_covidcases


@timer_decorator
def get_indian_cities_covid_change_data():
    driver = webdriver.Chrome('/home/neilalb116/repos/Python-Files/Covid-Webscraper-with-Twitter-Bot/chromedriver')

    url = "https://www.incovid19.org/"

    indian_cities_covid_change = {}

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
    indian_cities_covid_change["Chennai"] = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[37]/div[2]/div[1]').text

    #Click on Karnataka
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[17]/div[1]').click()
    #Click on the element to sort the districts by alphabetical order
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[19]/div[1]').click()
    indian_cities_covid_change["Bangalore (Urban)"] = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[24]/div[2]/div[1]').text

    #Scrape data directly from Delhi since it is a state
    indian_cities_covid_change["Delhi"] = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[4]/div[2]/div/div[10]/div[2]/div[1]').text

    driver.quit()
    return indian_cities_covid_change
