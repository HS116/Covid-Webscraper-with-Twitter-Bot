from CountryCovidScraper import get_covid_data_from_worldometer as get_country_covid_data
from indianCitiesCovidScraper import get_indian_cities_covidcases_data
from indianCitiesCovidScraper import get_indian_cities_covid_change_data
from tweeting import tweet as tweet
from json_creation import create_json_file


country_covid_data = get_country_covid_data()
indian_cities_covidcases_data = get_indian_cities_covidcases_data()
indian_cities_covid_change_data = get_indian_cities_covid_change_data()


create_json_file(country_covid_data, "Country_specific_total_covid_cases_per_1M_population")
create_json_file(indian_cities_covidcases_data, "Indian_city_specific_total_confirmed_cases")
create_json_file(indian_cities_covid_change_data, "Indian_city_specific_daily_change_in_cases")


'''
tweet(country_covid_data, "total cases per 1M population")
tweet(indian_cities_covidcases_data, "total confirmed cases")
tweet(indian_cities_covid_change_data, "change in cases")

'''

