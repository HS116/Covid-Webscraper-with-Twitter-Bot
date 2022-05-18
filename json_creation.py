import json

#Serialize json from dictionaries developed from web scraping
#TODO: store the change in indian covid cities covid data in json file. 
#Issue is that the up arrow is represented as "/u2191", and we need to remove that, could u lamda function for that

def create_json_files(country_covid_data, indian_cities_covidcases_data, indian_cities_covid_change_data):

    #convert the string values of each dictionary to integer to make it easier for future data analysis
    #using dict() and list comprehension    
    
    country_covid_data = convert_text_val_of_dict(country_covid_data)
    

    indian_cities_covidcases_data = convert_text_val_of_dict(indian_cities_covidcases_data)


    indian_cities_covid_change_data = convert_text_val_of_dict(indian_cities_covid_change_data)

    country_covid_data_json_object = json.dumps(country_covid_data, indent=4)
    indian_cities_covidcases_json_object = json.dumps(indian_cities_covidcases_data, indent=4)
    indian_cities_covid_change_json_object = json.dumps(indian_cities_covid_change_data, indent=4)

    print(country_covid_data_json_object)
    print(indian_cities_covidcases_json_object)
    print(indian_cities_covid_change_json_object)

def convert_text_to_int(text):
    #remove commas and the '\u2191' which represents the up arrow character
    return int(text.replace(',', '').replace('\u2191', ''))

def convert_text_val_of_dict(dictionary):
    return dict([key, convert_text_to_int(value)] for key, value in dictionary.items())

